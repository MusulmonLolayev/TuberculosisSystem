<template>
  <v-container>
     <v-row>
        <v-col cols="10" md="4">
            <v-select
                label="Clinical form of Tuberculosis" 
                :items="CLINICAL_FORMS"
                item-text='name'
                @change="clinicalformChanged"
                return-object
                item-value="id"
                v-model="selectedClinicalForm"
            />
        </v-col>
        <v-col cols="10" md="3">
            <v-select
                label="Localization" 
                :items="LOCALIZATIONS"
                item-text='name'
                @change="localizationChanged"
                return-object
                item-value="id"
                v-model="selectedLocalization"
            />
        </v-col>
        <v-col cols="10" md="3">
            <v-select
                label="Prevalence" 
                :items="Prevalences"
                item-text='name'
                @change="prevalenceChanged"
                return-object
                item-value="id"
                v-model="selectedPrevalence"
            />
        </v-col>
     </v-row> 
     <v-row>
         <v-col cols="10" md="2">
            <v-checkbox
                v-model="primarydiagnose.infiltration"
                label="Infiltration"
            />
         </v-col>
         <v-col cols="10" md="2">
            <v-checkbox
                v-model="primarydiagnose.decay"
                label="Decay"
            />
         </v-col>
         <v-col cols="10" md="2">
            <v-checkbox
                v-model="primarydiagnose.seeding"
                label="Seeding"
            />
         </v-col>
         <v-col cols="10" md="2">
            <v-checkbox
                v-model="primarydiagnose.resorption"
                label="Resorption"
            />
         </v-col>
         <v-col cols="10" md="2">
            <v-checkbox
                v-model="primarydiagnose.compaction"
                label="Compaction"
            />
         </v-col>
         <v-col cols="10" md="2">
            <v-checkbox
                v-model="primarydiagnose.scarring"
                label="Scarring"
            />
         </v-col>
         <v-col cols="10" md="2">
            <v-checkbox
                v-model="primarydiagnose.calcification"
                label="Calcification"
            />
         </v-col>
         <v-col cols="10" md="2">
            BK
            <v-radio-group row v-model="bk" @change='rbChange'>
                <v-radio label="+" :value="0" />
                <v-radio label="-" :value="1"/>
            </v-radio-group>
         </v-col>
     </v-row>
  </v-container>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
import Api from '@/api/Api'

export default {
    name: 'PrimaryDiagnose',
    props: ['primarydiagnose'],
    data: function(){
        return {
            selectedClinicalForm: {},
            selectedLocalization: {},
            selectedPrevalence: {},
            Prevalences: [],
            bk: 0,
        }
    },
    methods: {
        clinicalformChanged(e){
            this.primarydiagnose.clinicalform = e.id
        },
        localizationChanged(e){
            this.primarydiagnose.localization = e.id
        },
        prevalenceChanged(e){
            this.primarydiagnose.prevalence = e.id
        },
        ...mapActions([
            'GET_CLINICAL_FORMS_FROM_API',
            'GET_LOCALIZATION_FROM_API',
        ]),
        GET_PREVALENCES_FROM_API(){
            let self = this
            Api().get('/prevalence')
            .then((response) => {
                self.Prevalences = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
        rbChange(e){
            this.primarydiagnose.bk = e == 0 ? true : false
        }
    },
    computed: {
        ...mapGetters([
            'CLINICAL_FORMS',
            'LOCALIZATIONS',
        ]),
    },
    mounted() {
        this.GET_CLINICAL_FORMS_FROM_API()
        this.GET_LOCALIZATION_FROM_API()
        this.GET_PREVALENCES_FROM_API()
        
        // When the object of props is editing
        if (typeof this.primarydiagnose.id != 'undefined'){
            
            // set selections
            this.selectedPrevalence = this.primarydiagnose.clinicalform
            this.selectedLocalization = this.primarydiagnose.localization
            this.selectedPrevalence = this.primarydiagnose.prevalence

            this.bk = this.primarydiagnose.bk ? 0 : 1
        }
    },
}
</script>

<style>

</style>