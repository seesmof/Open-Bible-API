from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/<reference>", methods=["GET"])
def get_verse(reference):
    """
    reference: str - main parameter for the verse reference

    random: bool - returns random verse
    """
    verse: dict = {
        "verse": "For GOD so loved the world that He gave His Only Son that whoever believes in Him should not perish but have eternal life.",
        "reference": "John 3:16",
        "lang": "en",
        "version": "BSB",
    }
    verse["reference"] = reference

    return jsonify(verse), 200


"""
Bible database schema for getting random Bible verses 

verse: str 
reference: str 
lang: str = "en" | "uk"
version: str = "BSB" | "UBIO"
"""