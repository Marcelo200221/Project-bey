import {createRouter, createWebHistory} from 'vue-router'
import Home from '@/Home.vue'
import BeyCreation from '@/AddBey.vue'
import VerBey from '@/VerBey.vue'
import Registrar from '@/Registrar.vue'
import Inicio from '@/Inicio.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'index',
            component: Home
        },
        {
            path: '/home',
            name: 'Home',
            component: Home
        },
        {
            path: '/create/:nombre',
            name: 'Create',
            component: BeyCreation
        },
        {
            path: '/ver/:id',
            name: 'Ver',
            component: VerBey
        },
        {
            path: '/registro',
            name: 'Registro',
            component: Registrar
        },
        {
            path: '/iniciar',
            name: 'Iniciar',
            component: Inicio
        }
    ]
})

export default router