<template>
  <div>
    <q-list bordered class="rounded-borders">
      <q-expansion-item
        expand-separator
        icon="fas fa-id-card-alt"
        :label="$t('init_inf')"
        :caption="title"
        dense
        default-opened
      >
        <div class="row" style="margin-left:40px">
          <patient-component :patient="patient" ref="refPatient" />
          <div class="col" style="margin-bottom:20px">
            <q-btn flat :label="$t('save')" @click="save()" />
            <q-btn flat :label="$t('remove')" @click="Delete()" />
          </div>
        </div>
      </q-expansion-item>

      <q-expansion-item expand-separator icon="live_help" :label="$t('init_questions')" dense>
        <div style="margin:10px">
          <init-questions-table :patient="patient" />
        </div>
      </q-expansion-item>

      <q-expansion-item expand-separator icon="fas fa-diagnoses" :label="$t('primary_diagnose')" dense>
        <div style="margin:10px">
          <primary-table :patient="patient" />
        </div>
      </q-expansion-item>

      <q-expansion-item icon="fas fa-capsules" :label="$t('taking_medicine')">
        <div style="margin:10px">
          <taking-table :patient="patient" />
        </div>
      </q-expansion-item>
      <q-expansion-item icon="fas fa-comment-medical" :label="$t('complaint')">
        <div style="margin:10px">
          <complaint-table :patient="patient" />
        </div>
      </q-expansion-item>
      <q-expansion-item icon="fas fa-burn" :label="$t('blood_analysis')">
        <div style="margin:10px">
          <blood-table :patient="patient" :check_acceptability="check_acceptability"/>
        </div>
      </q-expansion-item>
      <q-expansion-item icon="fas fa-biohazard" :label="$t('other_analysis')">
        <div style="margin:10px">
          <others-table :patient="patient"/>
        </div>
      </q-expansion-item>
    </q-list>
  </div>
</template>

<script>
import PatientComponent from "../components/editors/patient";
import InitQuestionsTable from "../components/list/init-qustions-table";
import PrimaryTable from "../components/list/primary-table";
import TakingTable from "../components/list/taking-table";
import ComplaintTable from "../components/list/complaint-table";
import BloodTable from "../components/list/blood-table";
import OthersTable from "../components/list/others-table";
export default {
  data() {
    return {
      title: "",
      patient: {},
      ranges: [],
    };
  },

  methods: {
    initialize() {
      this.$axios.get('/getaccetableintervals')
      .then(response => {
        this.ranges = response.data
      })
      this.patient = Object.assign({}, this.$store.state.patient.patient);
      if (this.patient.id == null || typeof this.patient.id == "undefined") {
        //this.$router.push('')
        return;
      }
      this.title =
        this.patient.last_name +
        " " +
        this.patient.first_name[0] +
        "." +
        this.patient.middle_name[0] +
        ".";
    },
    async save() {
      let hasError = await this.$refs.refPatient.hasError().then((success) => {
        return success;
      });
      if (!hasError) {
        this.step = 1;
        this.showErrorNotify();
        return;
      }

      // save the patient
      let response = await this.$helper.saveInstance(
        this.patient,
        "/patient_request"
      );
      if (response != true) {
        this.DealSavingRespone(response);
        return;
      }

      this.$q.notify({
        message: this.$t("saved"),
        color: "blue",
        icon: "success",
        actions: [{ label: this.$t("close"), color: "white" }],
      });
    },
    showErrorNotify() {
      this.$q.notify({
        message: this.$t("please_correct_errors"),
        color: "red",
        icon: "error",
        actions: [{ label: this.$t("close"), color: "white" }],
      });
    },
    DealSavingRespone(response) {
      this.$q.notify({
        message: this.$t("unsaved"),
        color: "red",
        icon: "error",
        actions: [{ label: this.$t("close"), color: "white" }],
      });
    },

    async Delete() {
      let id = this.patient.id;
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
          this.$router.go(-1);
        })
        .onCancel(() => {
          // console.log('>>>> Cancel')
        })
        .onDismiss(() => {
          // console.log('I am triggered on both OK and Cancel')
        });
    },
    check_acceptability: function(name, instance){
      return this.$helper.check_acceptability(name, instance, this.ranges)
    },
  },

  beforeMount() {
    this.initialize()
  },
  mounted() {
    //this.initialize();
  },
  meta() {
    return {
      title: this.title,
    };
  },

  components: {
    PatientComponent,
    InitQuestionsTable,
    PrimaryTable,
    TakingTable,
    ComplaintTable,
    BloodTable,
    OthersTable
  },
};
</script>

<style>
</style>