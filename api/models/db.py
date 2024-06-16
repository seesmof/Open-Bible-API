from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


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

    def to_dict(self):
        return {
            "text": self.text,
            "book": self.book,
            "chapter": self.chapter,
            "verse": self.verse,
            "reference": self.reference,
            "lang": self.lang,
            "version": self.version,
        }

    def __repr__(self) -> str:
        return f"<BibleVerse {self.reference}>"
