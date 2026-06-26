document.addEventListener('DOMContentLoaded', function() {
    const analyzeBtn = document.getElementById('analyzeBtn');
    const textInput = document.getElementById('textInput');
    const resultDiv = document.getElementById('result');
    const errorDiv = document.getElementById('error');
    
    analyzeBtn.addEventListener('click', function() {
        const text = textInput.value.trim();
        
        // Reset display
        resultDiv.style.display = 'none';
        errorDiv.style.display = 'none';
        resultDiv.innerHTML = '';
        errorDiv.innerHTML = '';
        
        if (!text) {
            showError('Please enter some text to analyze.');
            return;
        }
        
        // Show loading state
        analyzeBtn.textContent = 'Analyzing...';
        analyzeBtn.disabled = true;
        
        // Make AJAX request
        fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            analyzeBtn.textContent = 'Analyze Emotions';
            analyzeBtn.disabled = false;
            
            if (data.error) {
                showError(data.error);
                return;
            }
            
            if (!data.dominant_emotion) {
                showError('Invalid text! Please try again.');
                return;
            }
            
            // Display results
            displayResults(data);
        })
        .catch(error => {
            analyzeBtn.textContent = 'Analyze Emotions';
            analyzeBtn.disabled = false;
            showError('An error occurred. Please try again.');
            console.error('Error:', error);
        });
    });
    
    function displayResults(data) {
        const emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness'];
        let html = '<h3>Emotion Analysis Results:</h3>';
        html += '<div class="emotion-scores">';
        
        emotions.forEach(emotion => {
            const score = data[emotion] || 0;
            const percentage = (score * 100).toFixed(0);
            html += `
                <div class="emotion-item">
                    <span class="emotion-name">${emotion.charAt(0).toUpperCase() + emotion.slice(1)}</span>
                    <div class="emotion-bar-container">
                        <div class="emotion-bar" style="width: ${percentage}%; background: ${getEmotionColor(emotion)};"></div>
                    </div>
                    <span class="emotion-score">${score.toFixed(2)}</span>
                </div>
            `;
        });
        
        html += '</div>';
        html += `<p class="dominant-emotion"><strong>Dominant Emotion:</strong> ${data.dominant_emotion.charAt(0).toUpperCase() + data.dominant_emotion.slice(1)}</p>`;
        
        resultDiv.innerHTML = html;
        resultDiv.style.display = 'block';
        resultDiv.className = 'result-section show';
    }
    
    function showError(message) {
        errorDiv.innerHTML = `<strong>Error:</strong> ${message}`;
        errorDiv.style.display = 'block';
        errorDiv.className = 'error-section show';
    }
    
    function getEmotionColor(emotion) {
        const colors = {
            'anger': '#e53e3e',
            'disgust': '#9b59b6',
            'fear': '#f39c12',
            'joy': '#2ecc71',
            'sadness': '#3498db'
        };
        return colors[emotion] || '#666';
    }
    
    // Allow Enter key to trigger analysis
    textInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            analyzeBtn.click();
        }
    });
});