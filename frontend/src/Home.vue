<script setup>
import { ref, onMounted, watch, computed } from 'vue';
import api from './main';
import BeyComponent from '../components/BeyComponent.vue';
import Header from '../components/HeaderComponent.vue';
import BaseButton from '../components/BaseButton.vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const seleccion = computed(() => route.params.season || null);
const mostrandoSelectorTemporada = ref(false);

const beyblades = ref([]);
const busqueda = ref('');
const cargandoBeys = ref(false);

const user = localStorage.getItem('user');
const token = localStorage.getItem('auth_token');

const cargarBeys = async (select) => {
    const params = {};
    if (select && select.value) {
        params.select = select.value;
    }
    try {
        cargandoBeys.value = true;
        const res = await api.get('cargar/beyblade', { params });
        beyblades.value = res.data || [];
    } catch (error) {
        console.error('Error al cargar Beyblades:', error);
    } finally {
        cargandoBeys.value = false;
    }
};

const buscar = async () => {
    if (!busqueda.value.trim()) {
        if (seleccion.value) {
            await cargarBeys({ value: seleccion.value });
        }
        return;
    }
    try {
        cargandoBeys.value = true;
        const res = await api.get('buscador', {
            params: { busqueda: busqueda.value }
        });
        beyblades.value = res.data || [];
    } catch (error) {
        console.error('Error en búsqueda:', error);
    } finally {
        cargandoBeys.value = false;
    }
};

const irATemporadas = () => {
    mostrandoSelectorTemporada.value = true;
    router.push({ name: 'Home', query: { seasons: 'true' } });
};

const volverABienvenida = () => {
    mostrandoSelectorTemporada.value = false;
    router.push({ name: 'Home' });
};

watch(
    [() => route.params.season, () => route.query.seasons],
    ([newSeason, newSeasonsQuery]) => {
        if (newSeason) {
            cargarBeys({ value: newSeason });
            mostrandoSelectorTemporada.value = false;
        } else if (newSeasonsQuery === 'true') {
            mostrandoSelectorTemporada.value = true;
            beyblades.value = [];
        } else {
            mostrandoSelectorTemporada.value = false;
            beyblades.value = [];
        }
    },
    { immediate: true }
);

onMounted(() => {
    if (route.params.season) {
        cargarBeys({ value: route.params.season });
    } else if (route.query.seasons === 'true') {
        mostrandoSelectorTemporada.value = true;
    }
});
</script>

