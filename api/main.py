from flask import Flask, request, jsonify
from sqlalchemy import func
from models import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/<reference>", methods=["GET"])
def get_verse(reference):
    """
    reference: str - main parameter for the verse reference

    random: bool - returns random verse
    """

    is_random: bool = request.args.get("random")
    if is_random:
        verse: dict = db.BibleVerse.query.order_by(func.random()).first().to_dict()
    else:
        verse: dict = (
            db.BibleVerse.query.filter_by(reference=reference).first().to_dict()
        )

    if not verse:
        return jsonify({"error": "Verse not found"}), 404
    else:
        return jsonify(verse), 200


@app.route("/all", methods=["GET"])
def get_all_verses():
    """
    output a json of all Bible verses
    """
    return jsonify([]), 200
