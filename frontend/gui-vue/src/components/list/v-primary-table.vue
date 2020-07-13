<template>
  <div>
    <v-message-box :data="mBox" />
    <v-data-table :headers="headers" :items="items" sort-by="calories" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Primary diagnoses list</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="btnNewItem" dark class="mb-2">New Item</v-btn>
          <v-dialog v-model="dialog" max-width="500px">
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-primary-edit :primarydiagnose="editedItem" />
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
import vPrimaryEdit from "../create/v-primary-edit";
import Api from "@/api/Api";
import { mapGetters, mapActions } from "vuex";
import vMessageBox from "../commons/v-message-box";
import MessageBox from "../commons/messagebox.js";

export default {
  data: () => ({
    dialog: false,
    headers: [
      {
        text: "Clinical form of disease",
        align: "start",
        sortable: false,
        value: "clinicalform.name"
      },
      {
        text: "Localization",
        value: "localization.name",
        align: "start",
        sortable: false
      },
      {
        text: "Prevalence",
        value: "prevalence.name",
        align: "start",
        sortable: false
      },
      {
        text: "Infiltration",
        value: "infiltration",
        align: "start",
        sortable: false
      },
      { text: "Decay", value: "decay", sortable: false },
      { text: "Seeding", value: "seeding", sortable: false },
      { text: "Resorption", value: "resorption", sortable: false },
      { text: "Compaction", value: "compaction", sortable: false },
      { text: "Scarring", value: "scarring", sortable: false },
      { text: "Calcification", value: "calcification", sortable: false },
      { text: "BK", value: "bk", sortable: false },
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
    },
    ...mapGetters(["CLINICAL_FORMS", "LOCALIZATIONS", "PREVALENCES"])
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  },

  created() {
    this.GET_CLINICAL_FORMS_FROM_API();
    this.GET_LOCALIZATION_FROM_API();
    this.GET_PREVALENCES_FROM_API();
    this.initialize();
  },

  methods: {
    initialize() {
      let patient_id = this.patient.id;
      let mBox = this.mBox;
      Api()
        .get("/primary_request/" + patient_id)
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
    ...mapActions([
      "GET_CLINICAL_FORMS_FROM_API",
      "GET_LOCALIZATION_FROM_API",
      "GET_PREVALENCES_FROM_API"
    ]),
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
        clinicalform: this.CLINICAL_FORMS.find(
          item => item.id == obj.clinicalform
        ),
        localization: this.LOCALIZATIONS.find(
          item => item.id == obj.localization
        ),
        prevalence: this.PREVALENCES.find(item => item.id == obj.prevalence),
        infiltration: this.ToYesNO(obj.infiltration),
        decay: this.ToYesNO(obj.decay),
        seeding: this.ToYesNO(obj.seeding),
        resorption: this.ToYesNO(obj.resorption),
        compaction: this.ToYesNO(obj.compaction),
        scarring: this.ToYesNO(obj.scarring),
        calcification: this.ToYesNO(obj.calcification),
        bk: this.ToPlusMinus(obj.bk),
        status: this.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date
      };

      if (typeof obj.id != "undefined") resOjb.id = obj.id;

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        clinicalform: template.clinicalform.id,
        localization: template.localization.id,
        prevalence: template.prevalence.id,
        infiltration: this.ToBoolFromYesNo(template.infiltration),
        decay: this.ToBoolFromYesNo(template.decay),
        seeding: this.ToBoolFromYesNo(template.seeding),
        resorption: this.ToBoolFromYesNo(template.resorption),
        compaction: this.ToBoolFromYesNo(template.compaction),
        scarring: this.ToBoolFromYesNo(template.scarring),
        calcification: this.ToBoolFromYesNo(template.calcification),
        bk: this.ToBoolFromPlusMinus(template.bk),
        status: this.ToBoolFromYesNo(template.status),
        patient: template.patient,
        date: template.date
      };
      if (typeof template.id != "undefined") resObj.id = template.id;
      return resObj;
    },

    editItem(item) {
      this.editedIndex = this.primaries.indexOf(item);
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
        let primarydiagnose = this.editedItem;
        Api()
          .put("/primary_request", {
            primarydiagnose
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
            console.log(e);
            mBox.showMessage("Error", e, "error");
          });
      } else {
        let primarydiagnose = this.editedItem;
        Api()
          .post("/primary_request", {
            primarydiagnose
          })
          .then(respone => {
            this.editItem.id = respone.data;
            this.items.push(this.toTemplate(this.editedItem));
            this.close();
          })
          .catch(e => {
            console.log(e);
            mBox.showMessage("Error", e, "error");
          });
      }
    },
    btnNewItem() {
      this.dialog = true;
      this.defaultItem = {
        clinicalform: this.CLINICAL_FORMS[0].id,
        localization: this.LOCALIZATIONS[0].id,
        prevalence: this.PREVALENCES[0].id,
        infiltration: false,
        decay: false,
        seeding: false,
        resorption: false,
        compaction: false,
        scarring: false,
        calcification: false,
        bk: false,

        //date: new Date(),
        status: false,
        patient: this.patient.id
      };
      this.editedItem = Object.assign({}, this.defaultItem);
    }
  },
  components: {
    vPrimaryEdit,
    vMessageBox
  },
  mounted: function() {}
};
</script>