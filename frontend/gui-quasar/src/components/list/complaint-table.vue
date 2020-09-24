<template>
  <div>
    <q-table
      :data="items"
      :columns="headers"
      dense
      selection="single"
      :selected.sync="selectedItems"
      :no-data-label="$t('nothingtoshow')"
      :rows-per-page-label="$t('rows_per_page_label')+':'"
      :selected-rows-label="$helper.getSelectedString"
      :pagination-label="$helper.get_pagination_label"
    >
      <template v-slot:top>
        <q-btn icon="add" color="primary" @click="btnNewItem" dense />
        <q-btn
          icon="edit"
          class="q-ml-sm"
          color="primary"
          :disable="!IsSelectedItem"
          @click="editItem"
          dense
        />
        <q-btn
          icon="remove"
          class="q-ml-sm"
          color="primary"
          :disable="!IsSelectedItem"
          @click="deleteItem"
          dense
        />
      </template>
    </q-table>

    <q-dialog v-model="dialog">
      <q-card>
        <q-card-section>
          <span class="headline">{{ formTitle }}</span>
        </q-card-section>
        <q-separator />
        <q-card-section class="q-pt-none">
          <Complaint :complaint="editedItem" />
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn color="blue darken-1" dense @click="close" :label="$t('cancel')" />
          <q-btn color="blue darken-1" dense @click="save" :label="$t('save')" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import Complaint from "../editors/complaint";

export default {
  name: "ComplaintTable",
  data: () => ({
    dialog: false,
    headers: [],
    items: [],
    editedIndex: -1,
    editedItem: {},
    defaultItem: null,
    selectedItems: [],
    CHARACTER_STOOLS: [],
  }),
  props: ["patient"],
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? this.$t("new_item") : this.$t("editing");
    },
    IsSelectedItem() {
      return this.selectedItems.length;
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
  },

  beforeMount() {
    this.initialize();
  },

  methods: {
    async initialize() {
      this.headers = [
        {
          label: this.$t("diarrhea"),
          field: "diarrhea",
        },
        {
          label: this.$t("normal_stool"),
          field: "normal_stool",
        },
        {
          label: this.$t("constipation"),
          field: "constipation",
        },
        {
          label: this.$t("flatulence"),
          field: "flatulence",
        },
        {
          label: this.$t("stomachache"),
          field: "stomachache",
        },
        {
          label: this.$t("from"),
          field: "from_stool_frequency",
        },
        {
          label: this.$t("to"),
          field: "to_stool_frequency",
        },
        {
          label: this.$t("character"),
          field: row => row.character.name,
        },
        { label: this.$t("status"), field: "status" },
        { label: this.$t("date"), field: "date" },
      ];

      await this.$axios.get("/characterofstool").then((response) => {
        this.CHARACTER_STOOLS = response.data;
      });
      let patient_id = this.patient.id;
      await this.$axios
        .get("/complaint_request/" + patient_id)
        .then((respone) => {
          //console.log(respone);
          respone.data.map((item) => {
            this.items.push(this.toTemplate(item));
          });
        });
    },
    toTemplate(obj) {
      let resOjb = {
        diarrhea: this.$helper.ToYesNO(obj.diarrhea),
        normal_stool: this.$helper.ToYesNO(obj.normal_stool),
        constipation: this.$helper.ToYesNO(obj.constipation),
        flatulence: this.$helper.ToYesNO(obj.flatulence),
        stomachache: this.$helper.ToYesNO(obj.stomachache),
        from_stool_frequency: obj.from_stool_frequency,
        to_stool_frequency: obj.to_stool_frequency,
        character: this.CHARACTER_STOOLS.find(
          (item) => item.id == obj.character
        ),

        status: this.$helper.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date,
      };

      if (typeof obj.id != "undefined") resOjb.id = obj.id;

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        diarrhea: this.$helper.ToBoolFromYesNo(template.diarrhea),
        normal_stool: this.$helper.ToBoolFromYesNo(template.normal_stool),
        constipation: this.$helper.ToBoolFromYesNo(template.constipation),
        flatulence: this.$helper.ToBoolFromYesNo(template.flatulence),
        stomachache: this.$helper.ToBoolFromYesNo(template.stomachache),
        from_stool_frequency: template.from_stool_frequency,
        to_stool_frequency: template.to_stool_frequency,
        character: template.character.id,

        status: this.$helper.ToBoolFromYesNo(template.status),
        patient: template.patient,
        date: template.date,
      };
      if (typeof template.id != "undefined") resObj.id = template.id;
      return resObj;
    },

    editItem() {
      let item = this.selectedItems[0];
      this.editedIndex = this.items.indexOf(item);
      this.editedItem = this.toObject(item);
      this.dialog = true;
    },

    DealSavingRespone(response) {
      if (response == true) {
        this.$q.notify({
          message: this.$t("edited"),
          color: "blue",
          icon: "success",
          actions: [{ label: this.$t("close"), color: "white" }],
        });
      } else {
        this.$q.notify({
          message: this.$t("unedited"),
          color: "red",
          icon: "error",
          actions: [{ label: this.$t("close"), color: "white" }],
        });
      }
    },

    async deleteItem() {
      this.$q
        .dialog({
          title: this.$t("confirm"),
          message: this.$t("would_like_delete"),
          cancel: true,
          persistent: true,
        })
        .onOk(async () => {
          let item = this.selectedItems[0];
          const index = this.items.indexOf(item);
          let response = await this.$helper.deleteInstance(
            item,
            "/complaint_request"
          );
          if (response == true) {
            this.items.splice(index, 1);
            this.selectedItems = []
          }

          if (response == true) {
            this.$q.notify({
              message: this.$t("deleted"),
              color: "blue",
              icon: "success",
              actions: [{ label: this.$t("close"), color: "white" }],
            });
          } else {
            this.$q.notify({
              message: this.$t("notdeleted"),
              color: "red",
              icon: "error",
              actions: [{ label: this.$t("close"), color: "white" }],
            });
          }
        })
        .onOk(() => {
          // console.log('>>>> second OK catcher')
        })
        .onCancel(() => {
          // console.log('>>>> Cancel')
        })
        .onDismiss(() => {
          // console.log('I am triggered on both OK and Cancel')
        });
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    async save() {
      let response = await this.$helper.saveInstance(
        this.editedItem,
        "/complaint_request"
      );
      if (response == true) {
        if (this.editedIndex > -1) {
          Object.assign(
            this.items[this.editedIndex],
            this.toTemplate(this.editedItem)
          );
        } else {
          this.items.push(this.toTemplate(this.editedItem));
        }
        this.close();
      }
      this.DealSavingRespone(response);
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

        date: this.$helper.GetCurrentDate(),
        status: false,
        patient: this.patient.id,
      };
      this.editedItem = Object.assign({}, this.defaultItem);
      this.dialog = true;
    },
  },
  components: {
    Complaint,
  },
  mounted: function () {},
};
</script>

<style>
</style>