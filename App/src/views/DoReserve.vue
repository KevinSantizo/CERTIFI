<template>
  <v-container class="container">
    <v-card class="transparent">
        <v-app-bar  flat text app class="grey lighten-4"  height="57">
          <v-app-bar-icon></v-app-bar-icon>
          <v-layout row wrap>
            <v-flex xs12 md12>
              <v-row justify="left" align="top">
                <div style="position: absolute; left: 0.2em; top: 0.5em;">
                <v-btn icon  class="link" >
                <v-icon color="black" size="30 " >mdi-chevron-left</v-icon>
                </v-btn>
              </div>
              </v-row>
              <v-row justify="center" align="center">
                <v-icon color="black" size="15">mdi-calendar</v-icon><span class="font-weight-bold caption" >{{ this.days[new Date().getDay() ]}},{{ new Date().getDate()}} de {{  this.months[new Date().getMonth()] }} {{ new Date().getFullYear() }}</span>
              </v-row>
            </v-flex>
          </v-layout>
        </v-app-bar>
        <v-container class="bottom" >
        <v-divider inset vertical> </v-divider>
      <div style="top: 1em;">
      <v-slide-group
        v-model="model"
        class="" style="top: -2em;">
        <v-slide-item v-for="image in images" :key="image" v-slot:default="{ active, toggle }">
          <v-card :color="active ? 'primary' : 'grey lighten-1'" class="ma-4" height="100" width="200" @click="toggle">
             
                <v-img :src="image.src" height="100" width="200">
              </v-img>
              
          </v-card>
        </v-slide-item>
        
      </v-slide-group>
  </div>
            <v-layout row wrap>
            <v-flex xs12 sm6 lg3 > 
              <div class="ma-4 my-1 ">
                <v-hover v-slot:default="{ hover }">
                  <v-card >
                    <v-img src="http://www.tvavila.icrt.cu/wp-content/uploads/2019/03/futbol.jpg" height="150px">
                     
                    </v-img>
                    <v-footer class="white ma-1"  padless>
                      <v-row justify="left" no-gutters>
                        <div>
                          <span class="subtitle-2 ma-2">Futeca Xela</span>
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
                    <v-divider inset vertical> </v-divider>
                    <div class="action">
                    <v-card-actions v-for="field in fields" class="actions">
                      <div class="reserve" >
                        <v-row justify="left" align="left" class="ma-3 my-1">
                          <div>
                            <span class="ma-1 font-weight-bold  green--text" color="teal darken-4">{{ field.name}}</span><br>
                            <div class="span">
                              <span class="ma-1 caption">{{ field.price }}</span>
                            </div> 
                          </div>
                          <v-row justify="end" align="center" class="ma-1"> 
                            <v-btn text small class="link font-weight-bold">Reservar<v-icon right size=15>mdi-chevron-right</v-icon>
                            </v-btn>
                          </v-row>
                        </v-row>
                      </div>
                    </v-card-actions>
                    </div>
                  </v-card>
                </v-hover>
              </div>
            </v-flex>
          </v-layout>
        </v-container>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios'
import BottomNavigation from '@/components/BottomNavigation'
export default {
  data: () => ({
        reservations: [ ] ,
        companies: [ ],
        show: false,
        months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        days: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado',],
        activeBtn: 1,
        showNav: true,
        color: false,
        images: [
          { src: "https://bogota.gov.co/sites/default/files/styles/despliegue_1366x768_px/public/field/image/Nueva%20cancha%20sint%C3%A9tica%20en%20el%20Parque%20Las%20Cruces%20beneficiar%C3%A1%20comunidad%20de%20tres%20localidades%20P.jpg"},
          { src: "https://cdn.futbolperuano.com/sdi/2018/07/23/donde-alquilar-un-cancha-sintetica-en-lima-norte-para-las-pichangas-658476.jpg"},
          { src: "https://lh3.googleusercontent.com/6ygjCkkb-sYeWWJLh964wzsu-rnQcpquw2I9ebvQ4xzKCxoFnE0tWpuPXN7yV85rCdgEWqJq=w1080-h608-p-no-v0"},
          { src: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1vYclJ6emIr9MCaXt8cH754_vIRt-ouh_I6IuIj58t_SPrjxd&s"},
          { src: "https://www.parqueygrama.com/wp-content/uploads/2017/03/grama-sintetica-para-canchas-de-futbol-2.png"},
          { src: "https://www.pqs.pe/sites/default/files/styles/852x479/public/archivos/2015/actualidad/01/sabugattas/pastosintetico-lacanchita-futbol7-3.jpg?itok=awaMBCao"},
          { src: "http://www.tucaqueta.com/wp-content/uploads/2017/01/Cancha.jpg"},
          { src: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQEgGMX5i7iqw9ALETWvwt1shQtrmQp7LBnCqqY3DNLgKAMV7-sA&s"},
          { src: "https://files.alerta.rcnradio.com/alerta_tolima_prod/public/styles/article_desktop/public/migration/canchas14deoctubre.png?itok=thGx-QGr"},
          { src: "https://www.eluniversal.com.co/sites/default/files/201706/cancha_2.jpg"},
          { src: "http://www.eje21.com.co/site/wp-content/uploads/2016/04/Cancha-sintetica-de-la-terminal-de-manizales.jpg"},
          { src: "https://files.rcnradio.com/public/styles/img_galeria/public/2019-02/whatsapp_image_2019-02-11_at_4.22.50_pm_1_0.jpeg?itok=pjSrd8tA"}
        ]
    }),
     components: {
    BottomNavigation
  },
    methods: {
       getFields() {
      const path = 'http://127.0.0.1:8000/sport/fields/'
      axios.get(path).then((response)=> {
        this.fields = response.data
        console.log(response.data);
      })
      },

    },
    created(){
      this.getFields()
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
     margin-top: -0.6em; 
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
    max-height: 100%;
  }
  .actions {
  bottom: 3em; 
  }
</style>