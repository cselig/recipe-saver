import random

from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder="../static/dist", template_folder="../static/html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/demo")
def demo():
    return render_template("demo.html")

@app.route("/hello")
def hello():
    return random.choice(['Ciao', 'Hei', 'Salut', 'Hola', 'Hallo', 'Hej'])

@app.route("/get_categories")
def get_categories():
    return jsonify(['mains', 'sides', 'desserts'])

if __name__ == "__main__":
    app.run()
