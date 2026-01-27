
<script setup></script>
<template>
    <header class="header">
        <div>
            <div class="title">
                <router-link class="link" :to="{name: 'Home'}">BeyStory</router-link>
            </div>
        </div>
        <nav class="opciones">
            
            <router-link class="link" :to="{name: 'Create', params: {nombre: 'bey'}}">Crear Beyblade</router-link>
            <router-link class="link" :to="{name: 'Create', params: {nombre: 'fusion'}}">Crear Fusion Wheel</router-link>
            <router-link class="link" :to="{name: 'Create', params: {nombre: 'clear'}}">Crear Clear Wheel</router-link>
            <router-link class="link" :to="{name: 'Create', params: {nombre: 'track'}}">Crear Spin track</router-link>
            <router-link class="link" :to="{name: 'Create', params: {nombre: 'tip'}}">Crear Tip</router-link>
            <router-link class="link" :to="{name: 'Create', params: {nombre: 'tipe'}}">Crear Tipe</router-link>
            <a href="crear" type="button">Ir a chats</a>
            <a href="crear" type="button">Ventas</a>
        </nav>
    </header>
</template>

<style>
    html body{
        margin: 0;
        padding: 0;
    }
    .header{
        display: flex;
        background: cyan;
        padding: 1%;
        align-items: center;
        justify-content: space-between;
        height: 70px;
        padding: 0 20px;

    }
    .title .link{
        display: inline-block;
        color: black;
        font: bolder;
        font-size: 28px;
        border-radius: 5px;
        background: brown;
        text-decoration: none;
        transition: all 0.3s ease;
    }

    .title .link:hover{
        transform: scale(1.1);
    }

    .opciones{
        display: flex;
        justify-content: right;
        align-items: center;
    }

    .opciones a{
        text-decoration: none;
        margin: 5px;
        margin-right: 20px;
        color: black;
        font-size: large;
    }

</style>

