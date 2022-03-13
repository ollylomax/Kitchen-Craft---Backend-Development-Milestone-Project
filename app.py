import os

# Import date from datetime module
from datetime import date

# Import flask
from flask import (
    Flask, render_template, url_for, redirect, session, request, flash
)

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
def home():
    """ Function with GET method of rendering home html page. Locate the
        cuisine doc with the cuisine_of_week value of 'yes', target the
        cuisine_name of that doc and use it to filter all recipes. Pass the
        filtered results through to the rendered home page within a variable.
        Also pass through variable for an unfiltered findon cuisines
        collection.
    """
    # Convert cuisines collection to list, find object with the value of
    #   cuisine_of_week set to 'yes' and assign to variable
    find_cuisine_of_week = list(mongo.db.cuisines.find(
        {"cuisine_of_week": "yes"}))
    # Find the cuisine name within above variable by first index and assign to
    #   new variable.
    cuisine_of_week = find_cuisine_of_week[0]['cuisine_name']
    # Find all docs in recipes collection with value of above variable and
    #   assign to recipes variable.
    recipes = mongo.db.recipes.find({"cuisine_name": cuisine_of_week})
    # Find all docs in cuisines collection, sort by cuisines_name 
    #   alphabetically and assign to cuisines variable.
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_name", 1))

    # Render the home.html template and pass through the recipes and cuisines
    #   variables
    return render_template('home.html', recipes=recipes, cuisines=cuisines)


# Register page route decorator
@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Function with GET method of rendering register html page. If method is
        POST then check if the username is already taken. If so, redirect to
        register page with flash, if not then insert doc into users collection,
        flash message, initiate a user session and direct to profile page.
    """
    # Conditional to check if request method is POST
    if request.method == 'POST':
        # Check if username already exists in users collection
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        # If username already exists
        if existing_user:
            # Flash message telling user why registration failed
            flash("Sorry, that Username is already taken")
            # Redirect to register route
            return redirect(url_for('register'))
        # Build dictionary with inputted form fields ready to upload to
        #   collection
        upload = {
            'username': request.form.get('username').lower(),
            'fname': request.form.get('fname').lower(),
            'lname': request.form.get('lname').lower(),
            'email': request.form.get('email').lower(),
            # Use werkzeug hashing function on password input
            'password': generate_password_hash(request.form.get('password')),
            'is_admin': 'no'
        }
        # Insert the built dictionary as a doc into the users collection
        mongo.db.users.insert_one(upload)
        # Initiate session cookie
        session['user_session'] = request.form.get('username').lower()
        # Flash message to welcome user
        flash('Welcome to Kitchen Craft!')
        # Redirect user to profile page passing username as param
        return redirect(url_for(
            'profile', username=session['user_session']))

    # Render the register.html template
    return render_template('register.html')


# Login page route decorator
@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Function with GET method of rendering login html page. If method is
        POST then check if the username input exists in users collection. If
        not, flash message and redirect to login page. If so, check if hashed
        password of existing user matches that of the password input. If not,
        flash message and redirect to login page. If correct, flash message,
        initiate user session and redirect to profile page.
    """
    if request.method == 'POST':
        # Search users collection by username input and assign to variable
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        # Conditional to check if username variable is truthy
        if existing_user:
            # Conditional to ensure password input matches that stored in
            #   users collection using werkzeug hashing function
            if check_password_hash(
                    existing_user['password'], request.form.get('password')):
                # Initiate user session
                session['user_session'] = request.form.get('username').lower()
                # Flash message to welcome user
                flash(f"Welcome, {request.form.get('username')}")
                # Redirect user to profile page passing the username param
                return redirect(url_for(
                    'profile', username=session['user_session']))

            # If password doesn't match that stored in users collection
            else:
                # Flash message to tell user why login failed
                flash("Incorrect Username and/or Password")
                # Redirect to login page
                return redirect(url_for('login'))
        # If username doesn't exist
        else:
            # Flash message to tell user why login failed
            flash("Incorrect Username and/or Password")
            # Redirect to login page
            return redirect(url_for('login'))

    # Render the login.html template
    return render_template('login.html')


# Profile page route decorator with username expected in route
@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
    """ Function requiring username param passed through from route. Check
    for current user session and if one does not exist then redirect to logn
    page. If session exists then render template for profile page.
    """
    # Search users collection by username from session and assign to variable
    username = mongo.db.users.find_one(
        {'username': session['user_session']})
    # If a valid session exists
    if session['user_session']:
        # Render the profile.html page and pass through username variable
        return render_template('profile.html', username=username)
    # If session does not exist
    else:
        # Redirect user to login page
        return redirect(url_for('login'))


