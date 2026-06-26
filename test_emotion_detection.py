import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_emotion_detector_happy(self):
        """Test emotion detection with a happy statement."""
        result = emotion_detector("I am so happy today!")
        self.assertIsNotNone(result)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_emotion_detector_sad(self):
        """Test emotion detection with a sad statement."""
        result = emotion_detector("I am feeling very sad today.")
        self.assertIsNotNone(result)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_emotion_detector_angry(self):
        """Test emotion detection with an angry statement."""
        result = emotion_detector("I am extremely angry right now!")
        self.assertIsNotNone(result)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_emotion_detector_fear(self):
        """Test emotion detection with a fearful statement."""
        result = emotion_detector("I am terrified of the dark.")
        self.assertIsNotNone(result)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['dominant_emotion'], 'fear')
    
    def test_emotion_detector_disgust(self):
        """Test emotion detection with a disgusting statement."""
        result = emotion_detector("This food tastes disgusting!")
        self.assertIsNotNone(result)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_emotion_detector_empty(self):
        """Test emotion detection with empty input."""
        result = emotion_detector("")
        self.assertIsNotNone(result)
        self.assertIsNone(result.get('dominant_emotion'))
    
    def test_emotion_detector_blank(self):
        """Test emotion detection with blank input."""
        result = emotion_detector("   ")
        self.assertIsNotNone(result)
        self.assertIsNone(result.get('dominant_emotion'))
    
    def test_emotion_detector_null(self):
        """Test emotion detection with None input."""
        result = emotion_detector(None)
        self.assertIsNotNone(result)
        self.assertIsNone(result.get('dominant_emotion'))

if __name__ == '__main__':
    unittest.main()
