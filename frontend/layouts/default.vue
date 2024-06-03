<template>
  <v-app>
    <v-app-bar app color="pink" dark>
      <v-toolbar-title>MJP</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn text @click="$router.push('/')">Home</v-btn>
        <v-btn text>About</v-btn>
        <v-menu bottom left>
        <template v-slot:activator="{ on }">
          <v-btn text v-on="on">Services</v-btn>
        </template>
        <v-list>
          <v-list-item @click="$router.push('/page-image-recognition')">
            <v-list-item-title>Image Recognition</v-list-item-title>
          </v-list-item>
            <!-- 他のサービスアイテムをここに追加 -->
        </v-list>
        </v-menu>
        <v-btn text>Contact</v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>

    <v-footer app color="pink" dark>
      <v-col class="text-center">Everything in this app is Copyleft</v-col>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.v-application--wrap {
  min-height: 100vh;
}
</style>
