<template>
  <q-select
    v-model="lang"
    :options="langOptions"
    dense
    borderless
    emit-value
    map-options
    options-dense
    style="min-width: 80px"
  />
</template>

<script>
export default {
  data: function () {
    return {
      lang: this.$i18n.locale,
      langOptions: [
        { value: 'en-us', label: this.$t('lang_en') },
        { value: 'uz', label: this.$t('lang_uz') }
      ]
    }
  },
  watch: {
    lang (lang) {
      localStorage.setItem('lang', lang)
      this.$i18n.locale = lang
    }
  },
  mounted: function () {
    this.lang = localStorage.getItem('lang') || this.$i18n.locale
  }
}
</script>
