<template>
  <div>
    <v-data-table :headers="headers" :items="items" sort-by="calories" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Primary diagnoses list</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="btnNewItem" dark class="mb-2">New Item</v-btn>
          <v-dialog v-model="dialog">
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-primary-diagnose :primarydiagnose="editedItem" />
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
import vPrimaryDiagnose from "../create/v-primary-diagnose";
import {Api} from "@/api/Api";
import { mapGetters, mapActions } from "vuex";
import Helper from "../commons/functions";

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
    this.initialize();
  },

  methods: {
    async initialize() {

      await Promise.all([this.GET_CLINICAL_FORMS_FROM_API(), 
      this.GET_LOCALIZATION_FROM_API(), this.GET_PREVALENCES_FROM_API()])

      let patient_id = this.patient.id;
      await Api
        .get("/primary_request/" + patient_id)
        .then(respone => {
          //console.log(respone);
          respone.data.map(item => {
            this.items.push(this.toTemplate(item));
          });
        })
        .catch(e => {
          this.$store.state.message.showMessage("Error", e, "error");
        });
    },
    ...mapActions([
      "GET_CLINICAL_FORMS_FROM_API",
      "GET_LOCALIZATION_FROM_API",
      "GET_PREVALENCES_FROM_API"
    ]),
    toTemplate(obj) {
      let resOjb = {
        clinicalform: this.CLINICAL_FORMS.find(
          item => item.id == obj.clinicalform
        ),
        localization: this.LOCALIZATIONS.find(
          item => item.id == obj.localization
        ),
        prevalence: this.PREVALENCES.find(item => item.id == obj.prevalence),
        infiltration: Helper.ToYesNO(obj.infiltration),
        decay: Helper.ToYesNO(obj.decay),
        seeding: Helper.ToYesNO(obj.seeding),
        resorption: Helper.ToYesNO(obj.resorption),
        compaction: Helper.ToYesNO(obj.compaction),
        scarring: Helper.ToYesNO(obj.scarring),
        calcification: Helper.ToYesNO(obj.calcification),
        bk: Helper.ToPlusMinus(obj.bk),
        status: Helper.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date,
        id: obj.id,
      };

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        clinicalform: template.clinicalform.id,
        localization: template.localization.id,
        prevalence: template.prevalence.id,
        infiltration: Helper.ToBoolFromYesNo(template.infiltration),
        decay: Helper.ToBoolFromYesNo(template.decay),
        seeding: Helper.ToBoolFromYesNo(template.seeding),
        resorption: Helper.ToBoolFromYesNo(template.resorption),
        compaction: Helper.ToBoolFromYesNo(template.compaction),
        scarring: Helper.ToBoolFromYesNo(template.scarring),
        calcification: Helper.ToBoolFromYesNo(template.calcification),
        bk: Helper.ToBoolFromPlusMinus(template.bk),
        status: Helper.ToBoolFromYesNo(template.status),
        patient: template.patient,
        date: template.date,
        id: template.id,
      };
      return resObj;
    },

    editItem(item) {
      this.editedIndex = this.items.indexOf(item);
      this.editedItem = this.toObject(item);
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

    async deleteItem(item) {
      const index = this.items.indexOf(item);
      let response = await Helper.deleteInstance(item, '/primary_request')
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
      let response = await Helper.saveInstance(this.editedItem, '/primary_request')
      if (response == true){
        if (this.editedIndex > -1){
          Object.assign(
                this.items[this.editedIndex],
                this.toTemplate(this.editedItem)
              );
        }
        else{
          this.items.push(this.toTemplate(this.editedItem));
        }
        this.close();
      }
      this.DealSavingRespone(response)
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

        date: Helper.GetCurrentDate(),
        status: false,
        patient: this.patient.id
      };
      this.editedItem = Object.assign({}, this.defaultItem);
    }
  },
  components: {
    vPrimaryDiagnose
  },
  mounted: function() {}
};
</script>