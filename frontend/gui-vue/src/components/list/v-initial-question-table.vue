<template>
  <div>
    <v-data-table :headers="headers" :items="items" sort-by="calories" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Initial question list</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="btnNewItem" dark class="mb-2">New Item</v-btn>
          <v-dialog v-model="dialog">
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-initial-question :selected="editedItem" />
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="save">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import vInitialQuestion from "../create/v-initial-question";
import {Api} from "@/api/Api";

import Helper from "../commons/functions.js"

export default {
  name: "v-intial-question-table",
  data: () => ({
    dialog: false,
    headers: [
      /*{
        text: "coe",
        value: "coe",
        align: "start",
        sortable: false
      },*/
      { text: "Status", value: "status", sortable: false },
      { text: "Date", value: "date", sortable: false },
      { text: "Actions", value: "actions", sortable: false }
    ],
    items: [],
    editedIndex: -1,
    editedItem: {},
    defaultItem: {
      checkbox: [],
      radio: {},

      //date: new Date(),
      status: false,
      //patient: this.patient.id
    },
    question_titles: [],
    questions: [],
  }),
  props: ["patient"],
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    }
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  },

  created() {
    this.initialize();
  },

  methods: {
    toRow(item) {
      let ids = item.questions.split(",");
      let row = {};
      if (ids.length > 1)
        ids.map(id => {
          let question = Object.assign(
            {},
            this.questions.find(q => q.id == id)
          );
          let attribut = "v" + question.question_title;
          if (typeof row[attribut] == "undefined") {
            row[attribut] = question;
          } else {
            row[attribut].text += "; " + question.text;
            row[attribut].id += "," + question.id;
          }
        });
      else{
        let id = item.questions
        let question = Object.assign(
            {},
            this.questions.find(q => q.id == id)
          );
          let attribut = "v" + question.question_title;
          if (typeof row[attribut] == "undefined") {
            row[attribut] = question;
          } else {
            row[attribut].text += "; " + question.text;
            row[attribut].id += "," + question.id;
          }
      }
      row["id"] = item.id;
      row["status"] = item.status;
      row["date"] = item.date;
      return row;
    },
    async initialize() {
      try {
        let response = await Api.get("/question_titles");
        let length = response.data.length;
        for (let i = 0; i < length; i++) {
          let item = response.data[length - i - 1];
          this.question_titles.push(item);
          this.headers.splice(0, 0, {
            text: item.name,
            value: "v" + item.id + ".text",
            align: "start",
            sortable: false
          });
        }

        response = await Api.get("/questions");
        response.data.map(x => {
          this.questions.push(x);
        });
      } catch (e) {
        this.$store.state.message.showMessage("Error", e, "error");
      }

      let patient_id = this.patient.id;
      Api
        .get("/initial_questions/" + patient_id)
        .then(respone => {
          respone.data.map(item => {
            let row = this.toRow(item);
            this.items.push(this.toTemplate(row));
          });
        })
        .catch(e => {
          console.log(e);
          this.$store.state.message.showMessage("Error", e, "error");
        });
    },
    toTemplate(obj) {
      let resObj = Object.assign({}, obj);
      resObj.status = Helper.ToYesNO(obj.status);

      if (typeof obj.id != "undefined") resObj.id = obj.id;

      return resObj;
    },
    toObject(template) {
      let resObj = Object.assign({}, template);
      resObj.status = Helper.ToBoolFromYesNo(template.status);

      if (typeof template.id != "undefined") resObj.id = template.id;
      return resObj;
    },
    toItem(row) {
      let res = {
        id: row.id,
        status: row.status,
        date: row.date,
        checkbox: [],
        radio: {}
      };

      this.question_titles.map(item => {
        let attribut = row["v" + item.id];
        if (typeof attribut != "undefined") {
          if (item.isMany) {
            if (typeof attribut.id == "number") res.checkbox.push(attribut.id);
            else
              attribut.id.split(",").map(id => {
                res.checkbox.push(parseInt(id));
              });
          } else {
            res.radio["r" + item.id] = attribut.id;
          }
        }
      });
      return res;
    },
    editItem(item) {
      this.editedIndex = this.items.indexOf(item);
      let row = this.toObject(item);
      this.editedItem = this.toItem(row);

      this.dialog = true;
    },
    DealSavingRespone(response){
      if (response == true){
        this.$store.state.message.showMessage('Action was successfully', Helper.message_types.success)
      }
      else{
        this.$store.state.message.showMessage('Action was unsuccessfully\n' + response, 
        Helper.message_types.error, 10000)
      }
    },
    async deleteItem(deletedItem) {
      const index = this.items.indexOf(deletedItem);
      deletedItem = this.toItem(deletedItem)
      let initial_question = {
        id: deletedItem.id,
        patient: this.patient.id,
        questions: "",
        status: deletedItem.status,
        date: deletedItem.date
      };
      // Convert the ids into text
      deletedItem.checkbox.map(item => {
        initial_question.questions += item + ",";
      });
      Object.values(deletedItem.radio).map(item => {
        initial_question.questions += item + ",";
      });

      // Clean the last mark (,)
      initial_question.questions = initial_question.questions.slice(0, -1);

      let response = await Helper.deleteInstance(initial_question, '/initial_question_request')
      if (response == true){
          this.items.splice(index, 1);
      }
      this.DealSavingRespone(response)
    },
    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
    async save() {
      let initial_question = {
        patient: this.patient.id,
        questions: "",
        status: this.editedItem.status,
        date: this.editedItem.date,
        id: this.editedItem.id
      };

      // Convert the ids into text
      this.editedItem.checkbox.map(item => {
        initial_question.questions += item + ",";
      });
      Object.values(this.editedItem.radio).map(item => {
        initial_question.questions += item + ",";
      });

      // Clean the last mark (,)
      initial_question.questions = initial_question.questions.slice(0, -1);
      let response = await Helper.saveInstance(initial_question, '/initial_question_request')
      if (response == true){
        let row = this.toRow(initial_question)
        if (this.editedIndex > -1){
          Object.assign(this.items[this.editedIndex], this.toTemplate(row))
        }
        else{
          this.items.push(this.toTemplate(row))
        }
        this.close();
      }
      this.DealSavingRespone(response)
    },
    btnNewItem() {
      this.defaultItem = {
        checkbox: [],
        radio: {},

        date: Helper.GetCurrentDate(),
        status: false,
        patient: this.patient.id
      };
      this.editedItem = Object.assign({}, this.defaultItem);
      this.dialog = true;
    }
  },
  components: {
    vInitialQuestion
  },
  mounted: function() {}
};
</script>