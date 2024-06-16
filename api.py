import random
from fastapi import FastAPI

from lib import clean_reference, decypher_reference

app = FastAPI()
"""
TODO
add /ua and /en routes and for both of those add a route to list all available Bible translations
add a database from which we will query our Bible verses
    in database create tables for each Bible version
create Bible Book Names correspondance table
try out pydantic and sqlalchemy with sqlite3
"""

verses: list[dict[str, str]] = [
    {
        "text": "For the wages of sin is death, but the gracious gift of God is eternal life in Christ Jesus our Lord",
        "reference": "Romans 6:23",
    },
    {
        "text": "For God so loved the world, that He gave His only Son, so that everyone who believes in Him will not perish, but have eternal life",
        "reference": "John 3:16",
    },
]


@app.get("/")
def show_hint() -> str:
    return "Enter a reference to get a verse"


@app.get("/random")
def get_random_verse() -> dict[str, str]:
    return verses[random.randint(0, len(verses) - 1)]


@app.get("/all")
def get_all_verses() -> list[dict[str, str]]:
    return verses


@app.get("/{reference}")
def get_verse(reference: str) -> dict[str, str]:
    reference = decypher_reference(reference)
    for verse in verses:
        if verse.get("reference") == reference:
            return verse

    return {"error": "Verse not found", "reference": reference}
