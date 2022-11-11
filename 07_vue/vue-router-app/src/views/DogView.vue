<template>
  <div>
    <p v-if="!imgSrc">{{ message }}</p>
    <img :src="imgSrc" alt="">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data() {    // 이미지 주소를 API로부터 받아서 저장
    return {
      imgSrc: null,
      message: '로딩중'
    }
  },
  methods: {
    getDogImage() {
      const breed = this.$route.params.breed
      const dogImageUrl = `https://dog.ceo/api/breed/${breed}/images/random`
      axios({
        method: 'get',
        url: dogImageUrl
      })
        .then((response) => {
          console.log((response))
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          this.message = `${this.$route.}`
          console.log(error)

        })
    }
  },
  created() {
    this.getDogImage()
  }
}
</script>

<style>

</style>