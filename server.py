from flask import Flask, request, render_template, jsonify
import sys
import os

# Add the current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from EmotionDetection.emotion_detection import emotion_detector
except ImportError as e:
    print(f"Import Error: {e}")
    print("Make sure EmotionDetection/__init__.py exists")
    sys.exit(1)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    try:
        text_to_analyze = request.args.get('textToAnalyze', '')
        
        if not text_to_analyze or text_to_analyze.strip() == "":
            return jsonify({'error': 'Invalid text! Please try again.'}), 400
        
        result = emotion_detector(text_to_analyze)
        
        if result.get('error'):
            return jsonify({'error': result['error']}), 500
        
        if result.get('dominant_emotion') is None:
            return jsonify({'error': 'Invalid text! Please try again.'}), 400
        
        # Return JSON response for AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify(result)
        
        # For browser, return formatted text
        formatted = "The given text has the following emotions:\n"
        formatted += f"anger: {result['anger']:.2f}\n"
        formatted += f"disgust: {result['disgust']:.2f}\n"
        formatted += f"fear: {result['fear']:.2f}\n"
        formatted += f"joy: {result['joy']:.2f}\n"
        formatted += f"sadness: {result['sadness']:.2f}\n"
        formatted += f"The dominant emotion is {result['dominant_emotion']}."
        return formatted.replace('\n', '<br>')
        
    except Exception as e:
        print(f"Server Error: {e}")
        return jsonify({'error': 'An error occurred. Please try again.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)