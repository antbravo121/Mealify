var budgetSlider = document.getElementById("budgeRange");
var budgetOutput = document.getElementById("budget_value_display");

budgetOutput.innerHTML = budgetSlider.value;

budgetSlider.oninput = function() {
	budgetOutput.innerHTML = this.value
}

var calorieSlider = document.getElementById("calorieRange");
var calorieOutput = document.getElementById("calorie_value_display");

calorieOutput.innerHTML = calorieSlider.value;

calorieSlider.oninput = function() {
	calorieOutput.innerHTML = this.value
}
