POST /api/predict
Content-Type: multipart/form-data
Body: image=<leaf photo>

Response:
{
  "status": "success",
  "prediction": "cassava_mosaic",
  "confidence": 0.87,
  "remedy": "Apply XYZ in early stage"
}
