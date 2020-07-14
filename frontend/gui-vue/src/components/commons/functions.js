class Helper{
    ToYesNO(value) {
        return value == true ? "Yes" : "No";
    }
    ToBoolFromYesNo(value) {
        return value == "Yes";
    }
    ToPlusMinus(value) {
        return value == true ? "+" : "-";
    }
    ToBoolFromPlusMinus(value) {
        return value == "+";
    }
}

export default {Helper}