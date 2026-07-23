<script setup>
import Header from '../components/HeaderComponent.vue'
import { useTheme } from './theme'

const { theme, setTheme, lowPower, setLowPower } = useTheme()
</script>

<template>
    <Header></Header>
    <div class="flex flex-col items-center justify-center p-6 max-w-4xl mx-auto min-h-[calc(100vh-64px)]">
        <div class="glass-card w-full p-8 rounded-3xl shadow-xl flex flex-col items-center gap-8 border border-white/30 dark:border-slate-700/80">
            <div class="text-center space-y-1">
                <h1 class="text-3xl font-extrabold text-slate-900 dark:text-slate-100">⚙️ Configuración / Settings</h1>
                <p class="text-xs text-slate-600 dark:text-slate-300">Personaliza la apariencia, el tema visual y el rendimiento de la aplicación BeyStory.</p>
            </div>

            <!-- Tema Visual Section -->
            <div class="w-full max-w-xl space-y-4">
                <h2 class="text-base font-extrabold text-slate-900 dark:text-slate-100 border-b pb-2 border-slate-300 dark:border-slate-700/80">
                    🎨 Selección de Tema
                </h2>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <!-- Light Theme Option -->
                    <button 
                        @click="setTheme('light')" 
                        type="button" 
                        class="flex flex-col items-center justify-center p-6 rounded-2xl border-2 transition-all cursor-pointer gap-3 text-center"
                        :class="theme === 'light' ? 'border-amber-500 bg-amber-500/10 shadow-lg scale-105' : 'border-slate-300/40 hover:border-amber-400 bg-white/40'"
                    >
                        <span class="text-4xl">☀️</span>
                        <div>
                            <h3 class="font-bold text-base text-slate-900 dark:text-slate-100">Modo Claro</h3>
                            <p class="text-xs text-slate-600 dark:text-slate-300 mt-1">Fondo brillante porcelana con resplandores cálidos.</p>
                        </div>
                        <span v-if="theme === 'light'" class="text-xs font-semibold px-3 py-1 bg-amber-500 text-white rounded-full mt-1">Activo</span>
                    </button>

                    <!-- Dark Theme Option -->
                    <button 
                        @click="setTheme('dark')" 
                        type="button" 
                        class="flex flex-col items-center justify-center p-6 rounded-2xl border-2 transition-all cursor-pointer gap-3 text-center"
                        :class="theme === 'dark' ? 'border-amber-500 bg-amber-500/10 shadow-lg scale-105' : 'border-slate-300/40 hover:border-amber-400 bg-slate-900/40'"
                    >
                        <span class="text-4xl">🌙</span>
                        <div>
                            <h3 class="font-bold text-base text-slate-900 dark:text-slate-100">Modo Oscuro</h3>
                            <p class="text-xs text-slate-600 dark:text-slate-300 mt-1">Fondo neón nocturno con auroras y mallas de color.</p>
                        </div>
                        <span v-if="theme === 'dark'" class="text-xs font-semibold px-3 py-1 bg-amber-500 text-white rounded-full mt-1">Activo</span>
                    </button>
                </div>
            </div>

            <!-- Rendimiento y Bajo Consumo Section -->
            <div class="w-full max-w-xl space-y-4">
                <h2 class="text-base font-extrabold text-slate-900 dark:text-slate-100 border-b pb-2 border-slate-300 dark:border-slate-700/80">
                    ⚡ Rendimiento & Bajo Consumo
                </h2>

                <div 
                    class="p-6 rounded-2xl border-2 transition-all flex flex-col sm:flex-row items-center justify-between gap-6"
                    :class="lowPower ? 'border-emerald-500 bg-emerald-500/10 shadow-lg' : 'border-slate-300/40 dark:border-slate-700/60 bg-white/40 dark:bg-slate-900/40'"
                >
                    <div class="space-y-1 text-center sm:text-left">
                        <div class="flex items-center gap-2 justify-center sm:justify-start">
                            <span class="text-2xl">🌱</span>
                            <h3 class="font-extrabold text-base text-slate-900 dark:text-slate-100">Modo de Bajo Consumo</h3>
                            <span v-if="lowPower" class="px-2.5 py-0.5 bg-emerald-500 text-white text-[10px] font-extrabold rounded-full uppercase">Activado</span>
                        </div>
                        <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                            Desactiva los efectos de glassmorphism (difuminados de cristal), elimina animaciones continuas de fondo y utiliza colores planos para ahorrar batería y recursos de CPU/GPU.
                        </p>
                    </div>

                    <button 
                        @click="setLowPower(!lowPower)" 
                        type="button" 
                        class="px-5 py-2.5 rounded-xl text-xs font-extrabold shadow-md transition-all cursor-pointer flex-shrink-0"
                        :class="lowPower ? 'bg-emerald-500 hover:bg-emerald-600 text-white' : 'bg-slate-800 hover:bg-slate-700 text-white'"
                    >
                        {{ lowPower ? 'Desactivar Ahorro' : 'Activar Bajo Consumo' }}
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>

