from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql


app = Flask(__name__, static_folder="../static/dist", template_folder="../static/html")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/recipe_dev' # 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    ingredients = db.Column(postgresql.ARRAY(db.String()))
    instructions = db.Column(postgresql.ARRAY(db.String()))

    def __repr__(self):
        return '<Recipe %r>' % self.name


@app.route('/recipe')
@app.route('/recipes')
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_categories")
def get_categories():
    return jsonify([x.category for x in db.session.query(Recipe.category).distinct()])

@app.route("/get_recipes")
def get_recipes():
    category = request.args.get('category')
    return jsonify([x.name for x in Recipe.query.filter_by(category=category).all()])

if __name__ == "__main__":
    app.run()
