def to_dict(
    text: str,
    book: str,
    chapter: int,
    verse: int,
    reference: str,
    lang: str = "en",
    version: str = "BSB",
):
    return {
        "text": text,
        "book": book,
        "chapter": chapter,
        "verse": verse,
        "reference": reference,
        "lang": lang,
        "version": version,
    }
