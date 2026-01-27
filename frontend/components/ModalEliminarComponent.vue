<script setup>
import BaseButton from './BaseButton.vue';
const props = defineProps({
    texto: String,
    textoBoton: String,
    textoBoton2: String,
    color: String,
    hoverColor: String
})

const emit = defineEmits(['cancelar', 'eliminar'])

</script>

<template>
    <div class="modal-overlay">
        <div class="modal">
            <h1>{{ texto }}</h1>
            <BaseButton :color="color" :hover-color="hoverColor" @click="emit('eliminar')">{{ textoBoton }}</BaseButton>
            <BaseButton @click="emit('cancelar')">{{ textoBoton2 }}</BaseButton>
        </div>
    </div>
</template>

<style>
.modal-overlay{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;

    background: rgba(0,0,0,0.5);

    display: flex;
    align-items: center;
    justify-content: center;

    z-index: 9999;
}

.modal{
    background: white;
    padding: 20px;
    border-radius: 12px;
    min-width: 300px;
}
</style>