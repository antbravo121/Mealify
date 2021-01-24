import spoonacular as sp
api = sp.API("ac216317ddc84cdf97d4da95adc97574")

class Recipe:
	def __init__(self, idenfication, title, image):
		self.id = idenfication
		self.title = title
		self.image = image


def get_meal_plan(calories):
	response = api.generate_meal_plan(targetCalories=calories, timeFrame="week")
	data = response.json()

	meals = []

	for days in data["items"]:
		t = days.get("value")
		t = t[:-1]
		inx = t.index("title")
		t = t[inx+8:-1]
		meals.append(t)

	return meals

def get_recipes_by_ingredients(ingredients_input):
	response = api.search_recipes_by_ingredients(ingredients=ingredients_input, number=10, fillIngredients=True)
	data = response.json()

	recipes = []
	for x in data:
		recipes.append(Recipe(x['id'], x['title'], x['image']))

	return recipes













