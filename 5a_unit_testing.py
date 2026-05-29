"""
Unit tests for the emotion_detector function.
Task 5: Demonstrates required unit tests for all five emotions.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Unit tests for emotion_detector function."""

    def test_joy_detected_for_happy_statement(self):
        """Test that joy is the dominant emotion for a joyful statement."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_detected_for_angry_statement(self):
        """Test that anger is the dominant emotion for an angry statement."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_detected_for_disgusting_statement(self):
        """Test that disgust is the dominant emotion for a disgusting statement."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_detected_for_sad_statement(self):
        """Test that sadness is the dominant emotion for a sad statement."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_detected_for_fearful_statement(self):
        """Test that fear is the dominant emotion for a fearful statement."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
