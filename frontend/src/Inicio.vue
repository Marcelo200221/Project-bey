<script setup>
import Header from "../components/HeaderComponent.vue"
import BaseButton from "../components/BaseButton.vue";
import api from "./main";
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter()

const username = ref('')
const pass = ref('')

const login = async() => {
    try{
        console.log(username.value, pass.value)
        return await api.post('auth/login/', {
            username: username.value,
            password: pass.value
        }).then(response =>{
            const access = response.data.token.access;
            const user = response.data.user;

            if(access){
                localStorage.setItem("auth_token", access)
                localStorage.setItem("user", JSON.stringify(user))
                router.push('/home')
            }
        })

    }catch(error){
        console.error(error)
    }
}
</script>
<template>
    <Header></Header>
    <form>
        <div class="general">
            <h1>Iniciar sesion</h1>
            <div class="campos">
                <h3>Nombre de usuario</h3>
                <input type="text" v-model="username">
                <h3>Contraseña</h3>
                <input type="password" v-model="pass">
            </div>
        </div>
    </form>
    <BaseButton :color="'Cyan'" :hover-color="'Red'" @click="login()">Iniciar</BaseButton>
</template>