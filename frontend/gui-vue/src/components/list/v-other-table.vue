<template>
  <div>
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
import Helper from '../commons/functions'

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
          this.$store.state.message.showMessage("Error", e, "error");
        });
    },
    toTemplate(obj) {
      let resOjb = {
        tuberculosis_tolerance: Helper.ToYesNO(obj.tuberculosis_tolerance),
        related_disease: Helper.ToYesNO(obj.related_disease),
        nausea: Helper.ToYesNO(obj.nausea),
        vomiting: Helper.ToYesNO(obj.vomiting),
        headache: Helper.ToYesNO(obj.headache),
        sweating: Helper.ToYesNO(obj.sweating),
        weakness: Helper.ToYesNO(obj.weakness),
        allergodermatosis: Helper.ToYesNO(obj.allergodermatosis),
        coproscopy: Helper.ToYesNO(obj.coproscopy),
        from_weight_loss: obj.from_weight_loss,
        to_weight_loss: obj.to_weight_loss,

        status: Helper.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date
      };

      if (typeof obj.id != "undefined") resOjb.id = obj.id;

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        tuberculosis_tolerance: Helper.ToBoolFromYesNo(template.tuberculosis_tolerance),
        related_disease: Helper.ToBoolFromYesNo(template.related_disease),
        nausea: Helper.ToBoolFromYesNo(template.nausea),
        vomiting: Helper.ToBoolFromYesNo(template.vomiting),
        headache: Helper.ToBoolFromYesNo(template.headache),
        sweating: Helper.ToBoolFromYesNo(template.sweating),
        weakness: Helper.ToBoolFromYesNo(template.weakness),
        allergodermatosis: Helper.ToBoolFromYesNo(template.allergodermatosis),
        coproscopy: Helper.ToBoolFromYesNo(template.coproscopy),
        from_weight_loss: template.from_weight_loss,
        to_weight_loss: template.to_weight_loss,

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
      let response = await Helper.deleteInstance(item, '/other_request')
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
      let response = await Helper.saveInstance(this.editedItem, '/other_request')
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

        date: Helper.GetCurrentDate(),
        status: false,
        patient: this.patient.id
      };
      this.editedItem = Object.assign({}, this.defaultItem);
      this.dialog = true;
    }
  },
  components: {
    vOther },
  mounted: function() {}
};
</script>