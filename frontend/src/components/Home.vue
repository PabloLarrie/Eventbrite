<template>
  <home-layout>
    <template v-slot:homeBody>
      <div>
        <h1>Wellcome to Eventbrite</h1>
<!--        <b-button>-->
<!--          <router-link to="/">Cards</router-link>-->
<!--        </b-button>-->
<!--        <b-button>-->
<!--          <router-link to="/decks">Decks</router-link>-->
<!--        </b-button>-->
      </div>
    </template>
  </home-layout>
</template>

<script>

import HomeLayout from "@/layouts/HomeLayout";

export default {
  name: "Home",
  components: {
    HomeLayout,
  },
  data() {
    return {}
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/*h3 {*/
/*  margin: 40px 0 0;*/
/*}*/
/*ul {*/
/*  list-style-type: none;*/
/*  padding: 0;*/
/*}*/
/*li {*/
/*  display: inline-block;*/
/*  margin: 0 10px;*/
/*}*/
/*a {*/
/*  color: #42b983;*/
/*}*/
</style>