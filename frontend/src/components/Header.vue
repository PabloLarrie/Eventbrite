-<template>
  <div id="header">
    <b-navbar toggleable="lg">
      <a class="navbar-header" href="/"><img src="@/assets/logo.png" alt=""></a>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="position-absolute end-50">
          <b-button pill class="button pt-2 pb-2 pe-3 ps-3">
            <router-link class="router-link " to="#" >Online</router-link>
          </b-button>
          <b-button pill class="button">
            <router-link class="router-link" to="#">Offline</router-link>
          </b-button>
        </b-navbar-nav>
        <b-navbar-nav class="position-absolute end-0 pe-3">
<!--          <b-button v-if="!token">-->
<!--            <router-link v-b-tooltip.hover.down="'Click to login!'" to="/login">Login</router-link>-->
<!--          </b-button>-->
<!--          <b-button v-if="!token">-->
<!--            <router-link v-b-tooltip.hover.down="'Click to Register!'" to="/register">Register</router-link>-->
<!--          </b-button>-->
<!--          <b-dropdown class="position-relative" v-if="token" :text="user.username">-->
<!--            <b-dropdown-item href="#" to="/settings">Settings</b-dropdown-item>-->
<!--            <b-dropdown-item @click="logOut">Log out</b-dropdown-item>-->
<!--          </b-dropdown>          -->
          <b-button pill class="button">
            <router-link class="router-link" to="#" >Login</router-link>
          </b-button>
          <b-button pill class="button">
            <router-link class="router-link" to="#">Register</router-link>
          </b-button>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>

// import {mapMutations, mapState} from "vuex";
// import {TOKEN_STORAGE_KEY} from "@/constants";
// import {PUBLIC_PAGES} from "@/constants";

export default {
  name: "MyHeader",
  data() {
    return {
      bg_color: '#2e2831'
    };
  },
  methods: {
    // ...mapMutations("userStore", ["setToken", "setUser"]),
    // logOut() {
    //   localStorage.removeItem(TOKEN_STORAGE_KEY)
    //   this.setToken(null);
    //   this.setUser(null);
    //   const currentRoute = this.$router.currentRoute.name
    //   if (!PUBLIC_PAGES.includes(currentRoute)) {
    //     this.$router.push({
    //       name: "cards",
    //     });
    //   }
    // }
  },
  computed: {
    // ...mapState("userStore", ["token", "user"])
  }
};
</script>

<style scoped>

a, img {
  width: 28%;
  height: 18%;
  margin-left: 1%;
}

#header {
  background-color: #2e2831;
}

.button {
	background-color: rgba(71, 60, 79, 0.53);
	transition: all 0.3s ease 0s;
	color: #ded3ef;
	margin-left: 10px;
}

.router-link {
  text-decoration: none;
  color: inherit;
}

</style>