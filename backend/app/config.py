from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "backend"
    DATABASE_URL: str = "dburl"
    
    # 画像認識AI(Image Recognition, IR)
    # MEMO: 別で切り出したほうがいいのかも
    IR_IMAGE_SIZE: int = 32
    IR_MODEL_FILE_PATH: str = './app/assets/ai-models/model_cnn_cifar10.h5'
    IR_CLASSES: list = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()