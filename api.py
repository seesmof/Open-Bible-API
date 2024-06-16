from fastapi import FastAPI

app = FastAPI()

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


@app.get("/{reference}")
def get_verse(reference: str):
    for verse in verses:
        if verse["reference"] == reference:
            return verse
