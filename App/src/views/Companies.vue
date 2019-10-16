<template>
    <v-container class="my-1">
    <Navbar /> 
      <v-layout row wrap>
       <v-flex xs12 sm6 lg3 v-for="company in companies "> 
         <div class="my-5">
        <v-hover v-slot:default="{ hover }">
      <v-card @click="" class="mx-2" max="300" flat   :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }" >
        <v-img :src="company.image"  height="200px" class="white--text"  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)">
        </v-img>
       <div class="my-1">
         <span class="pa-4 my-4 font-weight-medium">{{ company.name }}</span>
       </div> 
       <div class="my-1">
         <span class="pa-4 my-4 caption">{{ company.address }}</span>
       </div> 
        <v-card-actions>
        <v-spacer></v-spacer>     
        </v-card-actions>
            <v-expansion-panels>
                  <v-expansion-panel  >
                     <v-expansion-panel-header class="teal--text font-weight-bold subtitle-1">Contacto</v-expansion-panel-header>
                      <v-expansion-panel-content>
                         <div><v-icon>mdi-email</v-icon>
                          {{ company.email }}</div>
                          <div><v-icon>mdi-phone</v-icon>
                          +502 {{ company.phone }}</div>
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
