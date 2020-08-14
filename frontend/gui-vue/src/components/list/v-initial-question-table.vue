<template>
  <div>
    <v-message-box :message="mBox" />
    <v-alert-box ref="alert" />
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
import vMessageBox from "../commons/v-message-box";
import MessageBox from "../commons/messagebox.js";
import vAlertBox from '../commons/v-alert-box'

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
    mBox: new MessageBox()
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
        console.log(e);
        this.mBox.showMessage("Error", e, "error");
      }

      let mBox = this.mBox;
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
          mBox.showMessage("Error", e, "error");
        });
    },
    ToYesNO(value) {
      return value == true ? "Yes" : "No";
    },
    ToBoolFromYesNo(value) {
      return value == "Yes";
    },
    ToPlusMinus(value) {
      return value == true ? "+" : "-";
    },
    ToBoolFromPlusMinus(value) {
      return value == "+";
    },
    toTemplate(obj) {
      let resObj = Object.assign({}, obj);
      resObj.status = this.ToYesNO(obj.status);

      if (typeof obj.id != "undefined") resObj.id = obj.id;

      return resObj;
    },
    toObject(template) {
      let resObj = Object.assign({}, template);
      resObj.status = this.ToBoolFromYesNo(template.status);

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

    deleteItem(item) {
      const index = this.items.indexOf(item);
      
      let initial_question = {
        patient: this.patient.id,
        questions: "",
        status: this.editedItem.status,
        date: this.editedItem.date
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

      initial_question.id = item.id

      confirm("Are you sure you want to delete this item?") &&
        Api
        .delete("/initial_question_request", {
          data: {initial_question}
        })
        .then(() => {
          this.$refs['alert'].showMessage('Deleted successfully', 
          Helper.message_types.success)
          this.items.splice(index, 1);
        })
        .catch((error) => {
          this.$refs['alert'].showMessage('Deleting action was unsuccessful: ' + error, 
          Helper.message_types.error, 5000)
        })
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      let mBox = this.mBox;

      let initial_question = {
        patient: this.patient.id,
        questions: "",
        status: this.editedItem.status,
        date: this.editedItem.date
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

      let _this = this;
      if (this.editedIndex > -1) {
        initial_question.id = this.editedItem.id;
        Api
          .put("/initial_question_request", {
            initial_question
          })
          .then(() => {
            let row = _this.toRow(initial_question);
            Object.assign(_this.items[this.editedIndex], _this.toTemplate(row));
            _this.close();
          })
          .catch(e => {
            mBox.showMessage("Error", e, "error");
            console.log(e);
          });
      } else {
        // Chech the primary diagnose id to be undefined to know ethier create instane or edit
        Api
          .post("/initial_question_request", {
            initial_question
          })
          .then(function(response) {
            let row = _this.toRow(initial_question);
            row.id = response.data;
            _this.items.push(_this.toTemplate(row));
            _this.close();
          })
          .catch(e => {
            console.log(e);
            this.mBox.showMessage("Error", e, "error");
          });
      }
    },
    btnNewItem() {
      this.defaultItem = {
        checkbox: [],
        radio: {},

        //date: new Date(),
        status: false,
        patient: this.patient.id
      };
      this.editedItem = Object.assign({}, this.defaultItem);
      this.dialog = true;
    }
  },
  components: {
    vInitialQuestion,
    vMessageBox,
    vAlertBox,
  },
  mounted: function() {}
};
</script>