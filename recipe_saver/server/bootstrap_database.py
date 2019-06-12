from server import db, Recipe

db.drop_all()
db.create_all()

recipes = {
    'mains': ['pulled pork', 'salmon'],
    'sides': ['broccoli', 'mashed potatoes'],
    'desserts': ['cookes', 'brownies'],
    'misc': ['pancakes'],
}
for category, recipe_list in recipes.items():
    for recipe in recipe_list:
        entry = Recipe(name=recipe, category=category)
        db.session.add(entry)
db.session.commit()
