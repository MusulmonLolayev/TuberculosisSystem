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
          <taking-medicine :takingmedicine="editedItem" />
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
import TakingMedicine from "../editors/taking-medicine";
export default {
  name: "TakingTable",
  data: () => ({
    dialog: false,
    headers: [],
    items: [],
    editedIndex: -1,
    editedItem: {},
    defaultItem: null,
    selectedItems: [],
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
    initialize() {
      this.headers = [
        { label: this.$t("from_date"), field: "fromdate", sortable: false },
        {
          label: this.$t("streptomycin"),
          field: "streptomycin",
        },
        {
          label: this.$t("rifampicin"),
          field: "rifampicin",
        },
        {
          label: this.$t("isoniazid"),
          field: "isoniazid",
        },
        {
          label: this.$t("pyrazinamide"),
          field: "pyrazinamide",
        },
        {
          label: this.$t("ethambutol"),
          field: "ethambutol",
        },

        { label: this.$t("status"), field: "status" },
        { label: this.$t("date"), field: "date" },
      ];
      let patient_id = this.patient.id;
      this.$axios.get("/taking_request/" + patient_id).then((respone) => {
        respone.data.map((item) => {
          this.items.push(this.toTemplate(item));
        });
      });
    },
    toTemplate(obj) {
      let resOjb = {
        fromdate: obj.fromdate,
        streptomycin: this.$helper.ToYesNO(obj.streptomycin),
        rifampicin: this.$helper.ToYesNO(obj.rifampicin),
        isoniazid: this.$helper.ToYesNO(obj.isoniazid),
        pyrazinamide: this.$helper.ToYesNO(obj.pyrazinamide),
        ethambutol: this.$helper.ToYesNO(obj.ethambutol),

        status: this.$helper.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date,
      };

      if (typeof obj.id != "undefined") resOjb.id = obj.id;

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        fromdate: template.fromdate,
        streptomycin: this.$helper.ToBoolFromYesNo(template.streptomycin),
        rifampicin: this.$helper.ToBoolFromYesNo(template.rifampicin),
        isoniazid: this.$helper.ToBoolFromYesNo(template.isoniazid),
        pyrazinamide: this.$helper.ToBoolFromYesNo(template.pyrazinamide),
        ethambutol: this.$helper.ToBoolFromYesNo(template.ethambutol),

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
            "/taking_request"
          );
          if (response == true) {
            this.items.splice(index, 1);
            this.selectedItems = [];
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
        "/taking_request"
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

      if (response == true) {
        this.$q.notify({
          message: this.$t("saved"),
          color: "blue",
          icon: "success",
          actions: [{ label: this.$t("close"), color: "white" }],
        });
      } else {
        this.$q.notify({
          message: this.$t("unsaved"),
          color: "red",
          icon: "error",
          actions: [{ label: this.$t("close"), color: "white" }],
        });
      }
    },
    btnNewItem() {
      this.dialog = true;
      this.defaultItem = {
        fromdate: this.$helper.GetCurrentDate(),
        streptomycin: false,
        rifampicin: false,
        isoniazid: false,
        pyrazinamide: false,
        ethambutol: false,

        date: this.$helper.GetCurrentDate(),
        status: false,
        patient: this.patient.id,
      };
      this.editedItem = Object.assign({}, this.defaultItem);
    },
  },
  components: {
    TakingMedicine,
  },
  mounted: function () {},
};
</script>

<style>
</style>