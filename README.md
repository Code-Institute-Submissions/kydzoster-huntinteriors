# Hunt Interiors


<img src="static/images/HUNTINT/mockup.pdf" >

Project Milestone Four - Code Institute

The Hunt Interiors website was developed for Code Institute as a final project.
This website is for a any client who requires an interior and exterior changes 
for their property and moreover it is for the site owner to be able to update and create 
its content without any prior knowledge of websites code using custom made administration tools.

## Table of contents
<!--ts-->

1. [UX](#UX)
    1. [User goals](#User-goals)
    2. [Design choices](#Design-choices)
    3. [Wireframes](#Wireframes)
2. [Features](#Features)
    1. [Accounts](#Accounts)
        1. [Register page](#Register-page)
        2. [Login page](#Login-page)
        3. [Reset password](#Reset-password)
    2. [Tour store](#Tour-store)
        1. [Home page](#Home-page)
        2. [Retreats](#Retreats)
        3. [Retreat details](#Retreat-details)
    3. [Cart](#Cart)
    4. [Checkout](#Checkout)
    5. [Search](#Search)
    7. [Admin page](#Admin-page)
    8. [Features left to implement](#Features-left-to-implement)
3. [Technologies](#Technologies)
    1. [Tools](#Tools)
    2. [Libraries and frameworks](#Libraries-and-frameworks)
    3. [Languages](#Languages)
4. [Testing](#Testing)
      - You can find the [TESTING.md](TESTING.md) file here.
5. [Deployment](#Deployment)
    1. [Instructions](#Instructions)
    2. [Deployment to Heroku](#Deployment-to-Heroku)
    3. [Add static files to AWS s3](#Add-static-files-to-AWS-s3)
6. [Credits](#Credits)
    1. [Media](#Media)
    2. [Code](#Code)
    3. [Acknowledgment](#Acknowledgment)
 <!--te-->

# UX

## User goals
The target audience of Hunt Interiors are:
- People who need interior and exterior changes to their property.
- People who want to buy furniture.
- Homeowners who need a reliable and trustworthy maintenance experts.

User goals:
- Search a product bar allows to search for any furnitures added to shop
- Learn more about the company and offered services
- View recently added furnitures on a homepage
- View recently posted reviews on a homepage
- View My Account to Register a new account
- View My Account to Login with an email or username or login with a facebook or google account
- view My Account and edit your personal details or change a password under My Dashboard
- View My Account to Logout from your profile
- View services to find out services provided by Hunt Interiors
- View Gallery to see uploaded images of completed/delivered projects
- Click on an image to view its description and to view an image upclose/enlarged
- View Shop to see furnitures sold by Hunt Interiors, sorted by categories
- View an Item and its description or to choose a quantity and add to a cart or return back to all furnitures
- After an item has been added to cart view its price and total price, update its quantity or remove it from cart
- Securely check out and receive an email about a successful purchase
- View Testamonials/Reviews and add your own review
- Edit or delete your posted review
- View contact us to see social platforms operated by Hunt Interiors or send a personalised message

## Admin goals
The site owners goals are:
- To have a Site management tools which provide easy to access most relevant CRUD options with good looking overlay
- To be able to edit about us information and pictures from homepage
- To be able to add new services, slides, gallery and furnitures from site management page
- To be able to view Testamonials from website pages and approve or delete them


## Design choices
Hunt Interiors website as an Interior and Exterior designer site should be easy for an eye, but also the one you would remember when visited.

### Fonts
- The font used in this project is [Poppins and Sans](https://fonts.googleapis.com/css?family=Open+Sans:400,600,700|Poppins:300,400,500,600,700).

#### Styling
  - Box shadow in card to give a depth idea and contrast with the background.
  - Scroll effects to give a better experience to users.
  - Icons used are [Themify](https://themify.me/)

### Wireframes
The wireframe developed for this project was built for desktop use, with taking in consideration that mobile users will also use this website.
Wireframe was created in [Balsamiq](https://balsamiq.com/).
  - [Desktop devices](https://github.com/kydzoster/huntinteriors/blob/main/static/images/HUNTINT/mockup.pdf)

# Features

Hunt Interiors contains 7 apps: `accounts`, `bag`, `furnitures`, `gallery`, `home`, `services` and `testaments`.

## Hunt Interiors Base

Hunt Interiors Base holds `nav bar`, `main bar` and `footer`

## Accounts
 The accounts app holds the functionality of `dashboard/profile`, `register`, `login`, `logout` and the `password reset`.

### Dashboard
<p align="center">
<img src="/static/images/HUNTINT/Account/AccountDashboard.png" width="40%">
</p>

  - Dashboard lets you change or update your account/profile information
  - Profile must be completed to be able to buy itms from the shop, notification will be given if profile is incomplete.

### Register page
<p align="center">
<img src="/static/images/HUNTINT/Account/Register.png" width="40%">
</p>

  - Username, name, email and password is required to create an account.
  - Username must be unique.
  - Password should not be short, must contain at least 8 characters and should not be common.
  - As soon as the user creates its username they are redirected to home page.

### Login page
<p align="center">

<img src="/static/images/HUNTINT/Account/Login.png" width="40%">
</p>
  - Login page will ask for a username which can be a username or emailaddress and a password to login.
  - There is also an option to login with facebook or google account

### Forgot Password
  - Step 1: at the login page, under the password you can find the `forgot password?` link in which will lead to a form to add your account email.
  - Step 2: Add the email you registered with to reset the password.
  - Step 3: You will receive an email with a link that will allow you to add a different password sending you to a reset password form.
  - Step 4: Add a new password and confirm it.
  - Step 5: Once the password is set you can login with the new password.

  <img src="/static/images/HUNTINT/Account/PWReset.png">

## Home

  [<img src="/static/images/HUNTINT/UserAction/Home.png">](https://www.youtube.com/watch?v=jWyOR4HXQWc)
  [![Watch the video]<img src="/static/images/HUNTINT/UserAction/Home.png">](https://www.youtube.com/watch?v=jWyOR4HXQWc)
  [![Watch the video](<img src="/static/images/HUNTINT/UserAction/Home.png">)](https://www.youtube.com/watch?v=jWyOR4HXQWc)

## Services
<p align="center">
 <img src="/static/images/readme_images/retreats_page.png" width="40%">
 </p>

  - The retreats page will display all of the retreats.
  - However, the pagination system will only display three destinations per page to not overload the page if there are a large amount of items.

## Gallery  
  - The page that gives the full detail about the retreat as well as the possibility to add it to cart.
  - In addition, the formatting functionality that can be applied by the website admin.
  - The user can also on the top right corner add the destination to cart.

## Shop

<img src="/static/images/readme_images/cart_image.png">

 The cart app gives the user the ability to `view`, `add` and `adjust` the cart as they wish. Including more or less retreats to their trip package.
  - Besides the destination the user will have a card that will allow them to add how many people will go to the trip.
  - `Important`: Since this project is to provide the user to add retreats to card, they will not be able to book the trip. Where in an actual case, once it's paid the booking should have done directly to the business management. Therefore, in the future a book system will be developed to provide a better experience to customers.

## Testimonials

<p align="center">
<img src="/static/images/readme_images/checkout_image.png" width="40%">
</p>

  - The checkout application holds and manipulates the `Stripe` API. In which empowers the overall application with the e-commerce functionality.
  - In this application is developed and performed the forms users who are willing to buy any retreat, to plot their details into the checkout application forms and finalise the purchase.


## Contact Us
  - Under the search application, a simple search functionality is used to find different destinations from the `Destinations` model by the tour title as the key word retrieved.
  - If a user adds one or multiple destinations that is in the database, it will be retrieved and shown on destination page.
  - If the tour title plotted on the search bar doesn't have in the data base, a message will be displayed instead, describing that destination is not yet added in the database.

## Dashboard

<p align="center">
<img src="/static/images/readme_images/four.png" width="40%">
</p>

  - Simple page 404 for when an error occur and give the ability to not lost the user, sending them back to the home page.

## Site Management

<p align="center">
<img src="/static/images/readme_images/admin_login.png" width="40%">
</p>

  - The admin login page was changed by the name of the website.

<p align="center">
<img src="/static/images/readme_images/admin.png" width="40%">
</p>

  - The admin page was separated by three sections:
     - Authentication and Authorization, where the admin can see and manage the users on the website.
     - Checkout, where the admin can see the orders done by the customers.
     - Tour store, where the admin will be able to check and approve comments and see the contacts done by prospects.

<p align="center">
<img src="/static/images/readme_images/wysiwyg.png" width="40%">
</p>

  - The WYSIWYG (what you see is what you get) functionality was implemented as a functionality from a third party application called [Ckeditor](https://ckeditor.com/). Where the normal text editor was changed to add more features such as:
     - Alignment
     - Tables
     - Images
     - Styling
     - Add more html elements
     - And much more.


## Features Left To Implement
  1. Admin page graphs to display data from comments, sales and views.
  2. Booking system to automate sales.
  3. Add multiple images on retreat preview such as horizontal carousel.
  4. Add tutor section for each retreat.
  5. Add real location with maps at the bottom of each retreat detail page.
  6. Add star based review.

# Technologies

## Tools

  - [Atom](https://atom.io/) as an IDE to develop this project.
  - [Stripe](https://stripe.com/ie) to receive payments.
  - [Heroku](https://www.heroku.com/) for hosting the application and deploy.
  - [AWS S3](https://aws.amazon.com/s3/) was used as a cloud service to host static files.
  - [Github](https://github.com/) to share and store code remotely.
  - [Git](https://git-scm.com/) was used to manage version control.
  - [CkEditor](https://ckeditor.com/docs/) was used to better format texts without the need to do within the code.
  - [Sqlite3](https://www.sqlite.org/index.html) a database provided by django for development.
  - [PostgreSQL](https://www.postgresql.org/), a robust database provided by Heroku for production development.
  - [Travis CI](https://travis-ci.org/) for continuous integration and testing.
  - [Canva](https://www.canva.com/) was used to design images on the web.
  - [Balsamiq](https://balsamiq.com/) for the wireframes design.

## Libraries and frameworks

  - [Django](https://www.djangoproject.com/) a high level python web-framework used to design this project.
  - [Bootstrap 4](https://getbootstrap.com/) a CSS library grid used for the development of this site.
  - [FontAwesome](https://fontawesome.com/) for the creation and implementation of icons.
  - [Google fonts](https://fonts.google.com/) to bring custom font styling.
  - [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) a template language for python used to bring logic into templates.
  - [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/#description) used as the Python PostgreSQL adapter.
  - [Jquery](https://jquery.com/) a Javascript library to simplify the code.
  - [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) a library that enables python code to modify AWS service.
  - [AOS](https://michalsnik.github.io/aos/) used to bring animation on scroll.

## Languages

  - This project uses HTML, CSS, Javascript and Python programming languages.


# Testing

The testing information can be found in this separated [Testing](TESTING.md) file.


# Deployment

For the deployment you will need tool as:

  - An IDE such as [Atom](https://atom.io/) or [Visual Studio Code](https://code.visualstudio.com/).
  - Have installed in your machine [Python 3](https://www.python.org/downloads/) and [Git](https://git-scm.com/).

To continue on the process of deployment you should have accounts on the following services:

  - [Stripe](https://stripe.com/ie)
  - [AWS](https://aws.amazon.com/s3/)
  - [Gmail](https://gmail.com)

### Instructions
  1. Download a copy of this repository from the link https://github.com/EliasOPrado/tour-project as a download zip file. Or at your terminal do the following git command:

      ```
      $ git clone https://github.com/EliasOPrado/tour-project
      ```
  2. If you downloaded the project as a zip file, unzip it and add it in your directory.
  3. To not run in some unexpected behaviours during development, a virtual environment is advised to be used before the project be installed in your machine. So create a virtual environment with the command:

      ```
     $ python -m venv venv
      ```
  4. After you already created the virtual environment folder you need to activate it:

      ```
      $ source venv/bin/activate
      ```
  5. Install requirements.txt file.

      ```
      $ pip install -r requirements.txt
      ```
  6. Create an `env.py` file to store environment variable keys.

     ```
     import os

     os.environ.setdefault('SECRET_KEY', '<secrete key>')
     os.environ.setdefault('DATABASE_URL', '<postgres key>')

     """ STRIPE API Keys """
     os.environ.setdefault('STRIPE_PUBLISHABLE', '<stripe publishable key>')
     os.environ.setdefault('STRIPE_SECRET', '<stripe secret key>')

     """ AWS API Keys """
     os.environ.setdefault('AWS_ACCESS_KEY_ID', '<aws access key id>')
     os.environ.setdefault('AWS_SECRET_ACCESS_KEY', '<aws secret access key>')

     """ Email Keys """
     os.environ.setdefault('EMAIL_ADDRESS', '<your email here>')
     os.environ.setdefault('EMAIL_PASSWORD', '<your email password here>')
     ```
  7. Add a git ignore file to not submit sensitive data to Github repository.

     ```
     $ touch .gitignore
     ```
     - Then add the `env.py` to the `.gitignore` file.

     ```
     $ git update-index --assume-unchanged env.py
     ```
     - Depending where the the `env.py` is locate the path will change.

  8. Migrate the models to crete a database template.

      ```
      $ python manage.py migrate
      ```
  9. In this step you will need to create a super user to have access to the admin page.

      ```
      $ python manage.py createsuperuser
      ```
  10. So, after you do all the steps to create a super user you can now run the server.

      ```
      $ python manage.py runserver
      ```
  11. After the server is running locally add the `/admin` path at the end of the url link. It might look like this if you are not running another application.

      ```
      http://127.0.0.1:8000/admin
      ```

### Deployment to Heroku

To make the deployment of this application to `Heroku` you will need to do the following steps.

  1. Signup for [Heroku](https://signup.heroku.com/)
  2. Install [Heroku-CLI](https://devcenter.heroku.com/articles/heroku-cli)
  3. After installing `Heroku toolbelt` add the following code into your termial and login into your account you already create.
     ```
     $ heroku login
      Enter your Heroku credentials.
      Email: your@email.com
      Password (typing will be hidden):
      Authentication successful.
     ```
  4. Save all the requirements into the `requirements.txt` as mentioned before with the command:
     ```
     $ pip freeze > requirements.txt
     ```
  5. Create a file named `Procfile` and add the following config.
     ```
     web: gunicorn main_tour_folder.wsgi
     ```
 6. After all the setup is done `git add .`, `git commit` and `git push` your application to a repository you created on Github.
 7. In your `Heroku`account click new and create new app.
 9. Select your region and create a name for your project.
10. In your `Heroku` settings click `reveal config vars`.
11. Add the following config variables:

| KEY            | VALUE         |
|----------------|---------------|
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |
| AWS_SECRET_ACCESS_KEY | `<your aws secret access key>`  |
| DATABASE_URL| `<your postgres database url>`  |
| EMAIL_ADDRESS| `<your email address>`  |
| EMAIL_PASSWORD | `<your email password>` |
| SECRET_KEY | `<your secret key>`  |
| STRIPE_PUBLISHABLE| `<your stripe publishable key>`  |
| STRIPE_SECRET| `<your stripe secret key>`  |
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |

12. Add a development (postgres) database:
  ```
  $ heroku addons:add heroku-postgresql:dev
    heroku addons:add heroku-postgresql:dev
    Adding heroku-postgresql on deploy_django... done, v13 (free)
    Attached as HEROKU_POSTGRESQL_COPPER_URL
    Database has been created and is available
    ! This database is empty. If upgrading, you can transfer
    ! data from another database with pgbackups:restore.
    Use `heroku addons:docs heroku-postgresql` to view documentation.

  $ heroku pg:promote HEROKU_POSTGRESQL_COPPER_URL
    Promoting HEROKU_POSTGRESQL_COPPER_URL to DATABASE_URL... done
   ```
13. After adding the config into your dashboard add the following commands.
  - `$ heroku login`
  - `heroku git:remote -a test-app-to-deploy`
  - `$ git push heroku master`

14. On your `Heroku` dashboard click on `open app` button and check if the application is running correctly.

### Add static files to AWS s3

1. If there is a need to add your static files to AWS S3 you can follow [this stutorial](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html). 

# Credits

## Media
  - The photos and video used in the project were downloaded from [Pexels](https://www.pexels.com/) and [Pixabay](https://pixabay.com/). Platforms that provides no-copyright media and free downloads.

## Code
  - This application was developed using [StartBootstrap](https://startbootstrap.com/templates/) templates and [snippets](https://startbootstrap.com/snippets/). But during the development good part of the original template and snippets were modified.
  - The 404 page snippet was acquired from [Bootsnipp](https://bootsnipp.com/snippets/).
  - The transparent navigation bar was acquired from [Bootstrapious](https://bootstrapious.com/p/transparent-navbar)
  - The `accounts`, `cart` and `checkout` apps were recycled from the [Code Institute](https://github.com/Code-Institute-Org) lessons but modified to fit with the project purpose.

## Acknowledgment
  - I received inspiration for this project from the [Retreat Guru](https://retreat.guru/) website.



Django-heorku (https://devcenter.heroku.com/articles/django-app-configuration)
Database (https://devcenter.heroku.com/articles/heroku-postgres-import-export)


git push https://git.heroku.com/glacial-eyrie-71049.git