from flask import Flask, jsonify, request
from flask import request
from sentiment_analysis import get_sentiment
import langid

app = Flask(__name__)

@app.route("/")
def hello():
    text = request.args.get("text")
    if text is None:
        return jsonify({"error": "text parameter is required"}), 400

    # Detect the language of the input text using langid
    lang, confidence = langid.classify(text)

    # Pass the detected language to the get_sentiment function
    message = get_sentiment(text, lang)

    return jsonify({"sentiment": message, "message": text, "language": lang})

if __name__ == "__main__":
    app.run()
