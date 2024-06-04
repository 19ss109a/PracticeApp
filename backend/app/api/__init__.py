from fastapi import APIRouter
from .endpoints import image_recognition_api

router = APIRouter()
router.include_router(image_recognition_api.router, prefix="/ir", tags=["ir"])