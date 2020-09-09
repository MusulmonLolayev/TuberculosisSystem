<template>
  <div>
    <q-list>
      <q-item clickable to='/'>
        <q-item-section avatar>
          <q-icon color="primary" name="home" />
        </q-item-section>
        <q-item-section>{{$t('home')}}</q-item-section>
      </q-item>
      <div v-if="show_loggined_div">
        <q-expansion-item
          expand-separator
          icon="list"
          :label="$t('data')"
          >
          <q-list>
            <q-item clickable to='new' style="margin-left:20px">
              <q-item-section avatar>
                <q-icon color="primary" name="person_add_alt_1"/>
              </q-item-section>
              <q-item-section>{{$t('new_patient')}}</q-item-section>
            </q-item>
            <q-item clickable to='patients' style="margin-left:20px">
              <q-item-section avatar>
                <q-icon color="primary" name='people_alt'/>
              </q-item-section>
              <q-item-section>{{$t('my_patients')}}</q-item-section>
            </q-item>
          </q-list>
        </q-expansion-item>
        <q-expansion-item
          expand-separator
          icon="analytics"
          :label="$t('int_analysis')"
          >
          <q-list>
            <q-item clickable to='mining' style="margin-left:20px">
              <q-item-section avatar>
                <q-icon color="primary" name="poll"/>
              </q-item-section>
              <q-item-section>{{$t('data_mining')}}</q-item-section>
            </q-item>
          </q-list>
        </q-expansion-item>
        <q-expansion-item
          expand-separator
          icon="account"
          :label="$t('int_analysis')"
          >
          <q-list>
            <q-item clickable to='mining' style="margin-left:20px">
              <q-item-section avatar>
                <q-icon color="primary" name="poll"/>
              </q-item-section>
              <q-item-section>{{$t('data_mining')}}</q-item-section>
            </q-item>
          </q-list>
        </q-expansion-item>
      </div>
    </q-list>
  </div>
</template>

<script>
export default {
  name: 'EssentialLink',
  computed: {
    show_loggined_div(){
      return this.$store.state.auth.IsLoggined;
    }
  }
}
</script>
