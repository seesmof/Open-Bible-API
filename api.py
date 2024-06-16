from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hallelujah thank YOU Jesus Christ our Holy Lord GOD Almighty"}
