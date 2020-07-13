class PrimaryDiagnose {
    template = null
    obj = null
    store
    constructor(store, obj){
        this.store = store
        this.obj = obj
        this.toConvertTemplate()

        // Check the store has Prevelance
        this.store.$store.
    }
    toConvertTemplate(){
        
    }

    toConvertObject(){

    }

    setTemplate(template){
        this.template = template
        this.toConvertObject()
    }

    setObj(obj){
        this.obj = obj
        this.toConvertTemplate()
    }
}