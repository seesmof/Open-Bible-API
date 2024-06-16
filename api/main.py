from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from lib import to_dict

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()


class BibleVerse(db.Model):
    """
    text: str
    book: str
    chapter: int
    verse: int
    reference: str
    lang: str = "en" | "uk"
    version: str = "BSB" | "UBIO"
    """

    __tablename__ = "Bible_Verse"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), nullable=False)
    book = db.Column(db.String(), nullable=False)
    chapter = db.Column(db.Integer(), nullable=False)
    verse = db.Column(db.Integer(), nullable=False)
    reference = db.Column(db.String(), nullable=False)
    lang = db.Column(db.String(), nullable=False)
    version = db.Column(db.String(), nullable=False)

    def __repr__(self) -> str:
        return f"<BibleVerse {self.reference}>"


@app.route("/<reference>", methods=["GET"])
def get_verse(reference):
    """
    reference: str - main parameter for the verse reference

    random: bool - returns random verse
    """

    is_random: bool = request.args.get("random")
    if is_random:
        verse = BibleVerse.query.order_by(func.rand()).first()
    else:
        verse: dict = BibleVerse.query.filter_by(reference=reference).first()

    if not verse:
        return jsonify({"error": "Verse not found"}), 404
    else:
        return jsonify(to_dict(**verse)), 200


@app.route("/all", methods=["GET"])
def get_all_verses():
    """
    output a json of all Bible verses
    """
    return jsonify([]), 200
