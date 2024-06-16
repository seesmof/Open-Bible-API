"""
use this to fill in the database
"""


def form_verse(
    text: str,
    book: str,
    chapter: int,
    verse: int,
    lang: str = "en",
    version: str = "BSB",
):
    reference: str = f"{book.title()} {chapter}:{verse}"

    return {
        "text": text,
        "book": book,
        "chapter": chapter,
        "verse": verse,
        "reference": reference,
        "lang": lang,
        "version": version,
    }
