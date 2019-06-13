from server import db, Recipe

db.drop_all()
db.create_all()

recipes = [
    {
        'name': 'pulled pork',
        'category': 'mains',
        'ingredients': [
            'Pork',
            'BBQ sauce',
        ],
        'instructions': [
            'Put pork in slow cooker',
            'Cook on low for 8hrs',
            'Shred and add sauce',
        ],
    },
    {
        'name': 'salmon',
        'category': 'mains',
        'ingredients': [
            'Salmon',
            'Olive oil',
            'Lemon',
        ],
        'instructions': [
            'Sauce salmon in foil',
            'Cook',
        ],
    },
    {
        'name': 'broccoli',
        'category': 'sides',
        'ingredients': [
            'broccoli',
            'olive oil',
            'lemon',
        ],
        'instructions': [
            'toss broccoli with olive oil, lemon, and salt',
            'roast',
            'season with black pepper',
        ],
    },
    {
        'name': 'cookies',
        'category': 'desserts',
        'ingredients': [
            'lots',
            'of',
            'stuff',
        ],
        'instructions': [
            'make dough',
            'chill dough',
            'bake',
        ],
    },
    # {
    #     'name': '',
    #     'category': '',
    #     'ingredients': [],
    #     'instructions': [],
    # },
]

for recipe in recipes:
    entry = Recipe(**recipe)
    db.session.add(entry)
db.session.commit()
