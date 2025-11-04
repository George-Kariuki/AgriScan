from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import io
import numpy as np
import os
from ..utils.model_loader import TFLiteModel

router = APIRouter(tags=["Prediction"])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
LABELS_FILE = os.path.join(BASE_DIR, "models", "labels.txt")

def load_labels():
    if os.path.exists(LABELS_FILE):
        with open(LABELS_FILE, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    return ["Cassava Bacterial Blight (CBB)",
            "Cassava Brown Streak Disease (CBSD)",
            "Cassava Green Mottle (CGM)",
            "Cassava Mosaic Disease (CMD)",
            "Healthy"]

CLASS_NAMES = load_labels()

try:
    model = TFLiteModel()
except Exception as e:
    model = None
    load_error = str(e)
else:
    load_error = None

def preprocess_image(file_bytes: bytes, target_size=(224, 224)):
    """
    Load bytes -> PIL -> resize -> numpy float32 normalized [0,1]
    """
    try:
        img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
    except Exception as e:
        raise ValueError("Invalid image file") from e

    img = img.resize(target_size)
    arr = np.array(img).astype(np.float32) / 255.0  # normalize
    return arr

@router.post("/predict")
async def predict(image: UploadFile = File(...)):
    # Early checks
    if model is None:
        raise HTTPException(status_code=500, detail=f"Model not loaded: {load_error}")

    # Read image bytes
    contents = await image.read()
    try:
        img_array = preprocess_image(contents)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid image file")

    # Model predict (TFLite)
    preds = model.predict(img_array)  # shape [1, n_classes] or [n_classes]
    # handle shapes
    preds = np.array(preds)
    if preds.ndim == 2:
        probs = preds[0]
    else:
        probs = preds

    top_idx = int(np.argmax(probs))
    top_conf = float(probs[top_idx])

    class_label = CLASS_NAMES[top_idx] if top_idx < len(CLASS_NAMES) else f"class_{top_idx}"

    response = {
        "class": class_label,
        "confidence": round(top_conf, 4)
    }
    return JSONResponse(response)
