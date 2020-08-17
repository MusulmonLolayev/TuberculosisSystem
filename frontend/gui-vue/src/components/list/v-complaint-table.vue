<template>
  <div>
    <v-data-table :headers="headers" :items="items" sort-by="calories" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Coplaint list</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="btnNewItem" dark class="mb-2">New Item</v-btn>
          <v-dialog v-model="dialog">
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-complaint :complaint="editedItem" />
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
import vComplaint from "../create/v-complaint";
import {Api} from "@/api/Api";
import { mapGetters, mapActions } from "vuex";

import Helper from "../commons/functions.js"


export default {
  name: "v-complaint-table",
  data: () => ({
    dialog: false,
    headers: [
      {
        text: "Diarrhea",
        value: "diarrhea",
        align: "start",
        sortable: false
      },
      {
        text: "Normal stool",
        align: "start",
        sortable: false,
        value: "normal_stool"
      },
      {
        text: "Constipation",
        value: "constipation",
        align: "start",
        sortable: false
      },
      {
        text: "Flatulence",
        value: "flatulence",
        align: "start",
        sortable: false
      },
      {
        text: "Stomachache",
        value: "stomachache",
        align: "start",
        sortable: false
      },
      {
        text: "From stool frequency",
        value: "from_stool_frequency",
        align: "start",
        sortable: false
      },
      {
        text: "To stool frequency",
        value: "to_stool_frequency",
        align: "start",
        sortable: false
      },
      {
        text: "Character of stool",
        value: "character.name",
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
    },
    ...mapGetters(["CHARACTER_STOOLS"])
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
      await this.GET_CHARACTER_STOOL_FROM_API();

      let patient_id = this.patient.id;
      await Api
        .get("/complaint_request/" + patient_id)
        .then(respone => {
          //console.log(respone);
          respone.data.map(item => {
            this.items.push(this.toTemplate(item));
          });
        })
        .catch(e => {
          console.log(e);
          this.$store.state.message.showMessage("Error", e, "error");
        });
    },
    ...mapActions(["GET_CHARACTER_STOOL_FROM_API"]),
    
    toTemplate(obj) {
      let resOjb = {
        diarrhea: Helper.ToYesNO(obj.diarrhea),
        normal_stool: Helper.ToYesNO(obj.normal_stool),
        constipation: Helper.ToYesNO(obj.constipation),
        flatulence: Helper.ToYesNO(obj.flatulence),
        stomachache: Helper.ToYesNO(obj.stomachache),
        from_stool_frequency: obj.from_stool_frequency,
        to_stool_frequency: obj.to_stool_frequency,
        character: this.CHARACTER_STOOLS.find(item => item.id == obj.character),

        status: Helper.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date
      };

      if (typeof obj.id != "undefined") resOjb.id = obj.id;

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        diarrhea: Helper.ToBoolFromYesNo(template.diarrhea),
        normal_stool: Helper.ToBoolFromYesNo(template.normal_stool),
        constipation: Helper.ToBoolFromYesNo(template.constipation),
        flatulence: Helper.ToBoolFromYesNo(template.flatulence),
        stomachache: Helper.ToBoolFromYesNo(template.stomachache),
        from_stool_frequency: template.from_stool_frequency,
        to_stool_frequency: template.to_stool_frequency,
        character: template.character.id,

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
      let response = await Helper.deleteInstance(item, '/complaint_request')
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
      let response = await Helper.saveInstance(this.editedItem, '/complaint_request')
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
      this.defaultItem = {
        diarrhea: false,
        normal_stool: false,
        constipation: false,
        flatulence: false,
        stomachache: false,
        from_stool_frequency: 0,
        to_stool_frequency: 0,
        character: this.CHARACTER_STOOLS[0].id,

        date: Helper.GetCurrentDate(),
        status: false,
        patient: this.patient.id
      };
      this.editedItem = Object.assign({}, this.defaultItem);
      this.dialog = true;
    }
  },
  components: {
    vComplaint,
  },
  mounted: function() {}
};
</script>