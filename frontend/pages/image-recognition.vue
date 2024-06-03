<template>
  <v-container>
    <h1 class="text-center">AIアプリ</h1>
    <v-row>
      <v-col cols="12">
        <v-file-input label="画像をアップロード" v-model="selectedImage" accept="image/*"></v-file-input>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" class="text-center">
        <v-btn @click="postImageAndRecognize" color="primary">実行</v-btn>
      </v-col>
    </v-row>
    <v-row v-if="result">
      <v-col cols="12">
        <v-card outlined>
          <v-card-title>結果</v-card-title>
          <v-card-text>
            <div>Predicted Class: {{ result.predicted_class }}</div>
            <div>Confidence: {{ result.confidence }}%</div>
          </v-card-text>
          <v-img :src="selectedImage" v-if="selectedImage" class="mx-auto" max-width="400"></v-img>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      selectedImage: null,
      result: null
    }
  },
  methods: {
    async postImageAndRecognize() {
      try {
        if (!this.selectedImage) {
          return;
        }
        // FastAPIのエンドポイント
        const endpoint = process.env.fastApiEndpoint + 'predict/'

        // FormDataオブジェクトを作成して画像を追加
        const formData = new FormData()
        formData.append('file', this.selectedImage)

        // POSTリクエストを送信してFastAPIに画像を送信
        const response = await axios.post(endpoint, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })

        // レスポンスのデータを返す
        console.log(response)
        this.result = response.data;
      } catch (error) {
        // エラー処理
        console.error('Error sending image to FastAPI:', error)
        throw error
      }
    }
  }
}
</script>

<style>
</style>