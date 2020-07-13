<template>
  <div>
    <v-message-box :data="mBox" />
    <v-data-table :headers="headers" :items="items" sort-by="calories" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Coplaint list</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="btnNewItem" dark class="mb-2">New Item</v-btn>
          <v-dialog v-model="dialog" max-width="500px">
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
import Api from "@/api/Api";
import vMessageBox from "../commons/v-message-box";
import MessageBox from "../commons/messagebox.js";
import { mapGetters, mapActions } from "vuex";

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
    mBox: new MessageBox()
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
    this.GET_CHARACTER_STOOL_FROM_API();
  },

  methods: {
    initialize() {
      let mBox = this.mBox;
      let patient_id = this.patient.id;
      Api()
        .get("/complaint_request/" + patient_id)
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
    ...mapActions(["GET_CHARACTER_STOOL_FROM_API"]),
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
        diarrhea: this.ToYesNO(obj.diarrhea),
        normal_stool: this.ToYesNO(obj.normal_stool),
        constipation: this.ToYesNO(obj.constipation),
        flatulence: this.ToYesNO(obj.flatulence),
        stomachache: this.ToYesNO(obj.stomachache),
        from_stool_frequency: obj.from_stool_frequency,
        to_stool_frequency: obj.to_stool_frequency,
        character: this.CHARACTER_STOOLS.find(item => item.id == obj.character),

        status: this.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date
      };

      if (typeof obj.id != "undefined") resOjb.id = obj.id;

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        diarrhea: this.ToBoolFromYesNo(template.diarrhea),
        normal_stool: this.ToBoolFromYesNo(template.normal_stool),
        constipation: this.ToBoolFromYesNo(template.constipation),
        flatulence: this.ToBoolFromYesNo(template.flatulence),
        stomachache: this.ToBoolFromYesNo(template.stomachache),
        from_stool_frequency: template.from_stool_frequency,
        to_stool_frequency: template.to_stool_frequency,
        character: template.character.id,

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
        let complaint = this.editedItem;
        Api()
          .put("/complaint_request", {
            complaint
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
        var complaint = this.editedItem;
        Api()
          .post("/complaint_request", {
            complaint
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
        diarrhea: false,
        normal_stool: false,
        constipation: false,
        flatulence: false,
        stomachache: false,
        from_stool_frequency: 0,
        to_stool_frequency: 0,
        character: this.CHARACTER_STOOLS[0].id,

        //date: new Date(),
        status: false,
        patient: this.patient.id
      };
      this.editedItem = Object.assign({}, this.defaultItem);
      this.dialog = true;
    }
  },
  components: {
    vComplaint,
    vMessageBox
  },
  mounted: function() {}
};
</script>