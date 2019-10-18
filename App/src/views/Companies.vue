<template>
  <v-container class="container round transparent">
    <Navbar /> 
      <v-item-group v-model="selected" multiple> 
        <v-row>
          <v-col v-for="(company, i) in companies" :key="i" cols="12" md="4">
            <v-hover v-slot:default="{ hover }">
              <v-card  max="300" flat   :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }" >
                <v-item v-slot:default="{ active, toggle }">
                  <v-img  :src="company.image" height="14em" class="text-right pa-2" @click="toggle"  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)">
                    <v-btn icon  text color="red accent-4" @click="toggle" :input-value="active">
                      <v-icon active-class="red accent-4"  @click="toggle" :input-value="active">
                        {{ active ? 'mdi-heart' : 'mdi-heart-outline' }}
                      </v-icon>
                    </v-btn>
                    <v-card-title class="title white--text">
                      <v-row class="fill-height flex-column" justify="space-between">
                        <div class="description">
                          <span class="mt-4  subtitle-1  text-left">{{ company.name }},</span>
                          <span class="mt-4  subtitle-1  text-left"> {{ company.address }}</span>
                          <v-divider inset vertical class="mx-1"></v-divider>
                          <span>
                            <v-icon size=18 color="amber accent-4">mdi-star</v-icon> 
                            <v-icon size=18 color="amber accent-4">mdi-star</v-icon>
                            <v-icon size=18 color="amber accent-4">mdi-star</v-icon>
                            <v-icon size=18 color="amber accent-4">mdi-star</v-icon>
                            <v-icon size=18 color="amber accent-4">mdi-star</v-icon>
                          </span>
                      </div>
                    </v-row>
                  </v-card-title>
                </v-img>
              </v-item>
            <v-card-action>
              <v-menu transition="scale-transition" origin="center center">
                <template v-slot:activator="{ on }">
                  <v-btn block color="grey lighten-4"  v-on="on">
                    <span class="font-weight-bold">Contáctanos</span>
                  </v-btn>
                </template>
                <v-list class="grey lighten-4">
                  <v-list-item>
                    <v-row justify="center" align="center">
                      <div>
                        <v-list-item-title>
                          <v-icon color="teal">mdi-email</v-icon>
                          <span class="subtitle-2 font-weight-medium ">{{company.email}}</span>
                        </v-list-item-title>
                      </div>
                        <v-divider  vertical class="mx-2 ma-3"></v-divider>
                        <div>
                          <v-list-item-title>
                            <v-icon  color="teal">mdi-phone</v-icon>
                            <span class="subtitle-2 font-weight-medium ">{{company.phone}}</span>
                          </v-list-item-title>
                        </div>
                    </v-row>
                  </v-list-item>
                  </v-list>
                </v-menu>
              <div class="mx-4 hidden-sm-and-down"></div>
              </v-card-action>
            </v-card>
          </v-hover>
        </v-col>
      </v-row>
    </v-item-group>
  </v-container>
</template>

<script>
import axios from 'axios'
import Navbar from '@/components/Navbar'

export default {
  data: () => ({
        reservations: [ ] ,
        companies: [ ],
        show: false,
        selected: [],
        expand: false,
        expand2: false
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
</style>