# Logout route decorator
@app.route('/logout')
def logout():
    """ Function to remove current user session, inform user that they have
    logged out then redirect to login page.
    """
    # Flash message to tell user of successful log out
    flash('You have been Logged Out')
    # Specify which session cookie to remove
    session.pop('user_session')
    # Redirect to login page
    return redirect(url_for('login'))


# Edit profile page route decorator with username expected in route
@app.route("/edit_profile/<username>", methods=['GET', 'POST'])
def edit_profile(username):
    """ Function with GET method of rendering edit_profile html page passing
        through the username variable. If method is POST then update the doc
        found by searching for username in users collection by inserting built
        dictionary, flash success message and direct to profile page.
    """
    # Search users collection by username from session and assign to variable
    username = mongo.db.users.find_one(
        {'username': session['user_session']})
    # Conditional to check if request method is POST
    if request.method == "POST":
        # Build dictionary with inputted form fields ready to upload to
        #   collection
        upload = {
            "fname": request.form.get("fname"),
            "lname": request.form.get("lname"),
            "email": request.form.get("email")
        }
        # Update the doc assigned to username variable with the insertion of
        #   the built dictionary
        mongo.db.users.update_one(username, {"$set": upload})
        # Flash message telling user of successful update
        flash("Profile Updated")
        # Redirect to profile page passing through the username variable
        return redirect(url_for('profile', username=session['user_session']))
    # Render the edit_profile.html page and pass through username variable
    return render_template("edit_profile.html", username=username)


# Change password page route decorator with username expected in route
@app.route("/change_password/<username>", methods=['GET', 'POST'])
def change_password(username):
    """ Function with GET method of rendering change_password html page passing
        through the username variable. If method is POST then update the doc
        assigned to username variable with the new password assigned to
        new password variable, flash successful change message and direct to
        profile page.
    """
    # Search users collection by username from session and assign to variable
    username = mongo.db.users.find_one(
        {'username': session['user_session']})
    # Conditional to check if request method is POST
    if request.method == "POST":
        # Use werkzeug hashing function on password input and assign to
        #   variable
        new_password = generate_password_hash(request.form.get('password'))
        # Update the doc assigned to username variable with the insertion of
        #   vew password variable
        mongo.db.users.update_one(
            username, {"$set": {'password': new_password}})
        # Flash message telling user of successful password change
        flash("Your Password has been changed")
        # Redirect to profile page passing through the username variable
        return redirect(url_for('profile', username=session['user_session']))
    # Render the change_password.html page and pass through username variable
    return render_template("change_password.html", username=username)


# Recipes page route decorator
@app.route('/recipes')
def recipes():
    """ Function with GET method of rendering recipes html page passing
    through two variables; the recipes variable assigned to all recipes
    with the latest insertions shown first, and the cuisines variable
    assigned to all cuisines in ascending order.
    """
    # Assign variable to a find on all recipes with the latest 
    #   insertions shown first using the parameter $natural sort order
    recipes = mongo.db.recipes.find().sort('$natural', -1)
    # Assign variable to a find on all cuisines sorted by ascending order
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_name", 1))
    # Render the recipes.html page passing both recipes and cuisines variables
    return render_template('recipes.html', recipes=recipes, cuisines=cuisines)


# Search route decorator
@app.route("/search", methods=["GET", "POST"])
def search():
    """ Function to get the user index query from the form input and assign to
    variable. Then perform a find on the recipes collection using that variable
    and assign to a new variable to be passed through to the rendered page.
    """
    # Assign variable to the user index query from form input
    index_query = request.form.get("index_query")
    # Find recipes in the recipes collection using an index text search on the
    #   index query variable and assign to new variable
    recipes = list(mongo.db.recipes.find({"$text": {"$search": index_query}}))
    # Render the recipes.html page passing though the recipes variable
    return render_template("recipes.html", recipes=recipes)


