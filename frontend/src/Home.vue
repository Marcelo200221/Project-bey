<script setup>
    import { ref } from 'vue';
    import api from './main';
    import BeyComponent from '../components/BeyComponent.vue';
    import Header from '../components/HeaderComponent.vue'
    import { RouterLink } from 'vue-router';

    const beyblades = ref([])

    const cargarBeys =  async() => {
        const res = await api.get("cargar/beyblade")
        beyblades.value = res.data
        console.log(beyblades.value)
    }

    cargarBeys()
</script>

<template>
    <Header></Header>
    
        <div v-for="bey in beyblades" :key="bey.id" class="flex justify-center max-w-[300px] mx-auto my-10 p-5 border-2 border-black rounded-[20%] transition duration-300 hover:scale-110"  type="button">
            <router-link class="no-underline text-black" :to="{name: 'Ver', params:{id : bey.id}}" >
                <BeyComponent
                    :nombre="bey.nombre"
                />
            </router-link>
            
        </div>

</template>

<style>

    .link{
        text-decoration: none;
        color: black;
    }
</style>