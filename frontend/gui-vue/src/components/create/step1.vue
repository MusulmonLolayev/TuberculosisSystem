<template>
        <v-container>
            <h1>Step1: Initial information</h1>
            <v-row>
                <v-col cols="10" md="3">
                    <v-text-field
                        v-model="lastname"
                        :rules="nameRules"
                        label="Last name"
                        required/>
                </v-col>

                <v-col cols="10" md="3">
                    <v-text-field
                        v-model="firstname"
                        :rules="nameRules"
                        label="First name"
                        required />
                </v-col>

                <v-col cols="10" md="3">
                    <v-text-field
                        v-model="middlename"
                        :rules="middleRules"
                        label="Middle name"
                        required />
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="10" md="3">
                    <datepicker label='Date of birthday'/>
                </v-col>

                <v-col cols="10" md="3">
                    <v-radio-group v-model="row" row>
                        <v-radio label="Male" value="radio-1" />
                        <v-radio label="Female" value="radio-2" />
                    </v-radio-group>
                </v-col>
            </v-row>
            
            <h2>Address</h2>
            <v-row>
                <v-col cols="10" md="3">
                    <v-select
                        :items="items"
                        label="Country" />
                </v-col>
                
                <v-col cols="10" md="3">
                    <v-select
                        :items="items"
                        label="Region" />
                </v-col>
                <v-col cols="10" md="3">
                    <v-select
                        :items="items"
                        label="District" />
                </v-col>

                <v-col cols="10" md="9">
                    <v-text-field
                        v-model="address_line"
                        label="Address line"
                        required/>
                </v-col>
            </v-row>

            <h2>Addinational information</h2>
            <v-row>
                <v-col cols="10" md="3">
                    <datepicker label='Date of birthday'/>
                </v-col>
                
                <v-col cols="10" md="3">
                    <v-select
                        :items="items"
                        label="Profession" />
                </v-col>
                
                
            </v-row>
        </v-container>
</template>

<script>
import datepicker from '../inputs/datepicker'
export default {
    name: 'CreateMainInformation', 
    components: {
        datepicker,
    }
}
</script>


<style scoped>
    .card-form {
        margin:auto;
        margin-top:50px;
        max-width: 850px;
        width: 100%;
        border-radius: 10px;
        padding: 10px;
        float: center;
    }
    .header{
        align-content: center;
    }
    label{
        margin: 10px;
        margin-inline: initial;
    }
</style>