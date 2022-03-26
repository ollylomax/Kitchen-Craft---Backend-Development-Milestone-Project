<h1 align="center">Data-Centric-Backend-Development-Milestone-Project (Milestone Project #3)</h1>
<h1 align="center">Olly Lomax</h1>

<h2 align="center"><img src="docs/readmeimages/kitchencraft-readmeheader.png"></h2>

![Responsive Visuals](docs/readmeimages/responsive.png)
# Kitchen Craft Website
I built this website using my knowledge of HTML5, CSS3, JavaScript, jQuery, Materialize, Python, MongoDB and Flask which I have learned from Code Institute during my Diploma in Full Stack Software Development. Kitchen Craft is an imaginary brand that I have created to showcase my knowledge and skills in the aforementioned languages and frameworks with the intention of completing my Data Centric Backend Development Milestone Project.

View the live project [here](https://kitchen-craft.herokuapp.com/).

## UX STRATEGY

### Goals
  - To expand upon my knowledge of HTML5, CSS3, JavaScript and jQuery.
  - To show my knowledge of Python, Flask, MongoDB and Materialize frameworks.
  - To provide a responsive website fulfilling the UX Design philosophy.
  - To provide a website showcasing kitchen products for sale
  - To provide a website with user registration and profile page
  - To provide a website with community driven recipe sharing
  - To provide a website with admin functionality for adding new cuisines
  - To provide a website with superuser functionality for managing admin permissions and bans

### User Stories

    - As a user, I want to easily understand the purpose of the site.

    - As a user, I want to clearly view the website and content on any device.

    - As a user, I want to easily navigate the website so that I can find content quickly.

    - As a user, I want to be able to see what kitchen products are for sale and how much they are.

    - As a user, I want to be able to see all the community shared recipes

    - As a user, I want to be able to search the community shared recipes

    - As a user, I want to be able to see information about the different cuisines of the world

    - As a user, I want to be able to register to the website so that I can share my own recipes

    - As a user, I want to be able to easily return to the website if I encounter a page error

    - As a registered user, I want to be able to log in to my account on the website

    - As a registered user, I want to be able to view my profile, edit my details and change my password

    - As a registered user, I want to be able to add, edit and delete my own recipes

    - As a registered user, I want to be able to see all my recipes on my profile page

    - As an admin user, I want to be able to add, edit and delete cuisines

    - As the superuser, I want to be able to view and search the users page

    - As the superuser, I want to be able to edit admins and bans for users

    - As the superuser, I want to be able to delete users

## UX SCOPE

- ### Planned Features

    - Creating and storing Recipe, Product, Cuisine and User information as collections inside a mongoDB database.
    - Adopting UX Design Philosophy.
    - Navigation links on all pages.
    - Website title and description clearly stating intended purpose.
    - CRUD Functionality.
    - Login/Logout Functionality.
    - Home page with introduction and recipes listed under the chosen Cuisine of the Week.
    - Profile page viewable and editable by registered users, with user created recipes displayed beneath.
    - Change password page, separate from edit profile page, for users to securely change their password with validation.
    - Recipes page viewable and searchable by all users.
    - Add/Edit Recipe pages for registered users to share and edit their own recipes.
    - Products page with images, descriptions and prices viewable by all users.
    - Cuisines page with description, flag and checkbox for Cuisine of the Week viewable by all users with edit/delete buttons only viewable by admin users.
    - Add/Edit Cuisine pages for admin users to create and edit new cuisines as well as delete functionality.
    - Users page viewable and searchable only by the Superuser with editable admins, bans and delete functionality.
    - 404 and 500 error pages caught by flask error handling to direct user back to website.

    ![Scope Table](docs/wireframes/kitchen-craft-scope-table.png)

## UX STRUCTURE

### User Story:
> As a user, I want to easily understand the purpose of the site.

- #### Acceptance Criteria:
    - Kitchen Craft logo displayed top left of navbar.
    - Heading at top of home page with an introduction explaining the website.

 - #### Implementation:
    The logo will be displayed at the top left of the navbar, this will be consistent throughout all pages. An h1 heading will welcome users and a paragraph below, clearly displayed in white text over a coloured background, will outline the exact purpose of the site. A background image behind the h1 header and paragraph will show kitchen related produce/utensils.

### User Story:
> As a user, I want to clearly view the website and content on any device.

- #### Acceptance Criteria:
    The layout of the website is well structured, clearly readable and aesthetically pleasing across all viewports and devices.

- #### Implementation:
    Utilising rows and columns within Materialize frameworks and mobile first design will be used when coding the project and testing will be required to ensure the layout is clear on all devices. No elements should overlap their containers and all items should be responsive so that no elements are too large to display properly. Media will scale to fit all screen sizes with no stretch or distortion.

### User Story:
> As a user, I want to easily navigate the website so that I can find content quickly.

- #### Acceptance Criteria:
    Logo will link to home page on all pages.
    Navigation menu will be displayed on all pages.
    All navigation links will direct to the correct pages.

 - #### Implementation:

    For an **unregistered user**, the navigation menu will consist of:

    Home - home.html
    Products - products.html
    Recipes - recipes.html
    Cuisines - cuisines.html
    Register - register.html
    Login - login.html

    For an **registered user**, the navigation menu will consist of:

    - Home - home.html
    - Products - products.html
    - Recipes - recipes.html
    - Cuisines - cuisines.html
    - Dropdown Menu displaying username consisting of:
        - Profile - profile.html
        - Add Recipe - add_recipe.html
        - Log Out - directs to home.html
    
    For an **admin user**, the navigation menu will consist of:
    
    - Home - home.html
    - Products - products.html
    - Recipes - recipes.html
    - Cuisines - cuisines.html
    - Dropdown Menu displaying username consisting of:
        - Profile - profile.html
        - Add Recipe - add_recipe.html
        - Add Cuisine - add_cuisine.html
        - Log Out - directs to home.html

    For the **Superuser account**, the navigation menu will consist of:
    
    - Home - home.html
    - Products - products.html
    - Recipes - recipes.html
    - Cuisines - cuisines.html
    - Users - users.html
    - Dropdown Menu displaying username consisting of:
        - Profile - profile.html
        - Add Recipe - add_recipe.html
        - Add Cuisine - add_cuisine.html
        - Log Out - directs to home.html
      
    The navigation menu will be visible on all pages. Each navigation item will direct the user to the applicable page. For smaller devices the menu will collapse into a burger menu. When clicked, this menu will expand downwards on the right hand side of the screen displaying the same navigation items. Clicking away from this menu will close it.

### User Story:
> As a user, I want to be able to see what kitchen products are for sale and how much they are.

- #### Acceptance Criteria:
    Products page will be created.
    Products images displayed and scaled to fit all screen sizes with no distortion.
    Product descriptions clearly outlining product benefits
    Product prices stand out
    Indicate to user what the product may be useful for

 - #### Implementation:
    Product images will be selected of sufficient dots per inch to clearly show the product without loss of quality. Descriptions to be thorough enough to encourage sales and prices displayed in both a larger font size and weight. Will also display what foods the applicable item may be useful on, or what recipes they be be useful for.

### User Story:
> As a user, I want to be able to see all the community shared recipes

- #### Acceptance Criteria:
    Recipes page will be created.
    Community recipes will be shown on this page with relevant information
    Dropdown boxes will extend downwards containing the lengthly information

 - #### Implementation:
    A full list of community recipes will be shown on the recipes page from the mongoDB recipes collection with the cuisine they belong to, recipe name, preparation time, cooking time, a step-by-step guide and whether the recipe is vegetarian, vegan and/or hot. They will also show which user shared the recipes and when.

### User Story:
> As a user, I want to be able to search the community shared recipes

- #### Acceptance Criteria:
    A search bar will be displayed at the top of the Recipes page
    A clear header will tell the user that they are able to filter recipes by their query

 - #### Implementation:
    A database index will be created on the recipes collection in MongoDB, allowing users to search by recipe name and cuisine name. When a user types in search criteria and presses the search button (or presses enter) it will return a filtered list of recipes based upon that criteria.

### User Story:
> As a user, I want to be able to see information about the different cuisines of the world

- #### Acceptance Criteria:
    Cuisines page will be created.
    A list of current cuisines will be displayed
    Information about the cuisines will be included

 - #### Implementation:
    Each cuisine will include a country flag and a brief description. The cuisine chosen as the Cuisine of the Week will have a star icon at the top right, with a tooltip to let the user know.

### User Story:
> As a user, I want to be able to register to the website so that I can share my own recipes

- #### Acceptance Criteria:
    Register page will be created.
    A username and password will be required on form submission.
    Additional details such as first and last name as well as email address also required.
    Confirm password field which must match password field.

 - #### Implementation:
    The Register form will capture the username, first name, last name, password and email which when submitted, will all be stored in a MongoDB database collection called users. Each input field will have its own validation including but not limited to; minimum and maximum character limits, character requirements and regular expressions. There will also be a confirm password field as extra validation for the user's protection. Two 'silent' key/values will also be submitted for banned and admin status set to off. Upon a successful registration a session will be initialised and the user will be directed to their profile page with a flash message informing them of successful registration.

### User Story:
> As a user, I want to be able to easily return to the website if I encounter a page error

- #### Acceptance Criteria:
    404 page will be created.
    500 page will be created.
    Both pages will provide error information and a way back to the website.

 - #### Implementation:

    Error handling will be used to catch both 404 and 500 page errors and direct the user to the respective page. This will inform them in detail of the error in question and a link will be provided directing back to the home page.

### User Story:
> As a registered user, I want to be able to log in and log out of my account on the website

- #### Acceptance Criteria:
    Login page will be created.
    Username will be checked against password in a secure way.

 - #### Implementation:
    Username and password will be checked against each other from the mongoDB users collection. If the password does not match, the username does not exist or the user is banned then the user will be informed of this with a flash message. When a user has successfully logged in, a session will be initialised and they will be directed to their profile page with a flash message informing them of successful login. A Log Out button will be displayed to users who are logged in. When clicked this will terminate the session, flash a message informing them of successful log out and direct them to the login page.

### User Story:
> As a registered user, I want to be able to view my profile, edit my details and change my password

- #### Acceptance Criteria:
    - Profile page will be created.
    - Edit profile page will be created.
    - Change password page will be created.
    - Buttons on the profile page will be displayed to edit profile and/or change password which will link to their respective pages and a Sign Out button.

 - #### Implementation:
    The same information that the user registered with will be displayed on the profile page, with the exception of password. The Edit Profile button will link to the respective page where the user can edit First Name, Last Name and Email Address with the same field validation as the registration page. Username changes are not permitted. The Change Password button will direct to the respective page where the user can edit their password. This will have the same validation and confirmation field as the registration page. Upon successful edits of profile or password, a flash message will let the user know it was successful. A cancel button will also be included on each form to return to the profile page. Finally, a Sign Out button will be displayed on the profile page which will terminate the session and return the user to the login page with a successful log out flash message.

### User Story:
> As a registered user, I want to be able to add, edit and delete my own recipes

- #### Acceptance Criteria:
    - Recipe link to be put on navbar dropdown for desktop.
    - Recipe link to be put on mobile navbar.
    - Add Recipe page will be created.
    - Edit Recipe page will be created.
    - Details will be required and validated on form submission
    - A Remove button shown on recipes.


 - #### Implementation:
    An Add Recipe page will be built which will be accessible by a navigation link only visible to logged in users. This will be displayed in the dropdown on the desktop navigation and a standard link in the mobile collapsible menu. The Add Recipe page itself will also be restricted to logged in users. The user will be able to create a recipe from this page by filling in all required fields with validation including but not limited to; minimum and maximum character limits, character requirements and regular expressions. The Cuisine Name field will be a select input with a list of all current cuisines available to choose from. The recipe information will be stored in a MongoDB database collection called recipes. When user has successfully created a recipe, a flash message will alert them of the successful submission and direct them to the recipes page. Submission will also commit two 'silent' key/values to the recipes collection called created_by, which will display either 'You' if you created the recipe or the username of the user if not, and upload date which will be the date of creation. These will both be displayed on each recipe.

    An Edit button will be displayed to users only on the recipes which they have themselves created. This will link to the Edit Recipe page which will have the same field validation as adding a recipe. When user has successfully edited a recipe, a flash message will alert them of the successful edit and direct them to the recipes page.

    A Remove button will be displayed to users only on the recipes which they have themselves created. This will trigger a modal dialog to either confirm the deletion of the recipe, or return to the previous page.

### User Story:
> As a registered user, I want to be able to see all my recipes on my profile page

- #### Acceptance Criteria:
    - Show all recipes created by the user on their Profile page
    - Permit all CRUD functionality as was available on the recipes page

 - #### Implementation:
    A 'Your Recipes' section will be created on the Profile page which will be a filtered version of the mongoDB recipes collection. The username will be the criteria to filter by. The same functionality on the recipes page will be available to the user on their profile page for editing and removing their recipes if desired.

### User Story:
> As an admin user, I want to be able to add, edit and delete cuisines

- #### Acceptance Criteria:
    - Buttons to be created for Add, Edit and Remove Cuisine.
    - Add Cuisine page will be created.
    - Edit Cuisine page will be created.
    - Details will be required and validated on form submission

 - #### Implementation:
    Buttons for Add, Edit and Remove Cuisine will be visible only to admin users. Their respective pages will also be restricted to admin users.

    Add Cuisine buttons will direct to Add Cuisine page where the admin user will be able to create a cuisine by filling in all required fields with validation including minimum and maximum character requirements. There will also be a base64 string input for flag images which will require a valid base64 string. On successful creation of a cuisine the admin user will be directed to the cuisines page with a successful flash message.
    If the admin user selected the Cuisine of the Week box for a new cuisine, then the current Cuisine of the Week will be unselected and replaced with the added cuisine. This will change the Cuisine of the Week recipes listed on the home page.

    The Edit Cuisine buttons will be available for all cuisines irrespective of whether the admin user themselves created them. These will link to the Edit Cuisine page where the admin user will be able to edit the cuisine with the same requirements and validation as creating a cuisine. Upon a successful edit, the admin user will be shown a flash message informing them of successful submission. If the admin user unchecked the current Cuisine of the Week, then the cuisine will not be updated and they will be directed back to the cuisines page with a flash error message informing them of why it failed. If the admin user selected the Cuisine of the Week box during the edit, then the current Cuisine of the Week will be unselected and replaced with the edited cuisine. This will change the Cuisine of the Week recipes listed on the home page.

    The Remove Cuisine buttons will be available for all cuisines irrespective of whether the admin user themselves created them. This will trigger a modal dialog to either confirm the deletion of the cuisine, or return to the cuisines page.

### User Story:
> As the superuser, I want to be able to view and search the users page

- #### Acceptance Criteria:
    Users page will be created.
    Index will be created on Users page.
    A search bar will be displayed at the top of the Users page.

 - #### Implementation:
    The users page will be restricted specifically to the Superuser only and will show a list of all users from the mongoDB users collection. The information displayed will be username, first name and last name. A database index will be created on the users collection in MongoDB, allowing the Superuser to search by user name, first name, last name and email address. When the Superuser types in search criteria and presses the search button (or presses enter) it will return a filtered list of users based upon that criteria.

### User Story:
> As the superuser, I want to be able to edit admins, ban and unban users as well as delete them if necessary

- #### Acceptance Criteria:
    - Admin Yes/No checkbox will be included for each user.
    - Banned Yes/No checkbox will be included for each user.
    - Remove button will be displayed for each user.

 - #### Description:
    Next to the username in the users list there will be an 'Is Admin?' column with a checkbox for each user. Turning the switch on and off will result in an interative update of the is_admin key/value in the mongoDB users collection which was silently submitted on user registration. This will grant or revoke the applicable admin access to the user for whom it was changed.

    Beneath each username in the users list there will be an 'Ban User?' checkbox. Turning the switch on and off will result in an interative update of the is_banned key/value in the mongoDB users collection which was silently submitted on user registration. This will prevent or allow access to the account for whom it was changed.

    Beneath each 'Ban User?' checkbox in the users list is a Remove button. This will trigger a modal dialog to either confirm the deletion of the user, or return to the users page.

## UX SKELETON

- ### Wireframes

    - Home (mobile & desktop)
    ![Home](docs/wireframes/home.png)

    - Recipes (mobile & desktop)
    ![Recipes](docs/wireframes/recipes.png)

    - Products (mobile & desktop)
    ![Products](docs/wireframes/products.png)

    - Cuisines (mobile & desktop)
    ![Cuisines](docs/wireframes/cuisines.png)

    - Register (mobile & desktop)
    ![Register](docs/wireframes/register.png)

    - Log-In (mobile & desktop)
    ![Log In](docs/wireframes/log-in.png)

    - Profile (mobile & desktop)
    ![Profile](docs/wireframes/profile.png)

    - Edit Profile (mobile & desktop)
    ![Edit Profile](docs/wireframes/edit-profile.png)

    - Add Recipe (mobile & desktop)
    ![Add Recipe](docs/wireframes/add-recipe.png)

    - Edit Recipe (mobile & desktop)
    ![Edit Recipe](docs/wireframes/edit-recipe.png)

    - Add Cuisine (mobile & desktop)
    ![Add Cuisine](docs/wireframes/add-cuisine.png)

    - Edit Cuisine (mobile & desktop)
    ![Edit Cuisine](docs/wireframes/edit-cuisine.png)

    - Users (mobile & desktop)
    ![Users](docs/wireframes/users.png)

    - 404 (mobile & desktop)
    ![404](docs/wireframes/404.png)


![base64-expression](https://stackoverflow.com/questions/8571501/how-to-check-whether-a-string-is-base64-encoded-or-not)