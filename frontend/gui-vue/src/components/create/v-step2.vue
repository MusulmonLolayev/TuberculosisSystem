<template>
  <v-row>
    <v-checkbox
      v-model="selected"
      v-for="question in questions"
      v-bind:key="question.id"
      :label="question.text"
      :value="question.text"
    />
  </v-row>
</template>

<script>
export default {
  name: "v-step2",
  data: function() {
    return {
      questions: [
        { id: 1, text: "Question 1" },
        { id: 2, text: "Question 2" },
        { id: 3, text: "Question 3" },
        { id: 4, text: "Question 4" }
      ],
      selected: []
    };
  }
};
</script>