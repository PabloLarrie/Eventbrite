<template>
  <general-layout>
    <template v-slot:generalBody>

      <div class="text-center">
        <b-dropdown id="dropdown-form" text="Filter events by:" ref="dropdown">
          <b-dropdown-form >
            <b-form-checkbox
              id="checkbox-1"
              v-model="online_status"
              name="checkbox-1"
              value="Online"
              unchecked-value="all"
            >Online Events</b-form-checkbox>
          </b-dropdown-form>
          <b-dropdown-form >
            <b-form-checkbox
              id="checkbox-2"
              v-model="online_status"
              name="checkbox-2"
              value="Offline"
              unchecked-value="all"
            >Physical Events</b-form-checkbox>
          </b-dropdown-form>
        </b-dropdown>
      </div>
      <p>Filtering events by: <strong>{{ online_status}}</strong></p>

      <b-navbar >
        <div
          v-for="event in items"
          v-bind:key="event.id"
          >
          <div
            class="ms-lg-5"
            v-if="event.is_online && online_status === 'Online' ||
            !event.is_online && online_status === 'Offline' ||
            online_status === 'all'"
            style="max-width: 20rem; max-height:25rem;"
            @click="imgClick(event.id)"
            >
            <img
                :src="event.get_thumbnail"
                alt="image" class="rounded"
                style="width: 20rem; height:20rem; object-fit: cover;"
            />
            <b-card-sub-title class="text-center mt-2">{{ event.name }}</b-card-sub-title>
            <b-card-title class="text-center mt-2 mb-2">{{ event.location }}</b-card-title>
          </div>
        </div>
      </b-navbar>
    </template>

  </general-layout>
</template>

<script>
import GeneralLayout from "@/layouts/GeneralLayout";
import axios from "axios";

export default {
  name: "EventsList",
  components: {
    GeneralLayout,
  },

  data() {
    return {
      items: [],
      online_status: "all",
    };
  },
  mounted() {
    axios
      .get("http://localhost:8000/events/")
      .then(response => (this.items = response.data))
   },
  methods: {
    imgClick(id) {
      this.$router.push({
        name: "detail-event",
        params: { eventID: id },
      });
    },
    onlineSwitch() {
      this.online = !this.online
    }
  },
};
</script>
<style>
</style>