import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_detector_returns_emotions(self, mock_post):
        mock_post.return_value = Mock(
            status_code=200,
            json=lambda: {
                "emotionPredictions": [
                    {
                        "emotion": {
                            "anger": 0.1,
                            "disgust": 0.2,
                            "fear": 0.3,
                            "joy": 0.8,
                            "sadness": 0.1,
                        }
                    }
                ]
            },
        )

        result = emotion_detector("I am very happy today")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.8)

    def test_detector_handles_blank_text(self):
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
