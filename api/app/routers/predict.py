from fastapi import APIRouter, File, UploadFile

router = APIRouter(tags=["Prediction"])

@router.post("/predict")
async def predict(image: UploadFile = File(...)):
    # Stub logic for now
    return {
        "status": "success",
        "message": "Model not loaded yet — stub response",
        "filename": image.filename
    }
