import VueRouter from "vue-router"
import EventsList from "@/components/EventsList";
import EventDetail from "@/components/EventDetail";
import TicketDetail from "@/components/TicketDetail";


export const router = new VueRouter({
    mode: "history",
    routes: [
        {
            path: "/",
            name: "",
            component: EventsList,
        },
        {
            path: '/detail-event/:eventID/',
            name: 'detail-event',
            component: EventDetail,
            props: true,

        },
        {
            path: '/detail-event/:EventID/tickets/',
            name: 'detail-ticket',
            component: TicketDetail,
            props: true,

        },
    ],
})
