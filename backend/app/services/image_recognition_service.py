from PIL import Image
import io
import numpy as np
from tensorflow.keras.models import load_model
from fastapi.responses import JSONResponse
from app.config import settings

model = load_model(settings.IR_MODEL_FILE_PATH)

async def predict_image(file):
    try:
        # 画像を読み込む
        image = Image.open(io.BytesIO(await file.read()))
        image = image.convert("RGB")
        image = image.resize((settings.IR_IMAGE_SIZE, settings.IR_IMAGE_SIZE))
        data = np.asarray(image) / 255.0
        X = []
        X.append(data)
        X = np.array(X)
        
        result = model.predict([X])[0]
        predicted = result.argmax()
        rate = int(result[predicted] * 100)
 
        return {"predicted_class": settings.IR_CLASSES[predicted], "confidence": rate}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)