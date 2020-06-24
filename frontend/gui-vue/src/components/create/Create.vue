<template>
    <v-form v-model="valid" class="card-form">
        <step1 v-if="step_count == 1"/>
        <step2 v-if="step_count == 2"/>
        <v-card-actions>
            <v-btn text>Save</v-btn>
            <v-btn text v-on:click="step_count--" :disabled="step_count <= 1">Back</v-btn>
            <v-btn text v-on:click="step_count++" :disabled="step_max < step_count">Next</v-btn>
        </v-card-actions>
    </v-form>
</template>

<script>
import step1 from './step1'
import step2 from './step2'

export default {
    components:{
        step1,
        step2
    },
    data: function(){
        return {
            step_count: 1,
            step_max: 1
        }
    }
}
</script>