import random
from fastapi import FastAPI

from lib import decypher_reference

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
    {
        "text": "for all have sinned and fall short of the glory of God",
        "reference": "Romans 3:23",
    },
    {
        "text": "But God demonstrates His own love toward us, in that while we were still sinners, Christ died for us.",
        "reference": "Romans 5:8",
    },
    {
        "text": "that if you confess with your mouth Jesus as Lord, and believe in your heart that God raised Him from the dead, you will be saved; for with the heart a person believes, resulting in righteousness, and with the mouth he confesses, resulting in salvation.",
        "reference": "Romans 10:9-10",
    },
    {
        "text": "for “Everyone who calls on the name of the Lord will be saved.”",
        "reference": "Romans 10:13",
    },
    {
        "text": "Therefore, having been justified by faith, we have peace with God through our Lord Jesus Christ",
        "reference": "Romans 5:1",
    },
    {
        "text": "For whatever was written in earlier times was written for our instruction, so that through perseverance and the encouragement of the Scriptures we might have hope.",
        "reference": "Romans 15:4",
    },
    {
        "text": "Therefore there is now no condemnation at all for those who are in Christ Jesus.",
        "reference": "Romans 8:1",
    },
    {
        "text": "Jesus said to him, “I am the way, and the truth, and the life; no one comes to the Father except through Me.",
        "reference": "John 14:6",
    },
    {
        "text": "Jesus responded and said to him, “Truly, truly, I say to you, unless someone is born again he cannot see the kingdom of God.”",
        "reference": "John 3:3",
    },
]


@app.get("/")
def show_hint() -> str:
    return "Enter a reference to get a verse"


@app.get("/random")
def get_random_verse() -> dict[str, str]:
    random_verse: dict[str, str] = random.choice(verses)
    return random_verse


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