# Add recipe page route decorator
@app.route("/add_recipe", methods=['GET', 'POST'])
def add_recipe():
    """ Function with GET method of rendering add_recipe html page passing
        through the cuisines variable. If method is POST then insert built
        dictionary as a new doc in recipes collection, flash success message
        and redirect to recipes route.
    """
    # Conditional to check if request method is POST
    if request.method == "POST":
        # Conditional expressions to assign variables to either checked or
        #   unchecked depending on user checkbox inputs on form
        vegetarian = "checked" if request.form.get(
            "vegetarian") else "unchecked"
        vegan = "checked" if request.form.get("vegan") else "unchecked"
        hot = "checked" if request.form.get("hot") else "unchecked"
        # Return the current local date from the date object imported from
        #   datetime module
        now = date.today()
        # Build dictionary with inputted form fields ready to upload to
        #   collection
        recipe = {
            "cuisine_name": request.form.get("cuisine_name"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.get("ingredients"),
            "steps": request.form.get("steps"),
            "created_by": session["user_session"],
            "vegetarian": vegetarian,
            "vegan": vegan,
            "hot": hot,
            # Convert date from now variable to specified string format
            "upload_date": now.strftime("%d/%m/%Y")
        }
        # Insert the built dictionary as a doc into the recipes collection
        mongo.db.recipes.insert_one(recipe)
        # Flash success message to user
        flash("You have successfully shared your recipe with our community!")
        # Redirect to recipes route
        return redirect(url_for("recipes"))
    # Assign variable to a find on all cuisines sorted by ascending order
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    # Render add_recipe.html page passing through the cuisines variable
    return render_template("add_recipe.html", cuisines=cuisines)


# Edit recipe page route decorator with recipe_id expected in route
@app.route("/edit_recipe/<recipe_id>", methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """ Function with GET method of rendering edit_recipe html page passing
        through both the recipe and cuisines variables. Assign the recipe
        variable to a search on recipes collection by _id using the recipe_id
        passed through the route. If method is POST then update the doc
        assigned to the recipe variable by inserting built dictionary, flash
        success message and redirect to recipes route.
    """
    # Search recipes collection by _id using the object id from the parameter
    #   passed through the route and assign to variable
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # Conditional to check if request method is POST
    if request.method == "POST":
        # Conditional expressions to assign variables to either checked or
        #   unchecked depending on user checkbox inputs on form
        vegetarian = "checked" if request.form.get(
            "vegetarian") else "unchecked"
        vegan = "checked" if request.form.get("vegan") else "unchecked"
        hot = "checked" if request.form.get("hot") else "unchecked"
        # Return the current local date from the date object imported from
        #   datetime module
        now = date.today()
        # Build dictionary with inputted form fields ready to upload to
        #   collection
        upload = {
            "cuisine_name": request.form.get("cuisine_name"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.get("ingredients"),
            "steps": request.form.get("steps"),
            "created_by": session["user_session"],
            "vegetarian": vegetarian,
            "vegan": vegan,
            "hot": hot,
            "upload_date": now.strftime("%d/%m/%Y")
        }
        # Update the doc assigned to recipe variable with the insertion of
        #   the built dictionary
        mongo.db.recipes.update_one(recipe, {"$set": upload})
        # Flash success message
        flash("Your Recipe has been successfully updated")
        # Redirect to recipes route
        return redirect(url_for("recipes"))
    # Assign variable to a find on all cuisines sorted by ascending order
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    # Render edit_recipe.html page passing through both the recipe and 
    #   cuisines variables
    return render_template(
        "edit_recipe.html", recipe=recipe, cuisines=cuisines)


# Remove recipe route decorator with recipe_id expected in route
@app.route("/remove_recipe/<recipe_id>")
def remove_recipe(recipe_id):
    """ Function to delete the recipe by _id using the object id from
    the parameter passed through the route, flash success message and
    redirect to recipes route.
    """
    # Delete the recipe in recipes collection by _id using the object id from
    #   the recipe_id parameter passed through the route
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    # Flash success message
    flash("Your recipe has been successfully removed")
    # Redirect to recipes route
    return redirect(url_for("recipes"))


# Cuisines page route decorator with default set a None username
@app.route("/cuisines/", defaults={'username': None})
# Cuisines page route decorator with username expected in route
@app.route("/cuisines/<username>")
def cuisines(username):
    """ Function which sets a variable to a search on cuisines collection
    sorted by cuisine_of_week in descending order to display as the top
    iteration on rendered page. If user session is not set to None then
    username variable is set to current session and cuisines html page
    is rendered passing through both cuisines and username variables.
    If user session is set to None then render cuisines html page
    passing through just the cuisines variable.
    """
    # Variable set to all cuisines in cuisines collection sorted by
    #   cuisine_of_week in descending order
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_of_week", -1))
    # Conditional to check if user session is not set to None from route
    if session.get('user_session') is not None:
        # Search users collection by username from session and assign to
        #   variable
        username = mongo.db.users.find_one(
            {'username': session['user_session']})
        # Render cuisines.html page passing through both cuisines and
        #   username variables
        return render_template(
            "cuisines.html", cuisines=cuisines, username=username)
        # Otherwise if session is set to None
    else:
        # Render cuisines.html page passing through cuisines variable
        return render_template("cuisines.html", cuisines=cuisines)


@app.route("/add_cuisine/<username>", methods=["GET", "POST"])
def add_cuisine(username):

    if request.method == "POST":
        # with open(request.form.get('flag'), "rb") as img_file:
        #     my_string = base64.b64encode(img_file.read())

        cuisines = list(mongo.db.cuisines.find())
        if request.form.get('cuisine_of_week'):
            for cuisine in cuisines:
                mongo.db.cuisines.update_one(cuisine, {"$set": {'cuisine_of_week': 'no'}})

        cuisine_of_week = "yes" if request.form.get("cuisine_of_week") else "no"

        upload = {
            'cuisine_name': request.form.get('cuisine_name'),
            'flag': request.form.get('flag'),
            'description': request.form.get('description'),
            'cuisine_of_week': cuisine_of_week
        }
        mongo.db.cuisines.insert_one(upload)
        flash("Your New Cuisine has been Successfully Added to the Database")
        return redirect(url_for('cuisines', username=session['user_session']))

    username = mongo.db.users.find_one(
        {'username': session['user_session']})

    if username['is_admin'] == 'yes':
        return render_template("add_cuisine.html")
    else:
        return redirect(url_for("home"))


@app.route("/edit_cuisine/<username>/<cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(username, cuisine_id):

    username = mongo.db.users.find_one(
        {'username': session['user_session']})
    cuisine = mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})

    if request.method == "POST":

        cuisines = list(mongo.db.cuisines.find())
        dict = list(mongo.db.cuisines.find({"_id": ObjectId(cuisine_id)}))[0]

        if request.form.get('cuisine_of_week'):
            for cuisine in cuisines:
                mongo.db.cuisines.update_one(cuisine, {"$set": {'cuisine_of_week': 'no'}})

        if not request.form.get('cuisine_of_week') and dict['cuisine_of_week'] == 'yes':
            flash('There must always be a Cuisine of the Week')
            return render_template("edit_cuisine.html", cuisine=cuisine, username=username)
        else:
            cuisine_of_week = "yes" if request.form.get("cuisine_of_week") else "no"

        upload = {
            'cuisine_name': request.form.get('cuisine_name'),
            'flag': request.form.get('flag'),
            'description': request.form.get('description'),
            'cuisine_of_week': cuisine_of_week
        }

        mongo.db.cuisines.update_one({"_id": ObjectId(cuisine_id)}, {"$set": upload})
        flash("You have Successfully Updated the Cuisine")
        return redirect(url_for('cuisines', username=session['user_session']))

    if username['is_admin'] == 'yes':
        return render_template("edit_cuisine.html", cuisine=cuisine, username=username)
    else:
        return redirect(url_for("home"))


# Route to remove cuisine from collection
@app.route("/remove_cuisine/<cuisine_id>")
def remove_cuisine(cuisine_id):
    mongo.db.cuisines.delete_one({"_id": ObjectId(cuisine_id)})
    flash("Cuisine removed successfully")
    return redirect(url_for("cuisines"))


@app.route("/users/<username>")
def users(username):

    username = mongo.db.users.find_one(
        {'username': session['user_session']})
    users = mongo.db.users.find().sort("username", 1)

    if username == list(mongo.db.users.find({"is_superuser": {"$exists": True}}))[0]:
        return render_template("users.html", username=username, users=users)
    else:
        return redirect(url_for("home"))


@app.route("/edit_admin/<user_id>", methods=['GET', 'POST'])
def edit_admin(user_id):

    if request.method == "POST":

        is_admin = "yes" if request.form.get('is_admin') else "no"

        upload = {
            "is_admin": is_admin
        }

        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": upload})
        flash("Admins Updated")
        return redirect(url_for('users', username=session['user_session']))

    return redirect(url_for('users', username=session['user_session']))


@app.route("/remove_user/<user_id>")
def remove_user(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    flash("User has been permanently removed from the Database")
    return redirect(url_for('users', username=session['user_session']))


# Where and how to run app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
