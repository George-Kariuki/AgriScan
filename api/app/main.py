from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AgriScan API running"}
