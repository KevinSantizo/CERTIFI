<template>
    <v-container class="my-4">
        <v-row justify="center" align="center" class="my-1 " >
            <div class="form-group form pa-4 grey lighten-4">
                <v-btn class="my-3" block  color="light-blue darken-4 white--text" ><v-icon left size="25">mdi-facebook</v-icon> REGÍSTRATE CON FACEBOOK</v-btn>
                <v-btn block  color="red darken-1 white--text" ><v-icon left size="25">mdi-google-plus</v-icon> REGÍSTRATE CON GOOGLE</v-btn>
                <v-divider class="my-5"></v-divider>
                    <div class="form-group">
                        <v-form ref="form" v-model="form"  class="">
                            <v-text-field color="black" label="Nombres" type="text" placeholder ="Ingresa tus nombres" outlined height=5 autofocus></v-text-field>
                            <v-text-field color="black" label="Apelidos" type="text" placeholder="Ingresa tus apellidos " outlined></v-text-field>
                            <v-text-field color="black" label="Teléfono" type="text" placeholder="Ingresa tu teléfono " outlined></v-text-field>
                            <v-text-field color="black" label="Email" type="email" placeholder="Ingresa tu email " outlined></v-text-field>
                            <v-text-field color="black" label="Contraseña" type="password" placeholder="Crea tu contraseña " outlined></v-text-field>

                            <v-btn block  color="light-green accent-4 white--text" >CREAR MI CUENTA</v-btn>          
                        </v-form>
                    </div>
                <template>
                    <v-row justify="center" align="center" class="my-1">
                        <div>
                        <span class="caption">¿Ya tienes una cuenta? </span>
                        </div>
                        <div>
                        <router-link class="caption" :to="{name: 'login'}"><span>Inicia Sesión</span></router-link>
                        </div>
                    </v-row>
                    <v-row justify="center" align="center" class="my-1">
                        <img src="@/assets/ball.svg" alt="" style="width: 35px;">
                    </v-row>
                </template>
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
.form {
    width: 30em;
    bottom: 3em !important;
    border: 1px solid black;
    border-radius: 10px;
}

</style>
