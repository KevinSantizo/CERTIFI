<template>
    <v-container class="my-7">
        <v-row justify="center" align="center" class="my-1" width="100">
            <div class="form-group">
                <v-btn class="my-3" block  color="light-blue darken-4 white--text" ><v-icon left size="25">mdi-facebook</v-icon> INICIA SESIÓN CON FACEBOOK</v-btn>
                <v-btn block  color="red darken-1 white--text" ><v-icon left size="25">mdi-google-plus</v-icon> INICIA SESIÓN CON GOOGLE</v-btn>
                <v-divider class="my-5"></v-divider>
                    <div class="form-group">
                        <v-form ref="form" v-model="form"  class="pa-4 pt-6">
                            <v-text-field color="black" label="Email" type="email" placeholder ="Ingresa tu email" outlined height=5 autofocus></v-text-field>
                            <v-text-field color="black" label="Password" type="password" placeholder="Ingresa tu contraseña" outlined></v-text-field>
                            <v-btn block  color="light-green accent-4 white--text" >INICIA SESIÓN</v-btn>          
                        </v-form>
                        <v-row justify="center" align="center" class="my-1">
                            <router-link class="caption my-2" :to="{name: 'companies'}">¿Olvidaste tu contraseña?</router-link>
                        </v-row>
                        <v-divider></v-divider>
                    </div>
                <v-card-actions>
                    <v-row justify="center" align="center" class="my-1">
                        <span class="caption">¿Aún no tienes cuenta? </span><router-link class="caption" :to="{name: 'companies'}"> Regístrate</router-link>
                    </v-row>
                </v-card-actions>
            </div>
        </v-row>
    </v-container>
</template>


<script>
    export default {
         data: () => ({
      loading: false,
      selection: 1,
    }),

    methods: {
      reserve () {
        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
    },
    }
</script>

<style scoped>

</style>
