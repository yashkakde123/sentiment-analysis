from flask import Flask, jsonify, request
from sentiment_analysis import get_sentiment
import langid

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        text = request.args.get("text")
    elif request.method == "POST":
        text = request.form["text"]
    elif request.method == "HEAD":
        # Handle HEAD request method
        return jsonify({"message": "HEAD request received"}), 200

    # Detect the language of the input text using langid
    lang, confidence = langid.classify(text)

    # Pass the detected language to the get_sentiment function
    message = get_sentiment(text, lang)

    return jsonify({"sentiment": message, "message": text, "language": lang})

if __name__ == "__main__":
    app.run()
