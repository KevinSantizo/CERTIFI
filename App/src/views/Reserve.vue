<template>
    <v-container class="my-5 round grey lighten-3">
        <Navbar /> 
        <v-layout row wrap>
            <v-flex xs12 sm6 lg3 v-for="company in companies "> 
                <div class="my-3">
                    <v-hover v-slot:default="{ hover }">
                    <v-card @click="" class="mx-2 " max="300" flat   :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }" >
                        <v-row justify="center" align="center">
                            <v-chip class="ma-2 font-weight-bold subtitle-1" draggable  color="cyan" label text-color="white" align="center" justify="center"><v-icon left>mdi-soccer</v-icon>{{ company.name }}</v-chip>
                        </v-row>
                        <v-row justify="center" align="center">
                            <span class="title">{{ company.address }}</span>
                    </v-row>
        <v-card-actions>
        <v-spacer></v-spacer>     
        </v-card-actions>
            <v-expansion-panels>
                  <v-expansion-panel  >
                     <v-expansion-panel-header class="teal--text font-weight-bold subtitle-1"><span>Ver horarios <v-icon left color="teal">mdi-calendar-clock</v-icon></span></v-expansion-panel-header>
                    <v-expansion-panel-content>
                        <v-slide-group class="pa-1" center-active show-arrows>
                            <v-slide-item v-for="n in 15" :key="n" v-slot:default="{ active, toggle }">
                                <v-chip class="ma-3"   color="light-green accent-3" @click="" label text-color="black" align="center" justify="center">12:00 PM</v-chip>
                            </v-slide-item>
                        </v-slide-group>
                    </v-expansion-panel-content>
                   </v-expansion-panel>
            </v-expansion-panels>
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

export default {
  data: () => ({
        reservations: [ ] ,
        companies: [ ],
        show: false
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
</style>
