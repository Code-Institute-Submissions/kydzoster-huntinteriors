# Hunt Interiors.

<p align="center">
<img src="/static/images/HUNTINT/desktop.gif">

<img src="/static/images/HUNTINT/mobile.gif" width="40%">
</p>

Click [LiveSite](https://glacial-eyrie-71049.herokuapp.com/) to open Hunt Interiors Milestone Project.


The Hunt Interiors website was developed for Code Institute as a final project.
This website is for any client who requires an interior and exterior changes for 
their property and also for the site owner to be able to update and create its content 
without any prior knowledge of websites code using custom made administration tools.

## Table of contents
<!--ts-->

1. [UX](#UX)
    1. [User goals](#User-goals)
    2. [Admin goals](#Admin-goals)
    3. [Design choices](#Design-choices)
    4. [Wireframe](#Wireframe)
2. [Features](#Features)
    1. [Accounts](#Accounts)
        1. [Register page](#Register-page)
        2. [Login page](#Login-page)
        3. [Reset password](#Reset-password)
    2. [Home](#Home)
    3. [Services](#Services)
    4. [Gallery](#Gallery)
    5. [Shop](#Shop)
    6. [Testimonials](#Testimonials)
    7. [Contact Us](#Contact-Us)
    8. [Dashboard](#Dashboard)
    9. [Site Management](#Site-Management)
        1. [Add Services](#Add-Services)
        2. [Add Slides](#Add-Slides)
        3. [Add to Gallery](#Add-to-Gallery)
        4. [Add Products](#Add-Products)
        5. [Review Testaments](#Review-Testaments)
    10. [Features left to implement](#Features-left-to-implement)
3. [Technologies](#Technologies)
    1. [Tools](#Tools)
    2. [Libraries and frameworks](#Libraries-and-frameworks)
    3. [Languages](#Languages)
4. [Testing](#Testing)
5. [Deployment](#Deployment)
    1. [Instructions](#Instructions)
    2. [Deployment to Heroku](#Deployment-to-Heroku)
6. [Credits](#Credits)
    1. [Media](#Media)
    2. [Code](#Code)
    3. [Acknowledgment](#Acknowledgment)
 <!--te-->

# UX

## User goals
The target audience of Hunt Interiors are:
- People who need interior and exterior changes to their property.
- People who want to buy hand-made furniture created by Hunt Interiors.
- Homeowners who need reliable and trustworthy maintenance experts.

User goals:
- As a user I should be able to search a product from the shop when typing into a searchbar
- As a user I should be able to learn more about the company and offered services
- As a user I should be able to view recently added furniture on a homepage
- As a user I should be able to view recently posted reviews on a homepage
- As a user I should be able to view My Account to Register a new account
- As a user I should be able to view My Account to Login with an email or username or login with a Facebook or Google account
- As a user I should be able to view My Account and edit my personal details or change a password under My Dashboard
- As a user I should be able to view My Account to Logout from my profile
- As a user I should be able to view services to find out services provided by Hunt Interiors
- As a user I should be able to view Gallery to see uploaded images of completed/delivered projects
- As a user I should be able to click on an image to view its description and to view an image up-close/enlarged
- As a user I should be able to view Shop to see furniture sold by Hunt Interiors, sorted by categories
- As a user I should be able to view an Item and its description or to choose a quantity and add to a cart or return to all products
- As a user I should be able to add a product to cart view its price and total price, update its quantity or remove it from cart
- As a user I should be able to securely check out and receive an email about a successful purchase
- As a user I should be able to view Testimonials/Reviews and add new review about the services or purchased products
- As a user I should be able to edit or delete my posted reviews
- As a user I should be able to view Contact Us page to see social platforms operated by Hunt Interiors or send a personalised message

## Admin goals
The site owners goals are:
- As an admin I should be able to have a Site management tools which provide easy to access most relevant CRUD options with a good looking overlay
- As an admin I should be able to edit `About Us` information and pictures from the homepage
- As an admin I should be able to add new services, slides, gallery and furniture from the site management page or edit them from their current location
- As an admin I should be able to view Testimonials from website pages and approve or delete them


## Design choices
Hunt Interiors website as an Interior and Exterior designer site should be easy for an eye, but also the one you would remember when visited.

#### Fonts
- The font used in this project is [Poppins and Sans](https://fonts.googleapis.com/css?family=Open+Sans:400,600,700|Poppins:300,400,500,600,700).

#### Styling
  - Box shadow in card to give a depth idea and contrast with the background.
  - Scroll effects to give a better experience to users.
  - Icons used are [Themify](https://themify.me/)

## Wireframes
The wireframe developed for this project was built for desktop use, with taking in consideration that mobile users will also use this website.
The wireframe was created in [Balsamiq](https://balsamiq.com/).
  - [Desktop devices](https://github.com/kydzoster/huntinteriors/blob/main/static/images/HUNTINT/mockup.pdf)

# Features

Hunt Interiors contains 7 apps: `accounts`, `bag`, `furnitures`, `gallery`, `home`, `services` and `testaments`.

## Accounts
 The accounts app holds the functionality of `dashboard/profile`, `register`, `login`, `logout` and the `password reset`.

### Dashboard
<p align="center">
<img src="/static/images/HUNTINT/Account/AccountDashboard.png" width="40%">
</p>

  - Dashboard lets you change or update your account/profile information
  - Profile must be completed to be able to buy products from the shop, a notification will be given and redirect will be initiated if the profile is incomplete.

### Register page
<p align="center">
<img src="/static/images/HUNTINT/Account/Register.png" width="40%">
</p>

  - Username, name, email and password are required to create an account.
  - Username must be unique.
  - Password should not be short, must contain at least 8 characters and should not be common.
  - As soon as the user creates its username they are redirected to the home page.

### Login page
<p align="center">

<img src="/static/images/HUNTINT/Account/Login.png" width="40%">
</p>
  - Login page will ask for a username which can be a username or emailaddress and a password to login.
  - There is also an option to log in with Facebook or Google account

### Forgot Password
  - Step 1: at the login page, under the password you can find the `forgot password?` link in which will lead to a form to add your account email.
  - Step 2: Add the email you registered with to reset the password.
  - Step 3: You will receive an email with a link that will allow you to add a different password sending you to a reset password form.
  - Step 4: Add a new password and confirm it.
  - Step 5: Once the password is set you can log in with the new password.

  <img src="/static/images/HUNTINT/Account/PWReset.png">

## Home
The Home app holds the functionality for `Title`, `Slides`, `Management` and `Contact Us`.

Click [Here](https://www.youtube.com/watch?v=jWyOR4HXQWc) to view a video of the Home page

<p align="center">
  <img src="/static/images/HUNTINT/UserAction/Home.png" width="40%">
</p>


## Services
The Services app holds the functionality for `Services`.

<p align="center">
 <img src="/static/images/HUNTINT/UserAction/Services.png" width="40%">
 </p>


## Gallery  
The Gallery app holds the functionality for `Gallery`.

Click [Here](https://www.youtube.com/watch?v=CPjyrHFvViA) to view a video of the Gallery page

<p align="center">
 <img src="/static/images/HUNTINT/UserAction/Gallery.png" width="40%">
 </p>

  - Gallery can be viewed in three sections `All Gallery`, `Interiors` and `Exteriors`
  - Each picture can be viewed separately to find out a short description of a work accomplished in the picture.

## Shop
The bag app holds the functionality for `bag`, `checkout`, `search` and `invoice`.

Click [Here](https://www.youtube.com/watch?v=QXFZefb8Mi8) to view a video of the Shop page

<p align="center">
 <img src="/static/images/HUNTINT/UserAction/Shop.png" width="40%">
 </p>

 - Shop is separated into 5 categories: `All Furnitures`, `Bed`, `Sofa`, `Chair` and `Table`.
 - Client can also search for a product using a search a product bar, this search bar is a global and can be viewed from any page.
 - To view an Item need to click on View Item, it will show product details, product image and a short description
 - Potential buy can select a quantity and view a product in full scale when clicked on it.
 - Once the product is added to cart/bag it can be viewed in Shopping cart, where the client can change its quantity or delete it from a cart.
 - when the client is ready to checkout he will be directed to Stripe payment section, however,
  if the client has not updated his details he will be directed to his profile account
 - once payment has been made, the client will receive a notification of a successful payment and an email sent to his registered email address.

## Testimonials
The Testaments app holds the functionality for `testaments` and `testament review`.

Click [Here](https://www.youtube.com/watch?v=5ervA6jnC80) to view a video of the Testimonials page

<p align="center">
 <img src="/static/images/HUNTINT/UserAction/Testamonials.png" width="40%">
 </p>

 - Client can add a review of services received by Hunt Interiors, 
 however, his review will have to be approved by the site admin to view it in Testimonials page.

## Contact Us
Contact Us is a part of the Home app.

Click [Here](https://www.youtube.com/watch?v=rxGJX9mkcgY) to view a video of the Contact Us page
  
<p align="center">
 <img src="/static/images/HUNTINT/UserAction/Contact.png" width="40%">
 </p>

 - Client can send a personalised message, email to Hunt Interiors.
 
## Dashboard
The Dashboard is a part of the Account app.

<p align="center">
 <img src="/static/images/HUNTINT/UserAction/Dashboard.png" width="40%">
 </p>

  - Dashboard contains user profile information and an ability to edit it and change a password

## Site Management
  
  <p align="center">
 <img src="/static/images/HUNTINT/AdminActions/Management.png" width="40%">
 </p>

 - Site Admin can have easy to use basic CRUD functionality for `Services`, `Shop`, `Gallery`, `Testimonials` and `About Us and Slides`

 ### Add Services
 Click [Here](https://www.youtube.com/watch?v=U0OZZipW0EI) to view a video of the Add Services page
  
<p align="center">
  <img src="/static/images/HUNTINT/AdminActions/add-services.png" width="40%">
</p>

 ### Add Slides
 Click [Here](https://www.youtube.com/watch?v=fWLdaiME3hI) to view a video of the Add Slides and About us page
  
<p align="center">
  <img src="/static/images/HUNTINT/AdminActions/add-slides.png" width="40%">
</p>

 ### Add to Gallery
 Click [Here](https://www.youtube.com/watch?v=H09dw3Uu10g) to view a video of the Add to Gallery page
  
<p align="center">
  <img src="/static/images/HUNTINT/AdminActions/add-gallery.png" width="40%">
</p>

 ### Add Products
 Click [Here](https://www.youtube.com/watch?v=hanelVey-G4) to view video of the Add Products page
  
<p align="center">
  <img src="/static/images/HUNTINT/AdminActions/add-product.png" width="40%">
</p>

 ### Review Testaments
 Click [Here](https://www.youtube.com/watch?v=hQKI5xxYAn8) to view video of the Review Testaments page
  
<p align="center">
  <img src="/static/images/HUNTINT/AdminActions/review.png" width="40%">
</p>

## Features Left To Implement
  1. Add star-based reviews for each Service, currently, there is a simple version of revies aka Testimonials.
  2. Add most bought furniture from the shop, currently, there are only recently added products.
  3. Service Level agreement, Policy/Privacy Terms acknowledgement during checkout/registration process.
  4. Allow users to view their reviews from their Dashboard.
  5. Save the purchased furniture history in their Dashboard.
  6. Implement a live feed from the Hunt Interiors Facebook and Instagram on a sidebar.
  7. Implement automated testing
  8. Add an option to gallery to view it as a full-screen carousel

# Technologies

## Tools

  - [GitPod](https://gitpod.io/) as an IDE to develop this project.
  - [VSCode](https://code.visualstudio.com/) as an IDE to develop this project using localhost for testing purposes
  - [Stripe](https://stripe.com/) to receive payments.
  - [Heroku](https://www.heroku.com/) for hosting the application and deploy.
  - [Github](https://github.com/) to share and store code remotely.
  - [Balsamiq](https://balsamiq.com/) for the wireframes design.

## Libraries and frameworks

  - [Django](https://www.djangoproject.com/) a high level python web-framework used to design this project.
  - [Bootstrap 4](https://getbootstrap.com/) a CSS library grid used for the development of this site.
  - [Themify](https://themify.me/) for the creation and implementation of icons.
  - [Slick](https://kenwheeler.github.io/slick/) for the carousel and slider
  - [Google fonts](https://fonts.google.com/) for custom font styling.
  - [Decouple](https://pypi.org/project/python-decouple/) for secrets as env

## Languages

  - This project uses HTML, CSS, Javascript and Python programming languages.


# Testing

I have used Django Unit testing for urls.py, to activate it use ```python manage.py test app_name```

<p align="center">
  <img src="/static/images/HUNTINT/tests.png" width="80%">
</p>

- On mobile phones, I have deactivated slider in home page for About Us section and image for Testimonials section.
- As a payment method you can use 42's continually on all fields except email and postcode
- I had to add `!DOCTYPE html` inside each html document before the actual html code, otherwise it gives `doctype must be declared` error when using GitPod

# Deployment

### Instructions
  1. Open https://github.com/kydzoster/huntinteriors, hit the green Gitpod button
  2. Run `pip install -r requirements.txt` in the command line
  3. Migrate the models `python manage.py makemigrations` and then `python manage.py migrate`
  4. Create superuser `python manage.py createsuperuser`
  5. Run Server `python manage.py runserver`, because DB is not being shared you will have to populate your DB yourself, you can do that through Django admin or Site Management under the My Account.


### Deployment to Heroku

To make the deployment of this application to `Heroku` you will need to do the following steps.

  1. Signup for [Heroku](https://signup.heroku.com/)
  2. Install [Heroku-CLI](https://devcenter.heroku.com/articles/heroku-cli)
  3. In command line type `heroku login -i` enter email and password when prompted
  4. Create a file named `Procfile` and add the following code `release: python manage.py migrate && python manage.py loaddata initial_data.json` then on the next line add `web: gunicorn hunt_interiors.wsgi`
  5. Save all the requirements by running `pip freeze > requirements.txt` in the command line
  6. After all the setup is done run `git add .`, `git commit` and `git push`
  7. In your `Heroku`account click new and create a new app.
  9. Select your region and create a name for your project.
  10. In your `Heroku` settings click `reveal config vars`.
  11. Add the following config variables:

| KEY            | VALUE         |
|----------------|---------------|
| DATABASE_URL | `<your postgres database url>`  |
| DEBUG | `<False>`  |
| DISABLE_COLLECTSTATIC | `<1>`  |
| EMAIL_HOST_PASSWORD | `<your email password>`  |
| EMAIL_HOST_USER | `<your email address>`  |
| SECRET_KEY | `<your secret key>`  |
| SOCIAL_AUTH_FACEBOOK_KEY | `<your facebook key>`  |
| SOCIAL_AUTH_FACEBOOK_SECRET | `<your facebook secret key>`  |
| SOCIAL_AUTH_GOOGLE_OAUTH2_KEY | `<your Google key>`  |
| SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET | `<your Google secret key>`  |
| EMAIL_ADDRESS | `<your email address>`  |
| EMAIL_PASSWORD | `<your email password>` |
| STRIPE_PUBLIC_KEY | `<your stripe public key>`  |
| STRIPE_SECRET_KEY | `<your stripe secret key>`  |

  12. store data base to > ```python manage.py dumpdata > initial_data.json```
  13. Add a development (postgres) database by following this link:
    `https://devcenter.heroku.com/articles/heroku-postgres-import-export`

# Credits

## Media
  - The photos used in this project came from [Pexels](https://www.pexels.com/) and original [Hunt Interiors](http://www.huntinteriors.co.uk/) website.

## Code
  - This application was developed using [StartBootstrap](https://startbootstrap.com/templates/) templates. But during the development period, it was changed multiple times, a current wireframe is not the original wireframe.
  - Throughout the website, I used Code Institute code from the Boutique Ado project only changing bits and pieces so they would align with my project goals.
  - Django for Beginners v3 by William S. Vincent.
  - Django 3 By Example 3rd ed. by Antonio Mele.


## Acknowledgment
  - The initial start of my project was inspired by [Cocoabine youtuber](https://www.youtube.com/playlist?list=PLY4QSV0S7hD-qflv23HTWTMDCE-j3T8Xd), 
    later I had to change some design by adding Code institute code from the Boutique Ado project. After the meeting with my Mentor, I was advised to
     change my design and inspire more from the professionals like [This](https://preview.themeforest.net/item/mint-interior-design-html-template/full_screen_preview/27515892?_ga=2.260447242.645249026.1601897287-1650349433.1566209512)
  - Huge thanks go to Discord and stack overflow community, especially Martin Schere, Sohal Ahmad and Gaurav Sahdev for helping me with bugs during design, checkout and deployment.