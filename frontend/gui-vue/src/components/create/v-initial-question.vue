<template>
  <div>
    <ol>
      <li v-for="(item, index) in question_titles" :key="'Q' + index">
        <h3>{{item.title}}</h3>
        <ul v-if="item.isMany">
          <li style="list-style-type: none;">
            <v-row style="margin:0px">
              <v-col
                v-for="(option_item, option_index) in get_questions(item.id)"
                :key="index + '_' + option_index"
                md="3"
                cols="10"
                style="margin:0px"
              >
                <v-checkbox
                  multiple
                  :label="option_item.text"
                  v-model="selected.checkbox"
                  :value="option_item.id"
                />
              </v-col>
            </v-row>
          </li>
        </ul>
        <ul v-else>
          <v-radio-group
            v-model="selected.radio['r' + item.id]"
            style="margin-top:0px; margin-bottom:0px"
          >
            <li style="list-style-type: none;">
              <v-row style="margin:0px">
                <v-col
                  v-for="(option_item, option_index) in get_questions(item.id)"
                  :key="index + '_' + option_index"
                  md="3"
                  cols="10"
                  style="margin:0px"
                >
                  <v-radio :label="option_item.text" :value="option_item.id" />
                </v-col>
              </v-row>
            </li>
          </v-radio-group>
        </ul>
      </li>
    </ol>
    <v-row>
      <v-col cols="10" md="3">
        <v-checkbox v-model="selected.status" label="Status" />
      </v-col>
      <v-col cols="10" md="3">
        <v-text-field
        label="Date"
        v-model="selected.date"
        type='date'
      />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import {Api} from "@/api/Api";
import Helper from "../commons/functions.js";

export default {
  name: "v-step2",
  props: ["selected"],
  data: function() {
    return {
      question_titles: [],
      questions: [],
    };
  },
  created() {
    this.initialize();
  },
  methods: {
    async initialize() {
      if (typeof this.selected.id == "undefined") {
        this.selected.date = Helper.GetCurrentDate();
      }
      try {
        let response = await Api.get("/question_titles");
        for (let i = 0; i < response.data.length; i++) {
          let item = response.data[i];
          this.question_titles.push(item);
        }

        response = await Api.get("/questions");
        response.data.map(x => {
          this.questions.push(x);
        });
      } catch (e) {
        this.$store.state.message.showMessage("Error", e, "error");
      }
    },
    get_questions(title_id) {
      let res = [];
      this.questions.map(item => {
        if (item.question_title == title_id) res.push(item);
      });
      return res;
    },
  },
};
</script>

<style scoped>
</style>