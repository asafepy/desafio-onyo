import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Employee from '@/components/Employee'
import EmployeeCreate from '@/components/EmployeeCreate'


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
      name: 'Employee',
      component: Employee
    },
    {
      path: '/funcionario-create',
      name: 'EmployeeCreate',
      component: EmployeeCreate
    }
  ]
})

export default router