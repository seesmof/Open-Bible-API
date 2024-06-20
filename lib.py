import re


def decode_reference_uri(reference: str) -> str:
    """
    Decodes a URI percent-encoded reference by replacing special characters with stringly ones

    IN:
    reference (str): The URI reference to be decoded

    OUT:
    str: The decoded URI reference
    """

    reference = (
        reference.strip().replace("%20", " ").replace(".", ":").replace("%3A", ":")
    )
    return reference


def decrypt_reference(reference: str) -> str:
    """
    Takes in an unformatted input reference in all sorts of formats. Some of the acceptable formats listed below:
        JN1.1
        JHN1.1
        JN.1.1
        John1.1
        John1:1
        JN 1.1
        JHN 1.1
        John 1.1
        John 1:1
    and returns the proper formatted reference in the format `Book Chapter:Verse`

    TODO:
    account for all those kinds of Bible references and decypher them into a proper Bible reference in format `Book Chapter:Verse`

    IN:
    reference (str): The reference to be decrypted

    OUT:
    str: The decrypted reference in format `Book Chapter:Verse` if the reference is valid, otherwise the original reference
    """

    reference = decode_reference_uri(reference)

    pattern: str = r"(?P<Book>[A-Za-z]+)[.: ]?(?P<Chapter>\d+)[.:](?P<Verse>\d+)"
    match: re.Match = re.match(pattern, reference)

    if match:
        Book = match.group("Book")
        Chapter = match.group("Chapter")
        Verse = match.group("Verse")
        return f"{Book.title()} {Chapter}:{Verse}"

    return reference


def decompose_reference(reference: str) -> tuple[str, str, str]:
    """
    Decomposes a reference string into its constituent parts: Book, Chapter, and Verse

    IN:
    reference (str): The reference string to decompose

    OUT:
    tuple[str, str, str]: A tuple containing the Book, Chapter, and Verse parts of the reference string
    """

    Book, Chapter_Verse = reference.split(" ")
    Chapter, Verse = Chapter_Verse.split(":")
    return Book, Chapter, Verse
