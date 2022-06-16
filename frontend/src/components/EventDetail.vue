<template>
  <general-layout>
    <template v-slot:generalBody>
      <div>
       <img
          :src="items.get_image"
          alt="Card image"
          style="position:relative; width: 100%; max-height:40%; object-fit: cover; filter: blur(12px); z-index:1"
          >

        <ul style="position:absolute; margin:-22% 15%; width:100%; display:grid; grid-template-columns:repeat(3,1fr); z-index: 3">
          <b-card-group deck v-bind:key="items.id">
            <img
                :src="items.get_image"
                alt="Card image" class="mb-3"
                style="width: 60rem; height:40rem; object-fit:cover; z-index: 2"
            >
          </b-card-group >
          <b-card  style="width: 20rem; height:40rem;">
            <b-card-title class="text-center mb-4 mt-3 fs-3">{{ items.name }}</b-card-title>
            <b-card-sub-title class="text-center mb-4 fs-4">{{ items.location }}</b-card-sub-title>
            <b-card-sub-title class="text-center mb-5" style="font-size: 14px;">
              {{ items.description }}</b-card-sub-title>
            <b-card-sub-title class="text-center mb-5">Starts: {{ items.start_date }}</b-card-sub-title>
            <b-card-sub-title class="text-center mb-3">{{ items.is_online ? 'Online' : '' }}</b-card-sub-title>
            <div class="col text-center">
              <b-button v-on:click="ticketClick(items.id)" variant="outline-info">Buy Tickets</b-button>
            </div>
          </b-card>
        </ul>
      </div>

    </template>
  </general-layout>
</template>

<script>

import GeneralLayout from "@/layouts/GeneralLayout";
import axios from "axios";

export default {
  name: "EventDetail",
  components: {
    GeneralLayout,
  },
  props: {
    eventID: {
      required: true,
    },
  },
  data() {
    return {
      items: [],
    }
  },
  mounted() {
    axios
     .get("http://localhost:8000/events/" + this.eventID)
     .then(response => (this.items = response.data))
   },
  methods: {
    ticketClick(id) {
      this.$router.push({
        name: "detail-ticket",
        params: { EventID: id },
      });
    },
  },
}
</script>

<style>
</style>