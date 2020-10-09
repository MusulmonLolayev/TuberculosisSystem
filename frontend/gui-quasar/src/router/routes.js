
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'login', component: () => import('pages/Login.vue') },
      { path: 'new', component: () => import('pages/NewPatient.vue') },
      { path: 'patients', component: () => import('pages/PatientList.vue') },
      { path: 'detail', component: () => import('pages/Detail.vue') },
      { path: 'register', component: () => import('pages/Register.vue') },
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