<template>
    <Header></Header>

    <!-- Main Container for All Users (Guests & Logged In) -->
    <div class="min-h-[calc(100vh-64px)] p-6 max-w-7xl mx-auto flex flex-col items-center">
        
        <!-- 1. WELCOME HUB (Default Home State) -->
        <div v-if="!seleccion && !mostrandoSelectorTemporada" class="w-full space-y-10 py-6 max-w-5xl">
            
            <!-- Hero Welcome Card -->
            <div class="glass-card relative overflow-hidden p-8 sm:p-12 rounded-3xl text-center flex flex-col items-center justify-center gap-5 shadow-2xl border border-white/30 dark:border-slate-700">
                <!-- Background Accent Glows -->
                <div class="absolute -top-24 -left-24 w-72 h-72 bg-amber-500/20 rounded-full blur-3xl pointer-events-none"></div>
                <div class="absolute -bottom-24 -right-24 w-72 h-72 bg-orange-600/20 rounded-full blur-3xl pointer-events-none"></div>

                <div class="inline-flex items-center gap-2 px-4 py-1.5 bg-amber-500/15 border border-amber-500/40 text-amber-600 dark:text-amber-400 rounded-full text-xs font-bold uppercase tracking-wider shadow-sm">
                    <span>⚡ Portal Oficial BeyStory</span>
                </div>

                <h1 class="text-4xl sm:text-5xl font-black text-slate-900 dark:text-slate-100 tracking-tight leading-tight">
                    ¡Bienvenido a <span class="bg-gradient-to-r from-amber-500 via-orange-500 to-red-500 bg-clip-text text-transparent">BeyStory</span>!
                </h1>

                <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 max-w-2xl leading-relaxed">
                    El universo definitivo de Beyblade Metal Fight. Explora a los Bladers legendarios, consulta el catálogo interactivo de Beyblades por temporadas y conecta con la comunidad.
                </p>
            </div>

            <!-- Direct Navigation Cards Grid (Unified Visual Style) -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 w-full">
                
                <!-- Card 1: Personajes & Bladers -->
                <div class="glass-card flex flex-col justify-between p-6 rounded-3xl transition-all duration-300 hover:-translate-y-2 hover:border-amber-500 shadow-xl border border-white/30 dark:border-slate-700 group">
                    <div class="space-y-4">
                        <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-500/20 to-orange-500/20 border border-amber-500/40 flex items-center justify-center text-3xl shadow-inner group-hover:scale-110 transition-transform">
                            👤
                        </div>
                        <div>
                            <h2 class="text-2xl font-extrabold text-slate-900 dark:text-slate-100 group-hover:text-amber-500 transition-colors">
                                Bladers & Personajes
                            </h2>
                            <p class="text-xs text-slate-600 dark:text-slate-300 mt-2 leading-relaxed">
                                Explora las biografías, estadísticas de peso/altura y la evolución de los Beyblades asignados a cada Blader.
                            </p>
                        </div>
                    </div>

                    <div class="pt-6 mt-4 border-t border-slate-200 dark:border-slate-700/60">
                        <router-link 
                            to="/personajes"
                            class="w-full py-3 px-4 bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white rounded-xl text-xs font-extrabold shadow-md transition-all flex items-center justify-center gap-2 no-underline"
                        >
                            <span>Explorar Personajes</span>
                            <span>→</span>
                        </router-link>
                    </div>
                </div>

                <!-- Card 2: Beyblades & Catálogo por Temporada -->
                <div class="glass-card flex flex-col justify-between p-6 rounded-3xl transition-all duration-300 hover:-translate-y-2 hover:border-amber-500 shadow-xl border border-white/30 dark:border-slate-700 group">
                    <div class="space-y-4">
                        <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-orange-500/20 to-red-500/20 border border-orange-500/40 flex items-center justify-center text-3xl shadow-inner group-hover:scale-110 transition-transform">
                            🌀
                        </div>
                        <div>
                            <h2 class="text-2xl font-extrabold text-slate-900 dark:text-slate-100 group-hover:text-amber-500 transition-colors">
                                Beyblades por Temporada
                            </h2>
                            <p class="text-xs text-slate-600 dark:text-slate-300 mt-2 leading-relaxed">
                                Accede al catálogo completo dividido por sagas: Metal Fusion, Metal Masters, Metal Fury y sus piezas.
                            </p>
                        </div>
                    </div>

                    <div class="pt-6 mt-4 border-t border-slate-200 dark:border-slate-700/60">
                        <button 
                            type="button"
                            @click="irATemporadas"
                            class="w-full py-3 px-4 bg-gradient-to-r from-orange-500 to-red-500 hover:from-orange-600 hover:to-red-600 text-white rounded-xl text-xs font-extrabold shadow-md transition-all flex items-center justify-center gap-2 cursor-pointer"
                        >
                            <span>Seleccionar Temporada</span>
                            <span>→</span>
                        </button>
                    </div>
                </div>

                <!-- Card 3: Chats & Comunidad -->
                <div class="glass-card flex flex-col justify-between p-6 rounded-3xl transition-all duration-300 hover:-translate-y-2 hover:border-amber-500 shadow-xl border border-white/30 dark:border-slate-700 group md:col-span-2 lg:col-span-1">
                    <div class="space-y-4">
                        <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-red-500/20 to-amber-500/20 border border-red-500/40 flex items-center justify-center text-3xl shadow-inner group-hover:scale-110 transition-transform">
                            💬
                        </div>
                        <div>
                            <h2 class="text-2xl font-extrabold text-slate-900 dark:text-slate-100 group-hover:text-amber-500 transition-colors">
                                Chats & Comunidad
                            </h2>
                            <p class="text-xs text-slate-600 dark:text-slate-300 mt-2 leading-relaxed">
                                Entabla discusiones con otros fanáticos de Beyblade o consulta al asistente experto BeyBot.
                            </p>
                        </div>
                    </div>

                    <div class="pt-6 mt-4 border-t border-slate-200 dark:border-slate-700/60">
                        <router-link 
                            to="/chats"
                            class="w-full py-3 px-4 bg-gradient-to-r from-red-500 to-amber-500 hover:from-red-600 hover:to-amber-600 text-white rounded-xl text-xs font-extrabold shadow-md transition-all flex items-center justify-center gap-2 no-underline"
                        >
                            <span>Ir a los Chats</span>
                            <span>→</span>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>

        <!-- 2. SEASON SELECTOR (Sagas) -->
        <div v-else-if="mostrandoSelectorTemporada && !seleccion" class="w-full space-y-8 py-6 max-w-5xl">
            <!-- Header Section -->
            <div class="glass-card flex flex-col sm:flex-row items-center justify-between gap-4 p-6 sm:p-8 rounded-3xl shadow-xl border border-white/30 dark:border-slate-700">
                <div class="text-center sm:text-left space-y-1">
                    <h1 class="text-3xl font-extrabold text-slate-900 dark:text-slate-100">Catálogo por Temporada</h1>
                    <p class="text-xs text-slate-600 dark:text-slate-300">Selecciona una saga para explorar todos los Beyblades de esa generación.</p>
                </div>
                <button 
                    type="button" 
                    @click="volverABienvenida"
                    class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-xl text-xs font-bold transition-colors flex items-center gap-1.5 cursor-pointer shadow-md flex-shrink-0"
                >
                    <span>←</span> Volver al Hub
                </button>
            </div>

            <!-- Seasons Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 w-full">
                <!-- Metal Fusion -->
                <router-link 
                    :to="{ name: 'Home', params: { season: 'Fusion' } }"
                    class="glass-card group p-6 rounded-3xl flex flex-col justify-between items-center text-center gap-6 hover:border-amber-500 transition-all duration-300 hover:-translate-y-2 no-underline shadow-xl border border-white/30 dark:border-slate-700"
                >
                    <div class="w-20 h-20 rounded-2xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-4xl group-hover:scale-110 transition-transform shadow-inner">
                        🔥
                    </div>
                    <div class="space-y-2">
                        <h2 class="text-2xl font-black text-slate-900 dark:text-slate-100 group-hover:text-amber-500 transition-colors">Metal Fusion</h2>
                        <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                            La saga inicial. Explora los primeros Beyblades de la generación Metal Fight.
                        </p>
                    </div>
                    <span class="w-full py-2.5 bg-gradient-to-r from-amber-500 to-orange-500 text-white font-extrabold text-xs rounded-xl shadow-md group-hover:shadow-lg transition-all">
                        Ver Beyblades Fusion →
                    </span>
                </router-link>

                <!-- Metal Masters -->
                <router-link 
                    :to="{ name: 'Home', params: { season: 'Masters' } }"
                    class="glass-card group p-6 rounded-3xl flex flex-col justify-between items-center text-center gap-6 hover:border-orange-500 transition-all duration-300 hover:-translate-y-2 no-underline shadow-xl border border-white/30 dark:border-slate-700"
                >
                    <div class="w-20 h-20 rounded-2xl bg-orange-500/20 border border-orange-500/40 flex items-center justify-center text-4xl group-hover:scale-110 transition-transform shadow-inner">
                        ⚡
                    </div>
                    <div class="space-y-2">
                        <h2 class="text-2xl font-black text-slate-900 dark:text-slate-100 group-hover:text-orange-500 transition-colors">Metal Masters</h2>
                        <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                            Campeonato mundial Big Bang Bladers. Beyblades de máxima competición internacional.
                        </p>
                    </div>
                    <span class="w-full py-2.5 bg-gradient-to-r from-orange-500 to-red-500 text-white font-extrabold text-xs rounded-xl shadow-md group-hover:shadow-lg transition-all">
                        Ver Beyblades Masters →
                    </span>
                </router-link>

                <!-- Metal Fury -->
                <router-link 
                    :to="{ name: 'Home', params: { season: 'Fury' } }"
                    class="glass-card group p-6 rounded-3xl flex flex-col justify-between items-center text-center gap-6 hover:border-red-500 transition-all duration-300 hover:-translate-y-2 no-underline shadow-xl border border-white/30 dark:border-slate-700"
                >
                    <div class="w-20 h-20 rounded-2xl bg-red-500/20 border border-red-500/40 flex items-center justify-center text-4xl group-hover:scale-110 transition-transform shadow-inner">
                        🌟
                    </div>
                    <div class="space-y-2">
                        <h2 class="text-2xl font-black text-slate-900 dark:text-slate-100 group-hover:text-red-500 transition-colors">Metal Fury</h2>
                        <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                            Los Bladers Solar y el fragmento de estrella. El sistema 4D definitivo.
                        </p>
                    </div>
                    <span class="w-full py-2.5 bg-gradient-to-r from-red-500 to-amber-500 text-white font-extrabold text-xs rounded-xl shadow-md group-hover:shadow-lg transition-all">
                        Ver Beyblades Fury →
                    </span>
                </router-link>
            </div>

        </div>

        <!-- 3. BEYBLADES LISTING (Specific Season Selected) -->
        <div v-else class="w-full space-y-6">
            
            <!-- Controls Bar: Search + Back to Seasons -->
            <div class="glass-card flex flex-col md:flex-row items-center justify-between gap-4 p-4 sm:p-6 rounded-3xl shadow-xl border border-white/30 dark:border-slate-700">
                <!-- Title / Season Badge -->
                <div class="flex items-center gap-3">
                    <span class="text-3xl">🌀</span>
                    <div>
                        <h1 class="text-2xl font-extrabold text-slate-900 dark:text-slate-100 capitalize">
                            {{ seleccion ? `Temporada: Metal ${seleccion.replace('-', ' ')}` : 'Catálogo Beyblades' }}
                        </h1>
                        <p class="text-xs text-slate-600 dark:text-slate-300">Explora todos los modelos y especificaciones de esta temporada.</p>
                    </div>
                </div>

                <!-- Search Input & Navigation Buttons -->
                <div class="flex flex-col sm:flex-row items-center gap-3 w-full md:w-auto">
                    <div class="relative w-full sm:w-64">
                        <input 
                            type="text" 
                            v-model="busqueda"
                            @input="buscar"
                            placeholder="🔍 Buscar Beyblade..."
                            class="w-full px-4 py-2.5 bg-slate-900/80 border border-slate-700/80 rounded-2xl text-xs text-white placeholder-slate-400 focus:border-amber-500 focus:outline-none transition-colors shadow-inner"
                        >
                    </div>

                    <button 
                        type="button" 
                        @click="irATemporadas"
                        class="w-full sm:w-auto px-4 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-2xl text-xs font-bold transition-colors flex items-center justify-center gap-1.5 cursor-pointer shadow-md flex-shrink-0"
                    >
                        <span>🔄</span> Cambiar Temporada
                    </button>
                </div>
            </div>

            <!-- Loading State -->
            <div v-if="cargandoBeys" class="glass-card p-8 rounded-2xl text-center text-slate-600 dark:text-slate-300 max-w-md mx-auto my-8">
                <div class="text-3xl animate-spin mb-2">🌀</div>
                <p class="font-semibold text-sm">Cargando Beyblades...</p>
            </div>

            <!-- Beyblades Cards Grid -->
            <div v-else-if="beyblades.length > 0" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 p-2 justify-items-center">
                <div v-for="bey in beyblades" :key="bey.id" class="glass-card flex justify-center p-3 rounded-2xl transition-all duration-300 hover:-translate-y-1.5 hover:border-amber-500 overflow-hidden w-full max-w-xs shadow-lg">
                    <router-link class="no-underline text-slate-900 dark:text-slate-100 w-full" :to="{name: 'Ver', params:{id : bey.id}}" >
                        <BeyComponent
                            :photo="bey.photo"
                            :nombre="bey.nombre"
                            :color="bey.color"
                            :compact="true"
                        />
                    </router-link>
                </div>
            </div>

            <!-- Empty Beyblades State -->
            <div v-else class="glass-card p-8 rounded-3xl text-center max-w-md mx-auto my-8 space-y-3 shadow-xl">
                <span class="text-4xl">🌀</span>
                <h2 class="font-extrabold text-xl text-slate-900 dark:text-slate-100">No hay Beyblades en esta temporada</h2>
                <p class="text-xs text-slate-600 dark:text-slate-300">No se encontraron Beyblades registrados para {{ seleccion }}.</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>

