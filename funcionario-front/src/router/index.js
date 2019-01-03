import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Employee from '@/components/Employee'


Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/funcionario-list',
      name: 'Funcionários',
      component: Employee
    }
  ]
})

export default router