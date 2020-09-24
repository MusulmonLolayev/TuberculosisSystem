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
          <blood-analysis :bloodanalysis="editedItem" :check_acceptability="check_acceptability"/>
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
import BloodAnalysis from '../editors/blood-analysis'

export default {
  name: "BloodTable",
  data: () => ({
    dialog: false,
    headers: [],
    items: [],
    editedIndex: -1,
    editedItem: {},
    defaultItem: null,
    selectedItems: [],
  }),
  props: ["patient", "check_acceptability"],
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
        {
          label: this.$t("er"),
          field: "er",
        },
        {
          label: this.$t("leyk"),
          field: "leyk",
        },
        {
          label: this.$t("hb"),
          field: "hb",
        },
        {
          label: this.$t("color"),
          field: "color",
        },
        {
          label: this.$t("pya"),
          field: "pya",
        },
        {
          label: this.$t("sya"),
          field: "sya",
        },
        {
          label: this.$t("eoz"),
          field: "eoz",
        },
        {
          label: this.$t("lf"),
          field: "lf",
        },
        {
          label: this.$t("mon"),
          field: "mon",
        },
        {
          label: this.$t("coe"),
          field: "coe",
        },
        {
          label: this.$t("act"),
          field: "act",
        },
        {
          label: this.$t("alt"),
          field: "alt",
        },
        { label: this.$t("status"), field: "status" },
        { label: this.$t("date"), field: "date" },
      ];

      let patient_id = this.patient.id;
      this.$axios.get("/blood_request/" + patient_id).then((respone) => {
        respone.data.map((item) => {
          this.items.push(this.toTemplate(item));
        });
      });
    },
    toTemplate(obj) {
      let resOjb = {
        er: obj.er,
        leyk: obj.leyk,
        hb: obj.hb,
        color: obj.color,
        pok: obj.pok,
        pya: obj.pya,
        sya: obj.sya,
        eoz: obj.eoz,
        lf: obj.lf,
        mon: obj.mon,
        coe: obj.coe,
        act: obj.act,
        alt: obj.alt,

        status: this.$helper.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date,
      };

      if (typeof obj.id != "undefined") resOjb.id = obj.id;

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        er: template.er,
        leyk: template.leyk,
        hb: template.hb,
        color: template.color,
        pok: template.pok,
        pya: template.pya,
        sya: template.sya,
        eoz: template.eoz,
        lf: template.lf,
        mon: template.mon,
        coe: template.coe,
        act: template.act,
        alt: template.alt,

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
    async deleteItem(item) {
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
            "/blood_request"
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
    async save() {
      let response = await this.$helper.saveInstance(
        this.editedItem,
        "/blood_request"
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
        er: 0,
        leyk: 0,
        hb: 0,
        color: 0,
        pok: 0,
        pya: 0,
        sya: 0,
        eoz: 0,
        lf: 0,
        mon: 0,
        coe: 0,

        date: this.$helper.GetCurrentDate(),
        status: false,
        patient: this.patient.id,
      };
      this.editedItem = Object.assign({}, this.defaultItem);
      this.dialog = true;
    },
  },
  components: {
    BloodAnalysis,
  },
  mounted: function () {},
};
</script>

<style>
</style>