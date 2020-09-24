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
          <primary-diagnose :primarydiagnose="editedItem" />
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
import PrimaryDiagnose from "../editors/primary-diagnose";

export default {
  data: () => ({
    dialog: false,
    headers: [],
    items: [],
    selectedItems: [],
    editedIndex: -1,
    editedItem: {},
    defaultItem: null,
    CLINICAL_FORMS: [],
    LOCALIZATIONS: [],
    PREVALENCES: [],
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
          label: this.$t("clinical_form_of_tuberculosis"),
          field: (row) => row.clinicalform.name,
        },
        {
          label: this.$t("localization"),
          field: (row) => row.localization.name,
        },
        {
          label: this.$t("prevalence"),
          field: (row) => row.prevalence.name,
        },
        {
          label: this.$t("infiltration"),
          field: "infiltration",
        },
        { label: this.$t("decay"), field: "decay" },
        { label: this.$t("seeding"), field: "seeding" },
        { label: this.$t("resorption"), field: "resorption" },
        { label: this.$t("compaction"), field: "compaction" },
        { label: this.$t("scarring"), field: "scarring" },
        { label: this.$t("calcification"), field: "calcification" },
        { label: this.$t("bk"), field: "bk" },
        { label: this.$t("status"), field: "status" },
        { label: this.$t("date"), field: "date" },
      ];
      await this.$axios.get("/clinicalforms").then((respone) => {
        this.CLINICAL_FORMS = respone.data;
      });

      await this.$axios.get("/localization").then((respone) => {
        this.LOCALIZATIONS = respone.data;
      });

      await this.$axios.get("/prevalence").then((respone) => {
        this.PREVALENCES = respone.data;
      });

      let patient_id = this.patient.id;
      this.$axios.get("/primary_request/" + patient_id).then((respone) => {
        //console.log(respone);
        respone.data.map((item) => {
          this.items.push(this.toTemplate(item));
        });
      });
    },
    toTemplate(obj) {
      let resOjb = {
        clinicalform: this.CLINICAL_FORMS.find(
          (item) => item.id == obj.clinicalform
        ),
        localization: this.LOCALIZATIONS.find(
          (item) => item.id == obj.localization
        ),
        prevalence: this.PREVALENCES.find((item) => item.id == obj.prevalence),
        infiltration: this.$helper.ToYesNO(obj.infiltration),
        decay: this.$helper.ToYesNO(obj.decay),
        seeding: this.$helper.ToYesNO(obj.seeding),
        resorption: this.$helper.ToYesNO(obj.resorption),
        compaction: this.$helper.ToYesNO(obj.compaction),
        scarring: this.$helper.ToYesNO(obj.scarring),
        calcification: this.$helper.ToYesNO(obj.calcification),
        bk: this.$helper.ToPlusMinus(obj.bk),
        status: this.$helper.ToYesNO(obj.status),
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
        infiltration: this.$helper.ToBoolFromYesNo(template.infiltration),
        decay: this.$helper.ToBoolFromYesNo(template.decay),
        seeding: this.$helper.ToBoolFromYesNo(template.seeding),
        resorption: this.$helper.ToBoolFromYesNo(template.resorption),
        compaction: this.$helper.ToBoolFromYesNo(template.compaction),
        scarring: this.$helper.ToBoolFromYesNo(template.scarring),
        calcification: this.$helper.ToBoolFromYesNo(template.calcification),
        bk: this.$helper.ToBoolFromPlusMinus(template.bk),
        status: this.$helper.ToBoolFromYesNo(template.status),
        patient: template.patient,
        date: template.date,
        id: template.id,
      };
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
          let deletedItem = this.selectedItems[0];

          const index = this.items.indexOf(deletedItem);
          let response = await this.$helper.deleteInstance(
            deletedItem,
            "/primary_request"
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
        "/primary_request"
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

        date: this.$helper.GetCurrentDate(),
        status: false,
        patient: this.patient.id,
      };
      this.editedItem = Object.assign({}, this.defaultItem);
    },
  },
  components: {
    PrimaryDiagnose,
  },
  mounted: function () {},
};
</script>