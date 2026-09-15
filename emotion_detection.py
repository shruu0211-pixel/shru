import json

import requests


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for supplied text."""
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp"
        "/v1/NlpService/EmotionPredict"
    )
    payload = {
        "raw_document": {"text": text_to_analyze},
    }
    response = requests.post(
        url,
        json=payload,
        headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        timeout=30,
    )

    if response.status_code == 404:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response.raise_for_status()
    result = response.json()
    emotions = result.get("emotionPredictions", [{}])[0].get("emotion", {})
    scores = {
        "anger": emotions.get("anger"),
        "disgust": emotions.get("disgust"),
        "fear": emotions.get("fear"),
        "joy": emotions.get("joy"),
        "sadness": emotions.get("sadness"),
    }
    scores["dominant_emotion"] = max(
        scores,
        key=lambda emotion: scores[emotion] if scores[emotion] is not None else -1,
    )
    return scores