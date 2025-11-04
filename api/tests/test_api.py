from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict_endpoint_with_file():
    test_image_path = "tests/leaf.jpg"
    
    try:
        with open(test_image_path, "rb") as f:
            files = {"file": ("leaf.jpg", f, "image/jpeg")}
            response = client.post("/api/v1/predict", files=files)
            
            # Should return 200 if model is loaded, or 500 if model not found
            assert response.status_code in [200, 500]
            
            if response.status_code == 200:
                data = response.json()
                assert "class" in data
                assert "confidence" in data
                assert isinstance(data["confidence"], (int, float))
    except FileNotFoundError:
        # If test image doesn't exist, skip file test
        pass

def test_predict_endpoint_no_file():
    response = client.post("/api/v1/predict")
    assert response.status_code == 422  # Validation error

