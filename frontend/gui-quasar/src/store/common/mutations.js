export function setIsRefreshingTokenExpired(state, { status }) {
    state.IsRefreshingTokenExpired = status
}
export function setLangOptions(state) {
    state.LangOptions = [
        { value: 'en-us', label: this.lang.t('lang_en') },
        { value: 'uz', label: this.lang.t('lang_uz') }
    ]
    state.PatientList_Colunms = [
        {
            name: "fio",
            required: true,
            label: this.lang.t("fio"),
            align: "left",
            field: "name",
            sortable: true,
        },
        {
            name: "number",
            align: "left",
            label: this.lang.t("number"),
            field: "number",
            sortable: true,
        },
        {
            name: "birthday",
            align: "left",
            label: this.lang.t("birthday"),
            field: "birthday",
            sortable: true,
        },
        {
            name: "fromdate",
            align: "left",
            label: this.lang.t("from_date"),
            field: "fromdate",
            sortable: true,
        },
        {
            name: "gender",
            align: "left",
            label: this.lang.t("gender"),
            field: "gender",
            sortable: true,
        },
    ]
}
export function setConnectionStatus(state, { status }) {
    state.IsOnline = status
}