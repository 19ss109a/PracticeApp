from fastapi import APIRouter, File, UploadFile
from app.services.image_recognition_service import predict_image

router = APIRouter()

@router.post("/predict/")
async def predict(file: UploadFile = File(...)):
    return await predict_image(file)