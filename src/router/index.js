import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '../components/Dashboard.vue';
import NotFound from '../components/NotFound.vue';

const routes = [
  { path: '/', component: Dashboard },
  { path: '/dashboard', component: Dashboard },
  { path: '/:catchAll(.*)', component: NotFound },  // Handle 404 routes
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
