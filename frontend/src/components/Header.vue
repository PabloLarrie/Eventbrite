-<template>
  <div id="header">
    <b-navbar toggleable="lg">
      <a href="/"><img src="@/assets/logo.png" alt=""></a>
      <b-navbar-brand class="logo" to="/">ventbrite</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="position-absolute end-50">
          <b-button pill class="button pt-2 pb-2 pe-4 ps-4">
            <router-link class="router-link " to="#" >Events</router-link>
          </b-button>
          <b-button pill class="button pt-2 pb-2 pe-4 ps-4">
            <router-link class="router-link" to="#">Things</router-link>
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

img {
  width: 32px;
  height: 32px;
}

#header {
  background-color: #2e2831;
}

.logo {
	color: #ded3ef;
  font-size: 28px;
}

.logo:hover {
	color: #984134;
}


.button {
  /*padding: 10px 40px;*/
	background-color: rgba(71, 60, 79, 0.53);
	/*border: none;*/
	/*cursor: pointer;*/
	transition: all 0.3s ease 0s;
	/*border: 1px solid #6c1aef;*/
	/*font-size: 15px;*/
	color: #ded3ef;
	/*padding: 0.4rem 2.5;*/
	/*font-weight: 700;*/
	margin-left: 10px;
}

.router-link {
  text-decoration: none;
  color: inherit;
}

</style>