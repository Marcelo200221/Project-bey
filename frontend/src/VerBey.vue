<script setup>
    import Header from '../components/HeaderComponent.vue'
    import router from '../router';
    import { useRoute, useRouter } from 'vue-router';
    import api from './main';
    import { ref, resolveDirective, watch } from 'vue';
    import BeyComponent from '../components/BeyComponent.vue';
    import BaseButton from '../components/BaseButton.vue';
    import ModalEliminarComponent from '../components/ModalEliminarComponent.vue';
    import ModalDetalleComponent from '../components/ModalDetalleComponent.vue';


    const route = useRoute();
    const ruta = useRouter();
    const id = route.params.id

    const mostrarModal = ref(false)

    const mostrarModalF = ref(false)
    const mostrarModalC = ref(false)
    const mostrarModalT = ref(false)
    const mostrarModalTi = ref(false)
    const mostrarModalTipe = ref(false)

    const bey = ref({});

    const cargarBeyblade = async() => {
        try{
            const res = await api.get(`cargar/bey/${id}`)

            bey.value = res.data
            console.log(bey.value)
        } catch(error){
            console.error(error)
        }
    }

    const eliminarBey = async() => {
        try{
            await api.delete(`eliminar/bey/${id}`)

            console.log("Eliminación completa")
        } catch(error){
            console.error(error)
        }
    }

    const abrirModal = () => {
        mostrarModal.value = true
    }

    const cerrarModal = () => {
        mostrarModal.value = false
    }


    const abrirModalF = () => {
        mostrarModalF.value = true
    }

    const cerrarModalF = () => {
        mostrarModalF.value = false
    }

    const abrirModalC = () => {
        mostrarModalC.value = true
    }

    const cerrarModalC = () => {
        mostrarModalC.value = false
    }

    const abrirModalT = () => {
        mostrarModalT.value = true
    }

    const cerrarModalT = () => {
        mostrarModalT.value = false
    }

    const abrirModalTi = () => {
        mostrarModalTi.value = true
    }

    const cerrarModalTi = () => {
        mostrarModalTi.value = false
    }

    const abrirModalTipe = () => {
        mostrarModalTipe.value = true
    }

    const cerrarModalTipe = () => {
        mostrarModalTipe.value = false
    }
    

    cargarBeyblade()

</script>
<template>
    <Header></Header>
    <BeyComponent
        :nombre="bey.nombre"
        :descripcion="bey.descripcion"
    ></BeyComponent>

    <div class="contenedor-detalles">

        <div class="detalle" type="button" @click="abrirModalF">
            <h2>Fusion</h2>
        </div>

        <div class="detalle" type="button" @click="abrirModalC">
            <h2>Clear</h2>
        </div>

        <div class="detalle" type="button" @click="abrirModalT">
            <h2>Track</h2>
        </div>

        <div class="detalle" type="button" @click="abrirModalTi">
            <h2>Tip</h2>
        </div>

        <div class="detalle" type="button" @click="abrirModalTipe">
            <h2>Tipe</h2>
        </div>
    </div>

    <ModalDetalleComponent
        v-if="mostrarModalF"
        :titulo="bey.fusion"
        :detalle="bey.descripcion1"
        @cerrar="cerrarModalF()"
    ></ModalDetalleComponent>

    <ModalDetalleComponent
        v-if="mostrarModalC"
        :titulo="bey.clear"
        :detalle="bey.descripcion2"
        @cerrar="cerrarModalC()"
    ></ModalDetalleComponent>

    <ModalDetalleComponent
        v-if="mostrarModalT"
        :titulo="bey.track"
        :detalle="bey.descripcion3"
        @cerrar="cerrarModalT()"
    ></ModalDetalleComponent>

    <ModalDetalleComponent
        v-if="mostrarModalTi"
        :titulo="bey.tip"
        :detalle="bey.descripcion4"
        @cerrar="cerrarModalTi()"
    ></ModalDetalleComponent>

    <ModalDetalleComponent
        v-if="mostrarModalTipe"
        :titulo="bey.tipe"
        :detalle="bey.descripcion5"
        @cerrar="cerrarModalTipe()"
    ></ModalDetalleComponent>

    <div class="flex justify-center">
        <BaseButton  :color="'red'" :hover-color="'cyan'" @click="abrirModal()">Eliminar</BaseButton>
    </div>

    <ModalEliminarComponent
        v-if="mostrarModal"
        :texto="'¿Seguro de que quieres eliminar el Beyblade?'"
        :textoBoton="'Eliminar'"
        :textoBoton2="'Cancelar'"
        :color="'Red'"
        :hover-color="'Cyan'"
        @eliminar="eliminarBey()"
        @cancelar="cerrarModal()"
    ></ModalEliminarComponent>
</template>
<style>
.contenedor-detalles{
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap; /* para pantallas pequeñas */
    margin-top: 30px;
}
.detalle{
    display: flex;
    justify-content: center;
    align-content: flex-start;
    max-width: 300px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid black;
    border-radius: 30%;
    border-width: 2px;
    transition: all 0.3s ease;
}

.detalle:hover{
    transform: scale(1.1);
}
</style>