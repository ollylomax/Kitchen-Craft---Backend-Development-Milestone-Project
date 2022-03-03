import os

# Import flask
from flask import Flask, render_template, url_for

# Wire up flask with mongodb
from flask_pymongo import PyMongo

# Render objectid from mongodb docs
from bson.objectid import ObjectId

# Import env file only if path exists
if os.path.exists('env.py'):
    import env

# Import werkzeug security helpers for hashing and salting passwords
from werkzeug.security import generate_password_hash, check_password_hash

# Create instance of flask
app = Flask(__name__)

# Configure database name
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
# Configure connection string
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
# Get secret key
app.secret_key = os.environ.get('SECRET_KEY')

# Create instance of pymongo and pass in flask app object
mongo = PyMongo(app)

# Default route decorator
@app.route('/')
# Home page route decorator
@app.route('/home')
# Find all docs from recipes collection on mongodb and assign to recipes variable
# Render home.html template and pass through recipes variable to access on page
def home():
    recipes = mongo.db.recipes.find()
    return render_template('home.html', recipes=recipes)

# Register page route decorator
@app.route('/register', methods=['GET', 'POST'])
# Render register page from html template
def register():
    return render_template('register.html')


# Where and how to run app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)