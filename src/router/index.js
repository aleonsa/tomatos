import { createRouter, createWebHashHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Config from '../views/Config.vue'
import firebase from 'firebase'

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/config',
    name: 'config',
    component: Config,
    meta: {
      requiresAuth: true
    }
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(rec => rec.meta.requiresAuth)) {
    const user = firebase.auth().currentUser;
    if (user) {
      next();
    } else {
      next({
        name: 'login'
      })
    }
  } else {
    next();
  }
})

export default router;
