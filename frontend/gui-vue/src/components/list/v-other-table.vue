<template>
  <div>
    <v-message-box :message="mBox" />
    <v-alert-box ref="alert" />
    <v-data-table :headers="headers" :items="items" sort-by="calories" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Other analysis list</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="btnNewItem" dark class="mb-2">New Item</v-btn>
          <v-dialog v-model="dialog">
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-other :other="editedItem" />
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
import vOther from "../create/v-other";
import {Api} from "@/api/Api";
import vMessageBox from "../commons/v-message-box";
import MessageBox from "../commons/messagebox.js";
import Helper from '../commons/functions'
import vAlertBox from "../commons/v-alert-box"

export default {
  name: "v-other-table",
  data: () => ({
    dialog: false,
    headers: [
      {
        text: "Tuberculosis tolerance",
        value: "tuberculosis_tolerance",
        align: "start",
        sortable: false
      },
      {
        text: "related diseases",
        value: "related_disease",
        align: "start",
        sortable: false
      },
      {
        text: "Nausea",
        value: "nausea",
        align: "start",
        sortable: false
      },
      {
        text: "Vomiting",
        value: "vomiting",
        align: "start",
        sortable: false
      },
      {
        text: "Headache",
        value: "headache",
        align: "start",
        sortable: false
      },
      {
        text: "Sweating",
        value: "sweating",
        align: "start",
        sortable: false
      },
      {
        text: "Weakness",
        value: "weakness",
        align: "start",
        sortable: false
      },
      {
        text: "Allergodermatosis",
        value: "allergodermatosis",
        align: "start",
        sortable: false
      },
      {
        text: "From weight loss",
        value: "from_weight_loss",
        align: "start",
        sortable: false
      },
      {
        text: "To weight loss",
        value: "to_weight_loss",
        align: "start",
        sortable: false
      },
      {
        text: "Coproscopy",
        value: "coproscopy",
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
        .get("/other_request/" + patient_id)
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
        tuberculosis_tolerance: this.ToYesNO(obj.tuberculosis_tolerance),
        related_disease: this.ToYesNO(obj.related_disease),
        nausea: this.ToYesNO(obj.nausea),
        vomiting: this.ToYesNO(obj.vomiting),
        headache: this.ToYesNO(obj.headache),
        sweating: this.ToYesNO(obj.sweating),
        weakness: this.ToYesNO(obj.weakness),
        allergodermatosis: this.ToYesNO(obj.allergodermatosis),
        coproscopy: this.ToYesNO(obj.coproscopy),
        from_weight_loss: obj.from_weight_loss,
        to_weight_loss: obj.to_weight_loss,

        status: this.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date
      };

      if (typeof obj.id != "undefined") resOjb.id = obj.id;

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        tuberculosis_tolerance: this.ToBoolFromYesNo(template.tuberculosis_tolerance),
        related_disease: this.ToBoolFromYesNo(template.related_disease),
        nausea: this.ToBoolFromYesNo(template.nausea),
        vomiting: this.ToBoolFromYesNo(template.vomiting),
        headache: this.ToBoolFromYesNo(template.headache),
        sweating: this.ToBoolFromYesNo(template.sweating),
        weakness: this.ToBoolFromYesNo(template.weakness),
        allergodermatosis: this.ToBoolFromYesNo(template.allergodermatosis),
        coproscopy: this.ToBoolFromYesNo(template.coproscopy),
        from_weight_loss: template.from_weight_loss,
        to_weight_loss: template.to_weight_loss,

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
      let other = item;
      confirm("Are you sure you want to delete this item?") &&
        Api
        .delete("/other_request", {
          data: {other}
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
        let other = this.editedItem;
        Api
          .put("/other_request", {
            other
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
        var other = this.editedItem;
        Api
          .post("/other_request", {
            other
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
        related_disease: false,
        nausea: false,
        vomiting: false,
        headache: false,
        sweating: false,
        weakness: false,
        allergodermatosis: false,
        coproscopy: false,
        from_weight_loss: 0,
        to_weight_loss: 0,

        //date: new Date(),
        status: false,
        patient: this.patient.id
      };
      this.editedItem = Object.assign({}, this.defaultItem);
      this.dialog = true;
    }
  },
  components: {
    vOther,
    vMessageBox,
    vAlertBox,
  },
  mounted: function() {}
};
</script>