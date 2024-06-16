import random
from fastapi import FastAPI

app = FastAPI()
# todo add /ua and /en routes and for both of those add a route to list all available Bible translations or versions

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


def clean_reference(reference: str) -> str:
    return reference.replace("%20", " ").replace(".", ":")


@app.get("/random")
def get_random_verse():
    return verses[random.randint(0, len(verses) - 1)]


@app.get("/{reference}")
def get_verse(reference: str):
    reference = clean_reference(reference)
    # TODO parse reference to get correct Book, Chapter and Verse values
    print(reference)
    for verse in verses:
        if verse.get("reference") == reference:
            return verse

    return {"error": "Verse not found", "reference": reference}


@app.get("/")
def show_hint():
    return "Enter a reference to get a verse"
