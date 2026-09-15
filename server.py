from flask import Flask, jsonify, render_template, request

from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    text_to_analyze = request.values.get("text", "")
    if not text_to_analyze.strip():
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    return jsonify(emotion_detector(text_to_analyze))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
