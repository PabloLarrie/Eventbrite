<template>
  <general-layout>
    <template v-slot:generalBody>
      <div>
        <b-alert
            :show="dismissCountDown"
            variant="success"
            dismissible
            fade
            @dismissed-count-down="countDownChanged"
        >
          <h4 class="alert-heading">Ticked Aded!</h4>
          <p>
            Congratulations, you have successfully added a ticket for this event to your shopping cart!
          </p>
          <hr>
        </b-alert>
      </div>

      <div v-if="!items[0]">
        <h1 class="text-center">This is a free event, so you don't need tickets to join it :)</h1>
      </div>

      <div>
        <b-card
          v-for="ticket in items"
          v-bind:key="ticket.id">
          <b-card >
            <b-card-title class="text-left mb-2 mt-2">{{ ticket.name }}</b-card-title>
            <b-card-sub-title class="text-left mb-2">{{ ticket.price }}{{ ticket.currency }}</b-card-sub-title>
            <b-card-sub-title v-if="ticket.is_available" class="text-left mb-2">
              Available
              <p><b-button @click="showAlert" variant="primary mt-2">
                Select this ticket
              </b-button></p>
            </b-card-sub-title>
            <b-card-sub-title v-else class="text-left mb-2">
              <strong>Sold Out</strong>
            </b-card-sub-title>
          </b-card>
        </b-card>
      </div>

    </template>
  </general-layout>
</template>

<script>

import GeneralLayout from "@/layouts/GeneralLayout";
import axios from "axios";

export default {
  name: "TicketDetail",
  components: {
    GeneralLayout,
  },
  props: {
    EventID: {
      required: true,
    },
  },
  data() {
    return {
      items: [],
      dismissSecs: 5,
      dismissCountDown: 0,
    }
  },
  mounted() {
    axios
     .get("http://localhost:8000/events/" + this.EventID + "/tickets/?ordering=price")
     .then(response => (this.items = response.data))
   },
   methods: {
      countDownChanged(dismissCountDown) {
        this.dismissCountDown = dismissCountDown
      },
      showAlert() {
        this.dismissCountDown = this.dismissSecs
      }
    }
}
</script>

<style>
</style>