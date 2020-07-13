<template>
  <div>
    <v-message-box :data="mBox" />
    <v-data-table :headers="headers" :items="items" sort-by="calories" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Taking medicine list</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="btnNewItem" dark class="mb-2">New Item</v-btn>
          <v-dialog v-model="dialog" max-width="500px">
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-taking-medicine :takingmedicine="editedItem" />
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
import vTakingMedicine from "../create/v-taking-medicine";
import Api from "@/api/Api";
import vMessageBox from "../commons/v-message-box";
import MessageBox from "../commons/messagebox.js";

export default {
  name: "v-taking-medicine-table",
  data: () => ({
    dialog: false,
    headers: [
      { text: "From date", value: "fromdate", sortable: false },
      {
        text: "Streptomycin",
        align: "start",
        sortable: false,
        value: "streptomycin"
      },
      {
        text: "Rifampicin",
        value: "rifampicin",
        align: "start",
        sortable: false
      },
      {
        text: "Isoniazid",
        value: "isoniazid",
        align: "start",
        sortable: false
      },
      {
        text: "Pyrazinamide",
        value: "pyrazinamide",
        align: "start",
        sortable: false
      },
      {
        text: "Ethambutol",
        value: "ethambutol",
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
      Api()
        .get("/taking_request/" + patient_id)
        .then(respone => {
          console.log(respone);
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
        fromdate: obj.fromdate,
        streptomycin: this.ToYesNO(obj.streptomycin),
        rifampicin: this.ToYesNO(obj.rifampicin),
        isoniazid: this.ToYesNO(obj.isoniazid),
        pyrazinamide: this.ToYesNO(obj.pyrazinamide),
        ethambutol: this.ToYesNO(obj.ethambutol),

        status: this.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date
      };

      if (typeof obj.id != "undefined") resOjb.id = obj.id;

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        fromdate: template.fromdate,
        streptomycin: this.ToBoolFromYesNo(template.streptomycin),
        rifampicin: this.ToBoolFromYesNo(template.rifampicin),
        isoniazid: this.ToBoolFromYesNo(template.isoniazid),
        pyrazinamide: this.ToBoolFromYesNo(template.pyrazinamide),
        ethambutol: this.ToBoolFromYesNo(template.ethambutol),

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
        let takingmedicine = this.editedItem;
        Api()
          .put("/taking_request", {
            takingmedicine
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
        let takingmedicine = this.editedItem;
        Api()
          .post("/taking_request", {
            takingmedicine
          })
          .then(respone => {
            console.log("Created");
            this.editItem.id = respone.data;
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
      this.dialog = true;
      this.defaultItem = {
        //fromdate: new Date().toISOString(),
        streptomycin: false,
        rifampicin: false,
        isoniazid: false,
        pyrazinamide: false,
        ethambutol: false,

        //date: new Date(),
        status: false,
        patient: this.patient.id
      };
      this.editedItem = Object.assign({}, this.defaultItem);
    }
  },
  components: {
    vTakingMedicine,
    vMessageBox
  },
  mounted: function() {}
};
</script>