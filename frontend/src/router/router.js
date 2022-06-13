import VueRouter from "vue-router"
// import Home from "../components/Home";
import EventsList from "@/components/EventsList";


export const router = new VueRouter({
    mode: "history",
    routes: [
        {
            path: "/",
            name: "",
            component: EventsList,
        },
    ],
})
