<template>
  <div class="q-pa-md">
    <q-table
      grid
      :title="$t('patients')"
      :data="data"
      :columns="$store.state.common.PatientList_Colunms"
      row-key="name"
      :filter="filter"
      grid-header
      hide-header
      :no-data-label="$t('nothingtoshow')"
      :rows-per-page-label="$t('rows_per_page_label') + ':'"
      :selected-rows-label="$helper.getSelectedString"
      :pagination-label="$helper.get_pagination_label"
    >
      <template v-slot:top-right="props">
        <div class="row">
          <q-btn
            round
            icon="update"
            style="margin-right: 30px; margin-top: 5px"
            @click="updateDate"
          >
            <q-tooltip content-class="bg-accent">{{
              $t("update_data")
            }}</q-tooltip>
          </q-btn>
          <q-input
            dense
            debounce="300"
            v-model="filter"
            :placeholder="$t('search')"
          >
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>
        </div>
      </template>

      <template v-slot:item="props">
        <q-card style="margin: 5px; min-width: 220px">
          <q-card-section>
            <div class="row items-center no-wrap">
              <div class="col">
                <strong>{{
                  props.row.last_name +
                  " " +
                  props.row.first_name[0] +
                  " " +
                  props.row.middle_name[0]
                }}</strong>
              </div>

              <div class="col-auto">
                <q-btn color="grey-7" round flat icon="more_vert">
                  <q-menu cover auto-close>
                    <q-list>
                      <q-item clickable @click="goDetail(props.row)">
                        <q-item-section>{{ $t("detail") }}</q-item-section>
                      </q-item>
                      <q-item clickable @click="removePatient(props.row.id)">
                        <q-item-section>{{ $t("remove") }}</q-item-section>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-btn>
              </div>
            </div>
          </q-card-section>
          <q-separator />
          <q-card-section>
            <table>
              <tr>
                <td>
                  <strong>{{ $t("number") }}:</strong>
                </td>
                <td>{{ props.row.number }}</td>
              </tr>
              <tr>
                <td>
                  <strong>{{ $t("birthday") }}:</strong>
                </td>
                <td>{{ props.row.birthday }}</td>
              </tr>
              <tr>
                <td>
                  <strong>{{ $t("from_date") }}:</strong>
                </td>
                <td>{{ props.row.fromdate }}</td>
              </tr>
              <tr>
                <td>
                  <strong>{{ $t("gender") }}:</strong>
                </td>
                <td>{{ props.row.gender ? $t("male") : $t("female") }}</td>
              </tr>
            </table>
          </q-card-section>
        </q-card>
      </template>
    </q-table>
  </div>
</template>

<script>
export default {
  name: "PatientList",
  data() {
    return {
      filter: "",
      data: [],
    };
  },
  methods: {
    initialize() {
      this.updateDate();
    },
    async removePatient(id) {
      this.$q
        .dialog({
          title: this.$t("confirm"),
          message: this.$t("would_like_delete"),
          cancel: true,
          persistent: true,
        })
        .onOk(async () => {
          let response = await this.$helper.deleteInstance(
            { id: id },
            "/patient_request"
          );
          if (response == true) {
            this.$q.notify({
              message: this.$t("deleted"),
              color: "blue",
              icon: "success",
              actions: [{ label: this.$t("close"), color: "white" }],
            });
            this.data = this.data.filter((item) => item.id != id);
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

    goDetail(patient) {
      this.$store.dispatch("patient/setCurrentPatient", {
        patient: patient,
      });
      this.$router.push("detail");
    },

    updateDate() {
      this.$axios.get("/patient_request").then((response) => {
        this.data = response.data;
      });
    },
  },
  beforeMount() {
    this.initialize();
  },
};
</script>

<style scop>
</style>