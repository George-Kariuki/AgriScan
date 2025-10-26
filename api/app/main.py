from fastapi import FastAPI
from .routers import predict

app = FastAPI(
    title="AgriScan API",
    description="Offline Crop Disease Detection API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "AgriScan API running"}

# include predict router
app.include_router(predict.router, prefix="/api/v1")
