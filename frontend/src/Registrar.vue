<script setup>
import api from './main';
import BaseButton from '../components/BaseButton.vue';
import Header from '../components/HeaderComponent.vue';
import { ref } from 'vue';

const nombre = ref('')
const apellido = ref('')
const correo = ref('')
const nombreUsuario = ref('')
const pass1 = ref('')
const pass2 = ref('')

const registrar = async() => {
    try{
        if(pass1.value == pass2.value){
            await api.post('/registration', {
                first_name: nombre.value,
                last_name: apellido.value,
                email: correo.value,
                username: nombreUsuario.value,
                password1: pass1.value,
                password2: pass2.value
            })
            console.log("Registro exitoso")
        }
        
    } catch(error){
        console.error(error)
    }
}
</script>
<template>
    <Header></Header>
    <form>
        <div class="general">
            <h1>Registro de usuario</h1>
            <div class="campos">
                <h3>Nombre</h3>
                <input type="text" v-model="nombre">
                <h3>Apellido</h3>
                <input type="text" v-model="apellido">
                <h3>Correo</h3>
                <input type="text" v-model="correo">
                <h3>Nombre de usuario</h3>
                <input type="text" v-model="nombreUsuario">
                <h3>Contraseña</h3>
                <input type="text" v-model="pass1">
                <h3>Confirmar Contraseña</h3>
                <input type="text" v-model="pass2">
            </div>
        </div>
    </form>
    <BaseButton :color="'Cyan'" @accion="registrar">Rergistrar</BaseButton>
</template>