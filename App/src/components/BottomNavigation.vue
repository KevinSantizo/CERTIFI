<template>
  <v-bottom-navigation scroll-target="#scroll-area-2" hide-on-scroll   color="teal" absolute>
    <v-btn class="link" router to="/home">
      <span class="caption font-weight-medium">Inicio</span>
      <v-icon >mdi-home</v-icon>
    </v-btn>
    <v-btn class="link" router to="/companies">
      <span class="caption font-weight-medium">Compañías</span>
      <v-icon >mdi-domain</v-icon>
    </v-btn>
     <v-btn class="link" router to="/reserve">
      <span  class="caption font-weight-medium">Reservar</span>
      <v-icon >mdi-calendar</v-icon>
    </v-btn>
    <v-btn class="link" router to="/account">
      <span class="caption font-weight-medium">Mi Perfil</span>
      <v-icon >mdi-account</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
export default {
    data:() => ({
        show: false,
        selected: [],
        expand: false,
        expand2: false,
        show: false,
        months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        days: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado',],
        activeBtn: 1,
        showNav: true,
        color: false
    })
}
</script>

<style scoped>
  .v-card {
    transition: opacity .4s ease-in-out;
  }
  .v-card:not(.on-hover) {
    opacity: 0.9;
  }
  .show-btns {
    color: rgba(255, 255, 255, 1) !important;
  }
  .round{
        border-radius: 10px;
   }
   .container {
     position: absolute;
     max-width: 100%;
   }
   .description {
     position: absolute;
     margin-top: 6.5em;
     margin-left: 0.2em;
   }
   .item-icon {
     position: absolute;
     left: 0.5em;
     bottom: 0.5em;
   }
   .icon {
     position: absolute;
     left: 2.5em;
     bottom: 1.4em;
   }
    .item-icon2 {
     position: absolute;
     left: -0.5em;
     top: 0.5em;
   }
   .icon2 {
     position: absolute;
     left: 2.5em;
     bottom: -0.3em;
   }
   .bottom {
     margin-bottom:  50px;
   }
   .link {
     text-decoration: none;
   }
</style>