import json
import requests

def emotion_detector(text_to_analyze):
    """Detect emotions from text using Watson NLP API."""
    
    # Handle empty input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Watson NLP API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Make API request
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        # Parse response
        result = response.json()
        emotions = result.get('emotionPredictions', [{}])[0].get('emotion', {})
        
        # Extract scores
        anger = emotions.get('anger', 0.0)
        disgust = emotions.get('disgust', 0.0)
        fear = emotions.get('fear', 0.0)
        joy = emotions.get('joy', 0.0)
        sadness = emotions.get('sadness', 0.0)
        
        # Find dominant emotion
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
        
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return {
            'error': f'API request failed: {str(e)}',
            'dominant_emotion': None
        }
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return {
            'error': f'Error parsing response: {str(e)}',
            'dominant_emotion': None
        }