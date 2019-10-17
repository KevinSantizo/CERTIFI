<template>
    <v-container class="my-4">
      <div class="back">
        <v-btn text icon color="grey darken-4" router to="/home" class="link"> 
          <v-icon size="35">mdi-chevron-left</v-icon>
        </v-btn>
      </div> 
        <v-layout row wrap>
            <v-flex xs12 sm6 lg3 v-for="company in companies "> 
                <div class="ma-3 ">
                  <v-hover v-slot:default="{ hover }">
                      <v-card :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }">
                        <v-img :src="company.image" height="150px">
                        </v-img>
                        <v-footer class="white ma-1"  padless>
                          <v-row justify="left" no-gutters>
                         <div><span class="subtitle-2 ma-2">{{ company.name }} {{ company.address}}</span></div> 
                            <v-col class="text-left  caption black--text" cols="12">
                                <div class="description">
                                <span>
                                  <v-icon size=15 color="amber accent-4">mdi-star-outline</v-icon> 
                                  <v-icon size=15 color="amber accent-4">mdi-star-outline</v-icon>
                                  <v-icon size=15 color="amber accent-4">mdi-star-outline</v-icon>
                                  <v-icon size=15 color="amber accent-4">mdi-star-outline</v-icon>
                                  <v-icon size=15 color="amber accent-4">mdi-star-outline</v-icon>
                                </span>
                                <br>
                                <span ><v-icon color="black" size="15" class="caption">mdi-map-marker</v-icon>4ta. C 11-a, zona 1, quetzaltenango</span>
                                </div>
                              </v-col>
                              </v-row>

                        </v-footer>
                        <v-card-actions>
                          <div class="reserve">
                            <v-row justify="left" align="left" class="ma-1 my-1"> 
                              <div> <span class="ma-1 font-weight-bold  green--text" color="teal darken-4">Canchas: 5</span><br>
                              <div class="span"><span class="ma-1 caption">hola</span></div> 
                              </div>
                              <v-row justify="end" align="center" class="ma-1"> 
                                <v-btn text small class=" font-weight-bold">Reservar<v-icon right size=15>mdi-chevron-right</v-icon></v-btn>
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
</template>

<script>
import axios from 'axios'
import Navbar from '@/components/Navbar'
import Multiselect from 'vue-multiselect'

export default {
  components: {
    Multiselect
  },
  data: () => ({
        reservations: [ ] ,
        companies: [ ],
        show: false,
      tags: [
        '1:00 PM',
        '2:00 PM',
        '3:00 PM',
        '4:00 PM',
        '5:00 PM',
        '6:00 PM',
        '7:00 PM',
        '8:00 PM',
        '9:00 PM',
      ],
    }),
     components: {
    Navbar
  },
    methods: {
      getCompanies() {
      const path = 'http://127.0.0.1:8000/sport/companies/'
      axios.get(path).then((response)=> {
        this.companies = response.data
        console.log(response.data);
        
      })
      }
    },
    created(){
      this.getCompanies()
    }
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
     margin-left: 0.5em;
   }
   .back {
     position: absolute;
     margin-top: -1.5em;
     margin-left: 0.1em;
   }
   .link {
     text-decoration: none;
   }
</style>
