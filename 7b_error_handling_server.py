"""
Flask server for the Emotion Detection application.
Task 7: Handles blank input errors — returns user-friendly message when
        emotion_detector returns None (status 400 from Watson API).
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to detect emotions from text provided as a query parameter.
    Handles blank input by returning an error message.

    Returns:
        str: Formatted emotion scores and dominant emotion, or error message
             if the input is blank or invalid.
    """
    text_to_analyse = request.args.get('textToAnalyse')

    # Handle blank input before calling the API
    if not text_to_analyse or text_to_analyse.strip() == "":
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyse)

    # Handle the case where Watson returns status 400 (None values)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant = result['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant}</b>."
    )


@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
