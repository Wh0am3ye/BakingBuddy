function Copier() {
    var measure = document.getElementById("measure-value").value;
    var unitFrom = document.getElementById("fr-unit").option.value;
    var unitTo = document.getElementById("to-unit").option.value;
    var ingredient = document.getElementById("ingredients").option.value;
    if (unitFrom == "fr-ounces" && unitTo == "to-grams") {
        var newValue = measure * 28.3495;
    }
    var box = document.getElementById('user-recipe');
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(newValue + " " + unitTo + " " + ingredient));
    box.appendChild(li);
}