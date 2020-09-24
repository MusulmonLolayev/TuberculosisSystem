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
          <others :other="editedItem" />
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
import Others from "../editors/others";

export default {
  name: "OtherTable",
  data: () => ({
    dialog: false,
    selectedItems: [],
    headers: [],
    items: [],
    editedIndex: -1,
    editedItem: {},
    defaultItem: null,
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
        {
          label: this.$t("tolerance"),
          field: "tuberculosis_tolerance",
        },
        {
          label: this.$t("related_disease"),
          field: "related_disease",
        },
        {
          label: this.$t("nausea"),
          field: "nausea",
        },
        {
          label: this.$t("vomiting"),
          field: "vomiting",
        },
        {
          label: this.$t("headache"),
          field: "headache",
        },
        {
          label: this.$t("sweating"),
          field: "sweating",
        },
        {
          label: this.$t("weakness"),
          field: "weakness",
        },
        {
          label: this.$t("allergodermatosis"),
          field: "allergodermatosis",
        },
        {
          label: this.$t("from"),
          field: "from_weight_loss",
        },
        {
          label: this.$t("to"),
          field: "to_weight_loss",
        },
        {
          label: this.$t("coproscopy"),
          field: "coproscopy",
        },
        { label: this.$t("status"), field: "status" },
        { label: this.$t("date"), field: "date" },
      ];
      let patient_id = this.patient.id;
      this.$axios.get("/other_request/" + patient_id).then((respone) => {
        respone.data.map((item) => {
          this.items.push(this.toTemplate(item));
        });
      });
    },
    toTemplate(obj) {
      let resOjb = {
        tuberculosis_tolerance: this.$helper.ToYesNO(
          obj.tuberculosis_tolerance
        ),
        related_disease: this.$helper.ToYesNO(obj.related_disease),
        nausea: this.$helper.ToYesNO(obj.nausea),
        vomiting: this.$helper.ToYesNO(obj.vomiting),
        headache: this.$helper.ToYesNO(obj.headache),
        sweating: this.$helper.ToYesNO(obj.sweating),
        weakness: this.$helper.ToYesNO(obj.weakness),
        allergodermatosis: this.$helper.ToYesNO(obj.allergodermatosis),
        coproscopy: this.$helper.ToYesNO(obj.coproscopy),
        from_weight_loss: obj.from_weight_loss,
        to_weight_loss: obj.to_weight_loss,

        status: this.$helper.ToYesNO(obj.status),
        patient: obj.patient,
        date: obj.date,
      };

      if (typeof obj.id != "undefined") resOjb.id = obj.id;

      return resOjb;
    },
    toObject(template) {
      let resObj = {
        tuberculosis_tolerance: this.$helper.ToBoolFromYesNo(
          template.tuberculosis_tolerance
        ),
        related_disease: this.$helper.ToBoolFromYesNo(template.related_disease),
        nausea: this.$helper.ToBoolFromYesNo(template.nausea),
        vomiting: this.$helper.ToBoolFromYesNo(template.vomiting),
        headache: this.$helper.ToBoolFromYesNo(template.headache),
        sweating: this.$helper.ToBoolFromYesNo(template.sweating),
        weakness: this.$helper.ToBoolFromYesNo(template.weakness),
        allergodermatosis: this.$helper.ToBoolFromYesNo(
          template.allergodermatosis
        ),
        coproscopy: this.$helper.ToBoolFromYesNo(template.coproscopy),
        from_weight_loss: template.from_weight_loss,
        to_weight_loss: template.to_weight_loss,

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
            "/other_request"
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
        "/other_request"
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
        tuberculosis_tolerance: false,
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

        date: this.$helper.GetCurrentDate(),
        status: false,
        patient: this.patient.id,
      };
      this.editedItem = Object.assign({}, this.defaultItem);
      this.dialog = true;
    },
  },
  components: {
    Others,
  },
  mounted: function () {},
};
</script>

<style>
</style>