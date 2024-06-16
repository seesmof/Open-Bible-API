from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/verse", methods=["GET"])
def get_verse():
    verse: dict = {
        "verse": "For GOD so loved the world that He gave His Only Son that whoever believes in Him should not perish but have eternal life.",
        "reference": "John 3:16",
    }

    return jsonify(verse)


if __name__ == "__main__":
    app.run(debug=True)
