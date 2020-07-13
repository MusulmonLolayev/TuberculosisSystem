export default class MessageBox{
    title = ''
    message = ''
    alert_type = ''
    disagree = null
    agree = null
    dialog = false
    persistent = false
    btnAgree = null 
    btnDisAgree = null
    showMessage(title, message, alert_type='success', persistent=false, btnAgree = null, btnDisAgree = null){
        this.dialog = true
        this.title = title
        this.message = message
        this.alert_type = alert_type
        this.persistent = persistent
        this.btnAgree = btnAgree
        this.btnDisAgree = btnDisAgree
    }
    closeMessage(){
        this.dialog = false
    }
}