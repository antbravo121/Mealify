from flask import Flask, escape, request, render_template
from dataapi import get_meal_plan, get_recipes_by_ingredients

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
	if request.method == "POST":
		budget_value = request.form["budgeRange"]
		calorie_value = request.form["calorieRange"]
		meals = get_meal_plan(int(calorie_value))
		if len(meals) > 0:
			return render_template("index.html", 
				sun_b = meals[0], sun_l = meals[1], sun_d = meals[2],
				mon_b = meals[3], mon_l = meals[4], mon_d = meals[5],
				tues_b = meals[6], tues_l = meals[7], tues_d = meals[8],
				wed_b = meals[9], wed_l = meals[10], wed_d = meals[11], 
				thurs_b = meals[12], thurs_l = meals[13], thurs_d = meals[14],
				fri_b = meals[15], fri_l = meals[16], fri_d = meals[17],
				sat_b = meals[18], sat_l = meals[19], sat_d = meals[20])
		else:
			return render_template("index.html")
	else:
		return render_template("index.html")


@app.route("/recipe_finder", methods=["POST", "GET"])
def recipe_finder():

	if request.method == "POST":
		ingredients = request.form["ingredients_value"]
		recipes = get_recipes_by_ingredients(ingredients)

		return render_template("recipe.html", recipes=recipes)
	else:
		return render_template("recipe.html")


if __name__ == "__main__":
	app.run(debug=True)















