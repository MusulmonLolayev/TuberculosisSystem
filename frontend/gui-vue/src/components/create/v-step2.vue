<template>
  <div>
    <v-message-box :message="mBox" />
    <ol>
      <li v-for="(item, index) in question_titles" :key="'Q' + index">
        <h3>{{item.title}}</h3>
        <ul v-if="item.isMany">
          <li
            v-for="(option_item, option_index) in get_questions(item.id)"
            :key="index + '_' + option_index"
          >
            <v-checkbox
              multiple
              :label="option_item.text"
              style="margin:0px"
              v-model="selected_check"
              :value="option_item.id"
            />
          </li>
        </ul>
        <ul v-else>
          <v-radio-group v-model="selected_radio" multiple style="margin:0px" row @change="Checked">
            <li
              v-for="(option_item, option_index) in get_questions(item.id)"
              :key="index + '_' + option_index"
            >
              <v-radio :label="option_item.text" :value="option_item.id" style="margin:0px" />
            </li>
          </v-radio-group>
        </ul>
      </li>
    </ol>
  </div>
</template>

<script>
import Api from "@/api/Api";
import vMessageBox from "../commons/v-message-box";
import MessgeBox from "../commons/messagebox.js";

export default {
  name: "v-step2",
  data: function() {
    return {
      question_titles: [],
      questions: [],
      selected_check: [],
      selected_radio: [],
      mBox: new MessgeBox()
    };
  },
  created() {
    this.initialize();
  },
  methods: {
    async initialize() {
      try {
        let response = await Api().get("/question_titles");
        for (let i = 0; i < response.data.length; i++) {
          let item = response.data[i];
          this.question_titles.push(item);
        }

        response = await Api().get("/questions");
        response.data.map(x => {
          this.questions.push(x);
        });
      } catch (e) {
        console.log(e);
        this.mBox.showMessage("Error", e, "error");
      }
    },
    get_questions(title_id) {
      let res = [];
      this.questions.map(item => {
        if (item.question_title == title_id) res.push(item);
      });
      return res;
    },
    Checked() {
      console.log(this.selected_radio);
    }
  },
  components: {
    vMessageBox
  }
};
</script>

<style scoped>
li {
  list-style-type: none;
}
</style>