<template>
  <div>
    <v-message-box :message="mBox" />
    <v-alert-box ref="alert" />
    <v-data-table :headers="headers" :items="items" sort-by="calories" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Blood analysis list</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="btnNewItem" dark class="mb-2">New Item</v-btn>
          <v-dialog v-model="dialog">
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-blood-analysis :bloodanalysis="editedItem" :check_acceptability="check_acceptability"/>
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
import vBloodAnalysis from "../create/v-blood-analysis";
import {Api} from "@/api/Api";
import vMessageBox from "../commons/v-message-box";
import MessageBox from "../commons/messagebox.js";
import vAlertBox from "../commons/v-alert-box"

import Helper from "../commons/functions.js"

export default {
  name: "v-blood-table",
  data: () => ({
    dialog: false,
    headers: [
      {
        text: "er",
        value: "er",
        align: "start",
        sortable: false
      },
      {
        text: "leyk",
        value: "leyk",
        align: "start",
        sortable: false
      },
      {
        text: "hb",
        value: "hb",
        align: "start",
        sortable: false
      },
      {
        text: "color",
        value: "color",
        align: "start",
        sortable: false
      },
      {
        text: "pok",
        value: "pok",
        align: "start",
        sortable: false
      },
      {
        text: "pya",
        value: "pya",
        align: "start",
        sortable: false
      },
      {
        text: "sya",
        value: "sya",
        align: "start",
        sortable: false
      },
      {
        text: "eoz",
        value: "eoz",
        align: "start",
        sortable: false
      },
      {
        text: "lf",
        value: "lf",
        align: "start",
        sortable: false
      },
      {
        text: "mon",
        value: "mon",
        align: "start",
        sortable: false
      },
      {
        text: "coe",
        value: "coe",
        align: "start",
        sortable: false
      },
      {
        text: "act",
        value: "act",
        align: "start",
        sortable: false
      },
      {
        text: "alt",
        value: "alt",
        align: "start",
        sortable: false
      },
      { text: "Status", value: "status", sortable: false },
      { text: "Date", value: "date", sortable: false },
      { text: "Actions", value: "actions", sortable: false }
    ],
    items: [],
    editedIndex: -1,
    editedItem: {},
    defaultItem: null,
    mBox: new MessageBox()
  }),
  props: ["patient", "check_acceptability"],
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
    initialize() {
      let mBox = this.mBox;
      let patient_id = this.patient.id;
      Api
        .get("/blood_request/" + patient_id)
        .then(respone => {
          //console.log(respone);
          respone.data.map(item => {
            this.items.push(this.toTemplate(item));
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
      let resOjb = {
        er: obj.er,
        leyk: obj.leyk,
        hb: obj.hb,
        color: obj.color,
        pok: obj.pok,
        pya: obj.pya,
        sya: obj.sya,
        eoz: obj.eoz,
        lf: obj.lf,
        mon: obj.mon,
        coe: obj.coe,
        act: obj.act,
        alt: obj.alt,

        status: this.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date
      };

      if (typeof obj.id != "undefined") resOjb.id = obj.id;

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        er: template.er,
        leyk: template.leyk,
        hb: template.hb,
        color: template.color,
        pok: template.pok,
        pya: template.pya,
        sya: template.sya,
        eoz: template.eoz,
        lf: template.lf,
        mon: template.mon,
        coe: template.coe,
        act: template.act,
        alt: template.alt,

        status: this.ToBoolFromYesNo(template.status),
        patient: template.patient,
        date: template.date
      };
      if (typeof template.id != "undefined") resObj.id = template.id;
      return resObj;
    },

    editItem(item) {
      this.editedIndex = this.items.indexOf(item);
      this.editedItem = this.toObject(item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.items.indexOf(item);
      let bloodanalysis = item;
      confirm("Are you sure you want to delete this item?") &&
        Api
        .delete("/blood_request", {
          data: {bloodanalysis}
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
      if (this.editedIndex > -1) {
        let bloodanalysis = this.editedItem;
        Api
          .put("/blood_request", {
            bloodanalysis
          })
          .then(() => {
            console.log("Updated");
            Object.assign(
              this.items[this.editedIndex],
              this.toTemplate(this.editedItem)
            );
            this.close();
          })
          .catch(e => {
            mBox.showMessage("Error", e, "error");
            console.log(e);
          });
      } else {
        var bloodanalysis = this.editedItem;
        Api
          .post("/blood_request", {
            bloodanalysis
          })
          .then(respone => {
            this.editedItem.id = respone.data;
            this.items.push(this.toTemplate(this.editedItem));
            this.close();
          })
          .catch(e => {
            mBox.showMessage("Error", e, "error");
            console.log(e);
          });
      }
    },
    btnNewItem() {
      this.defaultItem = {
        er: 0,
        leyk: 0,
        hb: 0,
        color: 0,
        pok: 0,
        pya: 0,
        sya: 0,
        eoz: 0,
        lf: 0,
        mon: 0,
        coe: 0,

        //date: new Date(),
        status: false,
        patient: this.patient.id
      };
      this.editedItem = Object.assign({}, this.defaultItem);
      this.dialog = true;
    },
  },
  components: {
    vBloodAnalysis,
    vMessageBox,
    vAlertBox
  },
  mounted: function() {

  }
};
</script>