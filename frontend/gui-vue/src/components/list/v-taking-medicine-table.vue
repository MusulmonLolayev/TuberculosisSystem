<template>
  <div>
    <v-data-table :headers="headers" :items="items" sort-by="calories" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Taking medicine list</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="btnNewItem" dark class="mb-2">New Item</v-btn>
          <v-dialog v-model="dialog">
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
import {Api} from "@/api/Api";
import Helper from "../commons/functions.js"

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
    async initialize() {
      let patient_id = this.patient.id;
      await Api
        .get("/taking_request/" + patient_id)
        .then(respone => {
          respone.data.map(item => {
            this.items.push(this.toTemplate(item));
          });
        })
        .catch(e => {
          this.$store.state.message.showMessage("Error", e, "error");
        });
    },
    toTemplate(obj) {
      let resOjb = {
        fromdate: obj.fromdate,
        streptomycin: Helper.ToYesNO(obj.streptomycin),
        rifampicin: Helper.ToYesNO(obj.rifampicin),
        isoniazid: Helper.ToYesNO(obj.isoniazid),
        pyrazinamide: Helper.ToYesNO(obj.pyrazinamide),
        ethambutol: Helper.ToYesNO(obj.ethambutol),

        status: Helper.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date
      };

      if (typeof obj.id != "undefined") resOjb.id = obj.id;

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        fromdate: template.fromdate,
        streptomycin: Helper.ToBoolFromYesNo(template.streptomycin),
        rifampicin: Helper.ToBoolFromYesNo(template.rifampicin),
        isoniazid: Helper.ToBoolFromYesNo(template.isoniazid),
        pyrazinamide: Helper.ToBoolFromYesNo(template.pyrazinamide),
        ethambutol: Helper.ToBoolFromYesNo(template.ethambutol),

        status: Helper.ToBoolFromYesNo(template.status),
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
      let response = await Helper.deleteInstance(item, '/taking_request')
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
      let response = await Helper.saveInstance(this.editedItem, '/taking_request')
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
        fromdate: Helper.GetCurrentDate(),
        streptomycin: false,
        rifampicin: false,
        isoniazid: false,
        pyrazinamide: false,
        ethambutol: false,

        date: Helper.GetCurrentDate(),
        status: false,
        patient: this.patient.id
      };
      this.editedItem = Object.assign({}, this.defaultItem);
    }
  },
  components: {
    vTakingMedicine
  },
  mounted: function() {}
};
</script>