<template>
    <v-container class="my-7">
    <v-row justify="center" align="center" class="my-1">
    <div class="form-group col-md-4">
         <v-btn class="my-3" block  color="light-blue darken-4 white--text" ><v-icon left size="25">mdi-facebook</v-icon> INICIA SESIÓN CON FACEBOOK</v-btn>
         <v-btn block  color="red darken-1 white--text" ><v-icon left size="25">mdi-google-plus</v-icon> INICIA SESIÓN CON GOOGLE</v-btn>
    <v-divider class="my-5"></v-divider>
    <!-- <v-card-text> -->
        <div class="form-group">
        <form>
            <div class="form-group">
                <span class="my-1 body-2 black--text">Email</span>
                <input type="text" required placeholder="Ingresa tu email" name="title" class="form-control">
            </div>
            <div class="form-group">
                <span class="my-1 body-2 black--text">Contraseña</span>
                <input type="password" required placeholder="Ingresa tu contraseña" name="title" class="form-control">
            </div>
                <v-btn class="my-1" block color="light-green accent-4 white--text">INICIA SESIÓN</v-btn>
        </form>
         <v-row justify="center" align="center" class="my-1">
            <router-link class="caption my-2" :to="{name: 'companies'}">¿Olvidaste tu contraseña?</router-link>
        </v-row>
        <v-divider></v-divider>
        </div>
    <!-- </v-card-text> -->
    <v-card-actions>
    <v-row justify="center" align="center" class="my-1">
        <span class="caption">¿Aún no tienes cuenta? </span>
        <router-link class="caption" :to="{name: 'home'}"> Regístrate</router-link>
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