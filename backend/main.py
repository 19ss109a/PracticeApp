from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
from tensorflow.keras.models import load_model, model_from_json
import numpy as np


# 固定値
IMAGE_SIZE = 32
MODEL_FILE_PATH = './models/model_cnn_cifar10.h5'
CLASSES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
NUM_CLASSES = len(CLASSES)
model = load_model(MODEL_FILE_PATH)

app = FastAPI()

# CORSミドルウェアを追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # リクエストを許可するオリジン
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # 画像を読み込む
        image = Image.open(io.BytesIO(await file.read()))
        image = image.convert("RGB")
        image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
        data = np.asarray(image) / 255.0
        X = []
        X.append(data)
        X = np.array(X)
        
        result = model.predict([X])[0]
        predicted = result.argmax()
        rate = int(result[predicted] * 100)
 
        print(CLASSES[predicted], rate)
        return {"predicted_class": CLASSES[predicted], "confidence": rate}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)