# ベースイメージを指定
FROM node:latest

# 作業ディレクトリを設定
WORKDIR /app

# ホストのpackage.jsonとyarn.lockをコピーして依存関係をインストール
COPY package.json yarn.lock ./
RUN yarn install

# アプリケーションのソースコードをコピー
COPY . .

# ビルドされたアプリケーションを実行
CMD [ "yarn", "dev" ]

# ポート3000を開放
EXPOSE 3000