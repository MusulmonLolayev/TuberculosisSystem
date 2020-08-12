export default {

    message_types: {
        success: 'success',
        error: 'error'
    },

    ToYesNO(value) {
        return value == true ? "Yes" : "No";
    },
    ToBoolFromYesNo(value) {
        return value == "Yes";
    },
    ToPlusMinus(value) {
        return value == true ? "+" : "-";
    },
    ToBoolFromPlusMinus(value) {
        return value == "+";
    },
    GetCurrentDate() {
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();
        
        today = yyyy + '-' + mm + '-' + dd;
        return today
    }
}