<script setup>
    import { ref } from 'vue'
    import api from '@/main'
    import BaseButton from './BaseButton.vue'
    const nombre = ref("")
    const descripcion = ref("")
    const fusion_wheel = ref([])
    const clear_wheel = ref([])
    const track = ref([])
    const tip = ref([])
    const tipe = ref([])

    const nombres = ref("")
    const descripciones = ref("")
    const fusionWheels = ref([])
    const clearWheels = ref([])
    const tracks = ref([])
    const tips = ref([])
    const tipes = ref([])
    const props=defineProps({
        eleccion: String,
    })

    const cargarOpciones = async() => {
        try{
            const fus = await api.get("cargar/fusion")
            const cle = await api.get("cargar/clear")
            const tra = await api.get("cargar/track")
            const pun = await api.get("cargar/tip")
            const tipo = await api.get("cargar/tipe")

            fusionWheels.value = fus.data
            clearWheels.value = cle.data
            tracks.value = tra.data
            tips.value = pun.data
            tipes.value = tipo.data

            console.log(fusion_wheel.value)
        } catch(error){
            console.error(error)
        }
    }

    const emit = defineEmits(['creation-info'])

    const emitirCreacion = async()=>{
        let payload = {}

        switch (props.eleccion) {
            case 'fusion':
            case 'clear':
            case 'track':
            case 'tip':
            case 'tipe':
                payload = {
                    tipo: props.eleccion,
                    nombre: nombre.value,
                    descripcion: descripcion.value
                }
                break
            
            case 'bey':
                payload = {
                    tipo: 'bey',
                    nombre: nombre.value,
                    descripcion: descripcion.value,
                    fusion: fusion_wheel.value,
                    clear: clear_wheel.value,
                    track: track.value,
                    tip: tip.value,
                    tipe: tipe.value
                }
                break
        }
        emit('creation-info', payload)
    }

    cargarOpciones()
</script>
<template>
    <form action="post">
        <div class="campos">
            <div class="camposFusion" v-if="eleccion === 'fusion'">
                <h3>Nombre</h3>
                <input type="text" v-model="nombre">
                <h3>Descripción</h3>
                <textarea v-model="descripcion" rows="4" cols="100"></textarea>
            </div>
            <div class="camposClear" v-if="eleccion === 'clear'">
                <h3>Nombre</h3>
                <input type="text" v-model="nombre">
                <h3>Descripción</h3>
                <textarea v-model="descripcion" rows="4" cols="100"></textarea>
            </div>
            <div class="camposTrack" v-if="eleccion === 'track'">
                <h3>Nombre</h3>
                <input type="text" v-model="nombre">
                <h3>Descripción</h3>
                <textarea v-model="descripcion" rows="4" cols="100"></textarea>
            </div>
            <div class="camposTip" v-if="eleccion === 'tip'">
                <h3>Nombre</h3>
                <input type="text" v-model="nombre">
                <h3>Descripción</h3>
                <textarea v-model="descripcion" rows="4" cols="100"></textarea>
            </div>
            <div class="camposTipe" v-if="eleccion === 'tipe'">
                <h3>Nombre</h3>
                <input type="text" v-model="nombre">
                <h3>Descripción</h3>
                <textarea v-model="descripcion" rows="4" cols="100"></textarea>
            </div>
            <div class="camposBey" v-if="eleccion === 'bey'">
                <h3>Nombre</h3>
                <input type="text" v-model="nombre">
                <h3>Descripción</h3>
                <textarea v-model="descripcion" rows="4" cols="100"></textarea>
                <h3>Fusion Wheel</h3>
                <select v-model="fusion_wheel">
                    <option disabled value="">Seleccionar Rueda de fusion</option>
                    <option 
                        v-for="f in fusionWheels"
                        :key="f.id"
                        :value="f.id">
                    {{ f.nombre }}
                    </option>
                </select>
                <h3>Clear Wheel</h3>
                <select  v-model="clear_wheel">
                    <option disabled value="">Seleccionar Aro de energía</option>
                    <option
                        v-for="c in clearWheels" 
                        :key="c.id"
                        :value="c.id">
                        {{ c.nombre }}
                    </option>
                </select>
                <h3>Spin Track</h3>
                <select  v-model="track">
                    <option disabled value="">Seleccionar Eje de rotación</option>
                    <option
                        v-for="t in tracks" 
                        :key="t.id"
                        :value="t.id">
                        {{ t.nombre }}
                    </option>
                </select>
                <h3>Tip</h3>
                <select v-model="tip">
                    <option disabled value="">Seleccionar Punta de rendimiento</option>
                    <option
                        v-for="t in tips"
                        :key="t.id" 
                        :value="t.id">
                        {{ t.nombre }}
                    </option>
                </select>                                                      
                <h3>Tipe</h3>
                <select  v-model="tipe">
                    <option disabled value="">Seleccionar Tipo</option>
                    <option 
                        v-for="t in tipes"
                        :key="t.id"
                        :value="t.id">
                        {{ t.nombre }}
                    </option>
                </select>
            </div>
            <BaseButton :color="'Cyan'" @click="emitirCreacion()">Crear</BaseButton>
        </div>
    </form>

</template>
<style>
    .campos{
        display: flex;
        flex-direction: column;
        margin: 10px;
    }
    .campos.camposFusion{
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin: 10px;
        max-width: 500px;
        align-items: stretch;
        
    }

    .campos.camposFusion input{
        height: 30px;
    }

    .campos h3{
        margin: 0;
    }

    .form{
        display: flex;
        justify-content: center;
        align-items: flex-start;

    }

    .form form{
        width: 100%;
        max-width: 500px;
    }

    .crear{
        display: block;
        margin: 20px auto;
    }
</style>