<template>
    <v-container>
        <Navbar /> 
        <v-layout row wrap>
            <v-flex xs12 sm6 lg3 v-for="company in companies "> 
                <div class="my-3">
                    <v-hover v-slot:default="{ hover }">
                    <v-card class="mx-2 " max="300" flat   :elevation="hover ? 12 : 5" :class="{ 'on-hover': hover }" >
                        <div class="green accent-1">
                        <v-row justify="center" align="center">
                            <v-chip class="ma-2 font-weight-medium subtitle-2" color="teal darken-4" label text-color="white" align="center" justify="center"><v-icon left>mdi-soccer</v-icon>{{ company.name }}</v-chip>
                        </v-row>
                        <v-row justify="center" align="center">
                            <span class="title">{{ company.address }}</span>
                    </v-row>
                    <v-divider></v-divider>
                    </div>
                    
            <div class="ma-4">
         <v-chip-group multiple column active-class="light-green accent-3 black--text font-weight-medium">
        <v-chip v-for="tag in tags" small :key="tag">
          {{ tag }}
        </v-chip>
      </v-chip-group>
             <v-card-actions>
      <v-btn color="success" small outlined class="my-1t black--text" @click="">Reservar</v-btn>
    </v-card-actions>
            </div>
     
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
</style>
