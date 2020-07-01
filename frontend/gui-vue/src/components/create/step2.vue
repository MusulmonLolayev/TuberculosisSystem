<template>
  <v-container>
      <h1>Please, answer the questions below!</h1>
      <v-row>
          <v-checkbox
            v-model="selected" 
            v-for="question in questions" 
            v-bind:key="question.id"
            :label="question.text"
            :value="question.text"
            />
      </v-row>
      <v-row>
          <v-card
            class="mx-auto"
            max-width="300"
            >
            <v-card-text>
                <h2>The result of the answers</h2>
                <p class="display-1 text--primary">
                    Checked answers number is {{selected.length}}
                </p>
                <h1>Diagnose</h1>

                <div class="text--primary">
                    <v-label :disabled="selected.length < 3" > You must take the next examination </v-label>
                    <v-label :disabled="selected.length >= 3"> You should not take the next examination </v-label>
                </div>
            </v-card-text>
            <v-card-actions>
                
            </v-card-actions>
        </v-card>
      </v-row>
  </v-container>
</template>

<script>
export default {
    name: 'step2',
    data: function(){
        return{
            questions: [
                {id: 1, text: 'Question 1'},
                {id: 2, text: 'Question 2'},
                {id: 3, text: 'Question 3'},
                {id: 4, text: 'Question 4'},
            ],
            selected: [],
        }
    }
}
</script>