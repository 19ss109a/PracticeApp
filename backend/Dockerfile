# ベースイメージとしてPython 3.9を使用
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をコピーし、インストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# Uvicornサーバーをポート8000で起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]