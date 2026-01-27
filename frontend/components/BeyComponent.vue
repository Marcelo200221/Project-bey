<script setup>
    const prop = defineProps({
        nombre: {String},
        descripcion: String,
        fusion: String,
        descripcion1: String,
        clear: String,
        descripcion2: String,
        track: String,
        descripcion3: String,
        tip: String,
        descripcion4: String,
        tipe: String,
        descripcion5: String
    })
</script>

<template>
    <div class="campos">
        <div class="flex items-center justify-center font-sans border-2 border-black p-6">
            <img src="../img/image.png" alt="" class="w-24 h-auto mr-6">
            <div class="max-w-md text-center">
                
                <h3 class="text-3xl font-bold mb-4">{{prop.nombre}}</h3>
                <h4 class="text-base">{{ prop.descripcion }}</h4>
            </div>
        </div>
        <div class="fusion">
            <h3>{{prop.fusion}}</h3>
            <h4>{{ prop.descripcion1 }}</h4>
        </div>
        <div class="clear">
            <h3>{{prop.clear}}</h3>
            <h4>{{ prop.descripcion2 }}</h4>
        </div>
        <div class="track">
            <h3>{{prop.track}}</h3>
            <h4>{{ prop.descripcion3 }}</h4>
        </div>
        <div class="tip">
            <h3>{{prop.tip}}</h3>
            <h4>{{ prop.descripcion4 }}</h4>
        </div>
        <div class="tipe">
            <h3>{{prop.tipe}}</h3>
            <h4>{{ prop.descripcion5 }}</h4>
        </div>
    </div>
</template>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    .campos .principal h3{
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
    }

    .campos .principal h4{
        font-family: sans-serif;
        font-size: medium;
    }

    .fusion h3{
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        text-decoration: underline;
    }

    .fusion h4{
        font-family: sans-serif;
        font-size: medium;
    }

    .clear h3{
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        text-decoration: underline;
    }

    .clear h4{
        font-family: sans-serif;
        font-size: medium;
    }

    .track h3{
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        text-decoration: underline;
    }

    .track h4{
        font-family: sans-serif;
        font-size: medium;
    }

    .tip h3{
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        text-decoration: underline;
    }

    .tip h4{
        font-family: sans-serif;
        font-size: medium;
    }

    .tipe h3{
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        text-decoration: underline;
    }

    .tipe h4{
        font-family: sans-serif;
        font-size: medium;
    }
</style>