import os

from datetime import date

# Import flask
from flask import Flask, render_template, url_for, redirect, session, request, flash

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



# Default route decorator
@app.route('/<username>')
# Home page route decorator
@app.route('/home/<username>')
# Find all docs from recipes collection on mongodb and assign to recipes variable
# Render home.html template and pass through recipes variable to access on page
def home_two(username):
    username = mongo.db.users.find_one(
        {'username': session['user_session']})
    recipes = mongo.db.recipes.find()
    return render_template('home.html', recipes=recipes, username=username)




# Register page route decorator
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        if existing_user:
            flash("Sorry, that Username is already taken")
            return redirect(url_for('register'))
        register = {
            'username': request.form.get('username').lower(),
            'fname': request.form.get('fname').lower(),
            'lname': request.form.get('lname').lower(),
            'email': request.form.get('email').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(register)

        # Initiate session cookie
        session['user_session'] = request.form.get('username').lower()
        # Flash message to welcome user
        flash('Welcome to Kitchen Craft!')
        # Redirect user to profile page
        return redirect(url_for(
            'profile', username=session['user_session']))
    # Render register page from html template
    return render_template('register.html')


# Login page route decorator
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assign username input to variable if it exists in users collection
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        # Conditional to check if new variable is truthy
        if existing_user:
            # Conditional to ensure password input matches that stored in users collection
            # using werkzeug hashing function
            if check_password_hash(existing_user['password'], request.form.get('password')):
                # Initiate user session
                session['user_session'] = request.form.get('username').lower()
                # Flash message to welcome user
                flash('Welcome, {}'.format(request.form.get('username')))
                # Redirect user to profile page
                return redirect(url_for(
                    'profile', username=session['user_session']))

            # If password doesn't match that stored in users collection
            else:
                # Flash message to tell user that either username or password are incorrect
                flash("Incorrect Username and/or Password")
                # Redirect to login page
                return redirect(url_for('login'))
        # If username doesn't exist
        else:
            # Flash message to tell user that either username or password are incorrect
            flash("Incorrect Username and/or Password")
            # Redirect to login page
            return redirect(url_for('login'))

    # Render login page from html template
    return render_template('login.html')


# Profile page route decorator
@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
    # Get username from current session
    username = mongo.db.users.find_one(
        {'username': session['user_session']})
    # If a valid session exists
    if session['user_session']:
        # Render profile page from html template
        return render_template('profile.html', username=username)
    # If session does not exist
    else:
        # Redirect user to login page
        return redirect(url_for('login'))
        

# Logout route decorator
@app.route('/logout')
def logout():
    # Flash message to alert user ot successful log out
    flash('You have been Logged Out')
    # Specify which session cookie to remove
    session.pop('user_session')
    # Redirect to login page
    return redirect(url_for('login'))


@app.route("/edit_profile/<username>", methods=['GET', 'POST'])
def edit_profile(username):
    username = mongo.db.users.find_one(
        {'username': session['user_session']})
    if request.method == "POST":

        submit = {
            "fname": request.form.get("fname"),
            "lname": request.form.get("lname"),
            "email": request.form.get("email")
        }
        mongo.db.users.update_one({'username': session['user_session']}, {"$set": submit})
        flash("Profile Updated")
        return redirect(url_for('profile', username=session['user_session']))

    
    return render_template("edit_profile.html", username=username)


# Recipes page route decorator
@app.route('/recipes')
def recipes():
    # upload_dates = mongo.db.recipes.find("upload_date")
    # recipes = mongo.db.recipes.find().sort(upload_dates.sort(key=lambda date: datetime.strptime(date, "%d/%m/Y")))
    recipes = mongo.db.recipes.find().sort("upload_date", -1)
    return render_template('recipes.html', recipes=recipes)


@app.route("/add_recipe", methods=['GET', 'POST'])
def add_recipe():
    if request.method == "POST":
        vegetarian = "checked" if request.form.get("vegetarian") else "unchecked"
        vegan = "checked" if request.form.get("vegan") else "unchecked"
        hot = "checked" if request.form.get("hot") else "unchecked"

        now = date.today()
        recipe = {
            "cuisine_name": request.form.get("cuisine_name"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.get("ingredients"),
            "steps": request.form.get("steps"),
            "created_by": session["user"],
            "vegetarian": vegetarian,
            "vegan": vegan,
            "hot": hot,
            "upload_date": now.strftime("%d/%m/%Y")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("You have successfully shared your recipe with our community!")
        return redirect(url_for("recipes"))

    username = mongo.db.users.find_one(
        {'username': session['user_session']})
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    return render_template("add_recipe.html", cuisines=cuisines, username=username)


@app.route("/edit_recipe/<recipe_id>", methods=['GET', 'POST'])
def edit_recipe(recipe_id):

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, cuisines=cuisines)


# Where and how to run app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)