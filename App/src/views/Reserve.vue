<template>
  <v-container class="container">
    <v-card class="overflow-hidden" >
        <v-app-bar  flat text app class="grey lighten-4"  height="57">
          <v-layout row wrap>
            <v-flex xs12 md12>
              <v-row justify="center" align="center">
                <v-icon color="black" size="15" >mdi-map-marker</v-icon><span class="font-weight-bold subtitle-1">Quetzaltenango, quetzaltenango</span>
              </v-row>
              <v-row justify="center" align="center">
                <v-icon color="black" size="15">mdi-calendar</v-icon><span class="font-weight-bold caption" >{{ this.days[new Date().getDay() ]}},{{ new Date().getDate()}} de {{  this.months[new Date().getMonth()] }} {{ new Date().getFullYear() }}</span>
              </v-row>
            </v-flex>
          </v-layout>
        </v-app-bar>
      <template>
        <v-bottom-navigation :value="activeBtn" scroll-target="#scroll-area-2" hide-on-scroll  color="teal" absolute>
          <v-btn class="link" router to="/home">
            <span class="caption font-weight-medium">Inicio</span>
            <v-icon>mdi-home</v-icon>
          </v-btn>
          <v-btn>
            <span  class="caption font-weight-medium">Favoritas</span>
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <v-btn>
            <span  class="caption font-weight-medium">Configuración</span>
            <v-icon>mdi-settings</v-icon>
          </v-btn>
        </v-bottom-navigation>
      </template>
      <v-sheet id="scroll-area-1" class="overflow-y-auto" max-height="600" >
        <v-container class="bottom" >
          <v-layout row wrap>
            <v-flex xs12 sm6 lg3 v-for="company in companies "> 
              <div class="ma-2 my-1 ">
                <v-hover v-slot:default="{ hover }">
                  <v-card :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }">
                    <v-img :src="company.image" height="150px">
                      <v-row justify="left" align="center" class="ma-3 my-15">
                          <v-icon @click="color = !color" color="black" size="30" >mdi-heart-outline
                          </v-icon>
                      </v-row>
                    </v-img>
                    <v-footer class="white ma-1"  padless>
                      <v-row justify="left" no-gutters>
                        <div>
                          <span class="subtitle-2 ma-2">{{ company.name }} {{ company.address}}</span>
                        </div> 
                        <v-col class="text-left  caption black--text" cols="12">
                          <div class="description">
                            <span>
                              <v-icon size=15 color="amber accent-4">mdi-star</v-icon> 
                              <v-icon size=15 color="amber accent-4">mdi-star</v-icon>
                              <v-icon size=15 color="amber accent-4">mdi-star</v-icon>
                              <v-icon size=15 color="amber accent-4">mdi-star</v-icon>
                              <v-icon size=15 color="amber accent-4">mdi-star</v-icon>
                            </span><br>
                            <span >
                              <v-icon color="black" size="15" class="caption">mdi-map-marker</v-icon>4ta. C 11-a, zona 1, quetzaltenango
                            </span>
                          </div>
                        </v-col>
                      </v-row>
                    </v-footer>
                    <v-card-actions>
                      <div class="reserve">
                        <v-row justify="left" align="left" class="ma-1 my-1">
                          <div>
                            <span class="ma-1 font-weight-bold  green--text" color="teal darken-4">Canchas: 5</span><br>
                            <div class="span">
                              <span class="ma-1 caption">hola</span>
                            </div> 
                          </div>
                          <v-row justify="end" align="center" class="ma-1"> 
                            <v-btn text small router to="/do_reserve" class="link font-weight-bold">Reservar<v-icon right size=15>mdi-chevron-right</v-icon>
                            </v-btn>
                          </v-row>
                        </v-row>
                      </div>
                    </v-card-actions>
                  </v-card>
                </v-hover>
              </div>
            </v-flex>
          </v-layout>
        </v-container>
      </v-sheet>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
        reservations: [ ] ,
        companies: [ ],
        show: false,
        months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        days: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado',],
        activeBtn: 1,
        showNav: true,
        color: false
    }),
    methods: {
      getCompanies() {
      const path = 'http://127.0.0.1:8000/sport/companies/'
      axios.get(path).then((response)=> {
        this.companies = response.data
        console.log(response.data);
      })
      },
    },
    created(){
      this.getCompanies()
    },
    /*created(){
      this.getDate()
    }*/
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
   .reserve {
     border: solid 0.5px grey;
     width: 100%;
     border-radius: 5px;
     margin-top: 1.2em; 
   }
   .calendar {
     position: absolute;
     margin-top: 10.1em;
   }
   .span {
     position: relative;
     margin-top: -0.5em;
   }
   .description {
     position: absolute;
     margin-top: -0.8em;
     margin-left: 1em;
   }
   .back {
     position: absolute;
     margin-top: -1.5em;
     margin-left: -0.2em;
   }
   .link {
     text-decoration: none;
   }
   .heart {
     position: absolute;
     margin-left: 13.7em;
     margin-top:  0.2em;
   }
   .bottom {
     margin-bottom:  50px;
   }
   .container {
    max-width: 100%;
}
</style>