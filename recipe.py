import database
database.insert('recipes.txt', 'ketchup', 'Tomatoes, sugar, vinegar')
database.insert('recipes.txt', 'mustard', 'Mustard seeds and vinegar')
database.insert('recipes.txt', 'mayo', 'Oil and egg yolk')
mustard_recipe = database.select_one('recipes.txt', 'mustard')
print(mustard_recipe)
