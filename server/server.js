const express = require("express");
const Bible = require("../bible.json")

const app = express();
const port = 3000;

app.get("/", (req, res) => {
    return res.status(200).send("Please enter a Bible place in a format /Book/Chater/Verse or just /Book/Chapter/")
})

app.get("/:book/:chapter", (req, res) => {
    const book = req.params.book;
    let chapter = req.params.chapter;

    if (!chapter || chapter < 1 || chapter > 150) chapter = 1;

    const BibleBooks = Object.keys(Bible);
    if (!BibleBooks.includes(book)) return res.status(404).send("The provided book name was not found. Make sure the format is 3-letters capitalized: GEN, ROM, 1CO.")

    const result = Bible[book][chapter];
    if (!result || result === null) return res.status(404).send("Couldn't find the chapter specified. Please check the URL to make sure it's in the correct format.")

    return res.status(200).json(result);
})

app.get("/:book/:chapter/:verse", (req, res) => {
    const book = req.params.book;
    let chapter = req.params.chapter;
    const verse = req.params.verse;

    if (!chapter || chapter < 1 || chapter > 150) chapter = 1;

    const BibleBooks = Object.keys(Bible);
    if (!BibleBooks.includes(book)) return res.status(404).send("The provided book name was not found. Make sure the format is 3-letters capitalized: GEN, ROM, 1CO.")

    const result = Bible[book][chapter][verse];
    if (!result || result === null) return res.status(404).send("Couldn't find the verse provided. Please check the URL to make sure it is in the correct format.")

    return res.status(200).json(result);
})

app.listen(port)