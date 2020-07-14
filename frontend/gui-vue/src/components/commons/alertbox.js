export default class AlertBox{
    timeout = 4000
    show = false
    type = ''
    message = ''
    showMessage(message, type='success', timeout=4000){
        this.show = true
        this.message = message
        this.type = type
        this.timeout = timeout
    }
}