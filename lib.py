import re


def clean_reference(reference: str) -> str:
    reference = (
        reference.strip().replace("%20", " ").replace(".", ":").replace("%3A", ":")
    )
    return reference


def decypher_reference(reference: str) -> str:
    reference = clean_reference(reference)

    """
    JN1.1
    JHN1.1
    JN.1.1
    John1.1
    John1:1
    JN 1.1
    JHN 1.1
    John 1.1
    John 1:1
    """

    """
    TODO
    account for all those kinds of Bible references and decypher them into a proper Bible reference in format `Book Chapter:Verse`
    """

    pattern = r"(?P<Book>[A-Za-z]+)[.: ]?(?P<Chapter>\d+)[.:](?P<Verse>\d+)"
    match = re.match(pattern, reference)

    if match:
        Book = match.group("Book")
        Chapter = match.group("Chapter")
        Verse = match.group("Verse")
        return f"{Book.title()} {Chapter}:{Verse}"

    return reference
