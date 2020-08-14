<template>
  <div>
    <v-message-box :message="mBox" />
    <v-data-table :headers="headers" :items="items" sort-by="calories" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Immunogram analysis list</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="btnNewItem" dark class="mb-2">New Item</v-btn>
          <v-dialog v-model="dialog">
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-immunogram-analysis :immunogram="editedItem" />
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
import vImmunogramAnalysis from "../create/v-immunogram";
import {Api} from "@/api/Api";
import vMessageBox from "../commons/v-message-box";
import MessageBox from "../commons/messagebox.js";

export default {
  name: "v-immunogram-table",
  data: () => ({
    dialog: false,
    headers: [
      {
        text: "CD3",
        value: "cd3",
        align: "start",
        sortable: false
      },
      {
        text: "CD4",
        value: "cd4",
        align: "start",
        sortable: false
      },
      {
        text: "CD8",
        value: "cd8",
        align: "start",
        sortable: false
      },
      {
        text: "CD20",
        value: "cd20",
        align: "start",
        sortable: false
      },
      {
        text: "IgM",
        value: "igm",
        align: "start",
        sortable: false
      },
      {
        text: "IgG",
        value: "igg",
        align: "start",
        sortable: false
      },
      {
        text: "IgA",
        value: "iga",
        align: "start",
        sortable: false
      },
      {
        text: "TgE",
        value: "tge",
        align: "start",
        sortable: false
      },
      {
        text: "ACT",
        value: "act",
        align: "start",
        sortable: false
      },
      {
        text: "ALT",
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
    initialize() {
      let mBox = this.mBox;
      let patient_id = this.patient.id;
      Api
        .get("/immunogram_request/" + patient_id)
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
        cd3: obj.cd3,
        cd4: obj.cd4,
        cd8: obj.cd8,
        cd20: obj.cd20,
        igm: obj.igm,
        igg: obj.igg,
        iga: obj.iga,
        tge: obj.tge,
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
        cd3: template.cd3,
        cd4: template.cd4,
        cd8: template.cd8,
        cd20: template.cd20,
        igm: template.igm,
        igg: template.igg,
        iga: template.iga,
        tge: template.tge,
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
      confirm("Are you sure you want to delete this item?") &&
        this.items.splice(index, 1);
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
        let immunogram = this.editedItem;
        Api
          .put("/immunogram_request", {
            immunogram
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
        var immunogram = this.editedItem;
        Api
          .post("/immunogram_request", {
            immunogram
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
        cd3: 0,
        cd4: 0,
        cd8: 0,
        cd20: 0,
        igm: 0,
        igg: 0,
        iga: 0,
        tge: 0,
        act: 0,
        alt: 0,

        //date: new Date(),
        status: false,
        patient: this.patient.id
      };
      this.editedItem = Object.assign({}, this.defaultItem);
      this.dialog = true;
    }
  },
  components: {
    vImmunogramAnalysis,
    vMessageBox
  },
  mounted: function() {}
};
</script>