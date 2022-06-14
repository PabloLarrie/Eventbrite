<template>
  <table-layout>
    <template v-slot:table>
<!--      <b-table-->
<!--        class="w-100"-->
<!--        striped-->
<!--        hover-->
<!--        fixed-->
<!--        noCollapse-->
<!--        :fields="columns"-->
<!--        :items="items"-->
<!--        >-->
<!--      </b-table>-->
<!--      <span>{{ items }}</span>-->

      <ul style="margin-top:20px; width:100%; display:grid; grid-template-columns:repeat(4,2fr);">
        <b-card
          v-for="event in items"
          v-bind:key="event.id"
          no-body
          style="max-width: 20rem; max-height:25rem;"
          >
          <img
              :src="event.get_image"
              alt="image" class="rounded"
              style="width: 20rem; height:20rem; object-fit: cover">
          <b-card-title class="text-center">{{ event.name }}</b-card-title>
          <b-card-sub-title class="text-center">{{ event.location }}</b-card-sub-title>
        </b-card>
      </ul>


<!--      <ul style="display: grid; grid-template-columns:repeat(4,2fr);">-->
<!--        <b-card-->
<!--          no-body-->
<!--          style="max-width: 25rem;">-->
<!--          <img :src="items[0].get_thumbnail" alt="image" class="rounded">-->
<!--          <b-card-title>asdasd</b-card-title>-->
<!--          <b-card-sub-title>asdasd</b-card-sub-title>-->
<!--        </b-card>-->

<!--        <b-card-->
<!--          no-body-->
<!--          style="max-width: 25rem;">-->
<!--          <img :src="items[0].get_thumbnail" alt="image" class="rounded">-->
<!--          <b-card-title>asdasd</b-card-title>-->
<!--          <b-card-sub-title>asdasd</b-card-sub-title>-->
<!--        </b-card>-->
<!--      </ul>-->

    </template>

  </table-layout>
</template>

<script>
import TableLayout from "@/layouts/TableLayout";
import axios from "axios";

export default {
  name: "EventsList",
  components: {
    TableLayout,
  },
  data() {
    return {
      items: [],
      columns: [
        "id",
        "name",
        "get_image",
        "get_thumbnail",
        "is_online",
      ],
    };
  },
  mounted() {
    axios
      .get("http://localhost:8000/events/")
      .then(response => (this.items = response.data))
   },
  // methods: {
  //   loadData(url) {
  //     this.$api.get(url).then((response) => {
  //       this.items = response.data.results;
  //     });
  //   },
  // },
};
</script>
<style scoped>
</style>