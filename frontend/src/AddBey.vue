<script setup>
    import api from './main';
    import { ref, watch } from 'vue';
    import Header from '../components/HeaderComponent.vue'
    import CreateComponent from '../components/CreateComponent.vue';
    import { useRoute } from 'vue-router';

    const route = useRoute();

    const eleccion = route.params.nombre;



    const creacion = ref("bey")

    const crearElemento = async(data)=>{
        switch(data.tipo){
            case 'bey':
                console.log(data)
                await api.post("crear/beyblade", data)
                break
            case 'fusion':
                await api.post("crear/fusion", data)
                break
            case 'clear':
                await api.post("crear/clear", data)
                break
            case 'track':
                await api.post("crear/track", data)
                break
            case 'tip':
                await api.post("crear/tip", data)
                break
            case 'tipe':
                await api.post("crear/tipe", data)
                break
        }
    }

</script>

<template>

    <Header></Header>

    <h1 class="titulo">Crear Beyblade</h1>

    <div class="form">
        <CreateComponent
            :eleccion="eleccion"
            @creation-info="crearElemento"
        ></CreateComponent>
    </div>

    
</template>

<style>

    .titulo{
        display: flex;
        justify-content: center;
    }

</style>