import random

from flask import Flask, render_template, jsonify, request

app = Flask(__name__, static_folder="../static/dist", template_folder="../static/html")

@app.route("/recipes")
@app.route("/hello")
@app.route("/")
def index():
    return render_template("index.html")

def recipe_list():
    return render_template("recipes.html")

@app.route("/get_hello")
def get_hello():
    return random.choice(['hallo', 'bonjour'])

@app.route("/get_categories")
def get_categories():
    return jsonify(['mains', 'sides', 'desserts', 'misc'])

@app.route("/get_recipes")
def get_recipes():
    category = request.args.get('category')
    return jsonify({
        'mains': ['pulled pork', 'salmon'],
        'sides': ['broccoli', 'mashed potatoes'],
        'desserts': ['cookes', 'brownies'],
        'misc': [],
    }[category])

if __name__ == "__main__":
    app.run()
