export function setIsRefreshingTokenExpired (state, {status}) {
    state.IsRefreshingTokenExpired = status
}
export function setLangOptions (state) {
    state.LangOptions = [
        { value: 'en-us', label: this.lang.t('lang_en') },
        { value: 'uz', label: this.lang.t('lang_uz') }
      ]
}