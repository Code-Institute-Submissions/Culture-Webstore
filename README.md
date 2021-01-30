# Milestone Four

### Code Institute: Full Stack Frameworks Milestone Project

![Culture Logo](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/culture-logo.png)

## Culture Webstore - [Live Site](https://culture-webstore.herokuapp.com/)

Culture is an online ecommerce site providing clothing and accessories tailored to urban lifestyles.

 - - - - 

## Contents

1. [UX](#UX "Goto UX")
    * [User Stories](#User-Stories "Goto User Stories")
    * [Wireframes](#Wireframes "Goto Wireframes")
    * [Surface](#Surface "Goto Surface")

2. [Features](#Features "Goto Features")
    * [Existing Features](#Existing-Features "Goto Existing Features")
    * [Features Left to Implement](#Features-Left-to-Implement "Goto Features Left to Implement")

3. [Technologies Used](#Technologies-Used "Goto Technologies Used")

4. [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Database Models](#database-models)

5. [Testing](#Testing "Goto Testing")

6. [Deployment](#Deployment "Goto Deployment")

7. [Credits](#Credits "Goto Credits")
    * [Code](#Code "Goto Code")
    * [Media](#Media "Goto Media")

 - - - -

## UX

### Target Audience

* People who are fashion aware.

* People who are looking for a unique find.

* People who are interested in current urban culture and fashion.


### Visitor Goals

* Shop a secure site that looks trustworthy.

* Be presented with products in a familiar manner making the experience hassle free.

* Be able to view all information about my order and receive confirmation on orders.

* Sign up to a newsletter should I want to stay up-to-date with the stores news.


### Business Goals

* Entice users to purchase.

* Provide a clear, confident place to shop.

* Provide a clear, confident place to shop.

* Allow users to contact the store.



### User Stories

#### New Users

**As a new user of the site I want:**

* "To get a sense of the brand from the landing page"

* "To see a selection of products to engage with"

* "To see a breakdown of categories to choose from"

* "To easily navigate the site from each page"

* "To search the store for a particular item"

* "To view further information about each individual product"

* "To purchase a product or multiple of the same item"

* "To add multiple items to my bag"

* "To edit quantities of items or remove items from my cart"

* "To pay by credit card and receive a confirmation email for my order"

* "To see an about page form more information on the brand/company"

* "To view a clear returns policy"

* "To see view a FAQ page should I have any questions"

* "To view a contact page should I have any direct queries"

* "To have the ability to create an account with the store and view my previous orders"


#### Return Users

**As a returning user of the site I want:**

* "To have the ability to view my previous orders"

* "To have the ability to update my stored information"


#### Store Admin

* "To have the ability to add, edit or delete a product from the front end"

* "To have the ability to access the admin dashboard to view/edit all products, categories, emails, users and blog posts"


### Wireframes

Wireframes were created using [Sketch](https://www.sketch.com/).
Layouts were created for mobile, tablet and desktop to assist the design decisions before coding.

**Desktop**

* [Home Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/desktop/desktop-home-page.jpg)
* [Shop Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/desktop/desktop-shop-page.jpg)
* [Product Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/desktop/desktop-product-page.jpg)
* [About Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/desktop/desktop-about-page.jpg)
* [Blog Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/desktop/desktop-blog-page.jpg)
* [Blog Detail Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/desktop/desktop-blog-detail-page.jpg)
* [FAQ Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/desktop/desktop-faq-page.jpg)
* [Contact Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/desktop/desktop-contact-page.jpg)
* [Bag Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/desktop/desktop-bag-page.jpg)
* [Checkout Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/desktop/desktop-checkout-page.jpg)
* [Order Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/desktop/desktop-order-page.jpg)

**Tablet**

* [Home Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/tablet/tablet-home-page.jpg)
* [Shop Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/tablet/tablet-shop-page.jpg)
* [Product Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/tablet/tablet-product-page.jpg)
* [About Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/tablet/tablet-about-page.jpg)
* [Blog Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/tablet/tablet-blog-page.jpg)
* [Blog Detail Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/tablet/tablet-blog-detail-page.jpg)
* [FAQ Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/tablet/tablet-faq-page.jpg)
* [Contact Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/tablet/tablet-contact-page.jpg)
* [Bag Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/tablet/tablet-bag-page.jpg)
* [Checkout Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/tablet/tablet-checkout-page.jpg)
* [Order Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/tablet/tablet-order-page.jpg)


**Mobile**

* [Home Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/mobile/mobile-home-page.jpg)
* [Shop Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/mobile/mobile-shop-page.jpg)
* [Product Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/mobile/mobile-product-page.jpg)
* [About Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/mobile/mobile-about-page.jpg)
* [Blog Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/mobile/mobile-blog-page.jpg)
* [Blog Detail Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/mobile/mobile-blog-detail-page.jpg)
* [FAQ Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/mobile/mobile-faq-page.jpg)
* [Contact Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/mobile/mobile-contact-page.jpg)
* [Bag Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/mobile/mobile-bag-page.jpg)
* [Checkout Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/mobile/mobile-checkout-page.jpg)
* [Order Page](https://github.com/JustinMcC066/Culture-Webstore/blob/main/readme_images/wireframes/mobile/mobile-order-page.jpg)


### Surface

#### Tone/Colours

The landing/home hero is dynamic and engaging.

The design is clean, minimal and refined.

White is used for the body background colour for easy readability/accessibilty and allows the graphics, imagery to be the main focus.

#### Typography

**Font used:**
Primary font
* [Work Sans](https://fonts.google.com/specimen/Work+Sans)

Heading font
* [Fahkwang](https://fonts.google.com/specimen/Fahkwang)

Accent font
* [Roboto Mono](https://fonts.google.com/specimen/Roboto+Mono)

The font is linked from [Google Fonts](https://fonts.google.com/) in the Base stylesheet.

#### Animation

Hover animations are triggered on mouse hover over product and blog thumbnails to enhance the user experience.

A typing text animation is used on the home page hero to engage the user.

On the *About* page a subtle image rotation animation in the hero section is triggered on scroll.

 - - - - 

## Features

### Existing Features:

#### Landing Screen:
   - The landing page contains a hero section with an engaging animated title followed by a "Shop Now" button linking the user to the shop/all products page.
   - A short introductory text section follows informing the user of the store ethos.
   - A large image based category section follows with link to all products, womens or mens.
   - This is followed by a "Featured Products" section where 4 featured products are displayed. These 4 products are selected by the admin when adding a product.
   - An email subscription section is last to feature on the page. Users can submit their email address to be used for notification about new products and events. The emails are stored in a seperate table in the database.

#### Navigation:
   - The navbar is static and features across all pages.
   - The initial navbar links are: Shop | Spotlight | About | Search | Account (Dropdown: Register | Login) | Cart.
   - The navbar links change depending on the user state:
      * If the user is *not* logged in and the navbar dropdown links under *Account* are: Register | Login
      * If the user is logged in, the navbar dropdown links under *Account* are: Add product | My Profile | Logout
   - The nav search link opens a full-screen page overlay with a search form input.
   - When a product is added to the users cart the cart icon changes colour and updates to show items inside and the sum of the items in the bag is displayed.
   - Above the main nav-bar there is an additional banner highlighting the message, "FREE DELIVERY | WHEN YOU SPEND €60+". This price is set as a variable in the settings file of the project.

#### Footer:
   - The footer features on each page with social media links aswell as links to Privacy Policy | Terms | FAQ | Contact.
   - The footer also features an image of all accepted card types.

#### Animations:
   - Subtle hover animations are used on the home, product and blog pages.
   - A scrolling text animation is used on *Shop* mega menu directing customers to the shop page.
   - On the about page a rotate animation is triggered by the users scroll which rotates an svg image in the hero section of that page.

#### Links:
   - Links across the site have an animation that is triggered when hovered.

#### Category Images:
   - The category links featured on the home page animate with a zoom effect when hovered.

#### Product Cards:
   - The product cards throughout the site animate with a zoom effect when hovered.
   - The cards also have a hidden call to action that comes in to view on the card when hovered.
   - The name of the item and price is displayed below each product thumbnail image.
   - If the user is a superuser then additional *Edit* & *Delete* buttons are displayed on each card.

#### Products:
  **Sorting**
   - The products listed on the shop page can be sorted by:
    - Price (low to high)
    - Price (high to low)
    - Rating (low to high)
    - Rating (high to low)
    - Name (A-Z)
    - Name (Z-A)
    - Category (A-Z)
    - Category (Z-A)

  **Filters**
   - Products are filtered initially but mens of womens, then further by clothing type.
   - Each category is displayed on the product detail page showing which category it relates to.

  **Animations**
   - The product cards throughout the site animate with a zoom effect when hovered.
   - A hidden call to action that comes in to view on the card when hovered.

#### Product Detail Page:
   - Each prouduct has its own dedicated detail page.
   - This page includes a large product image along with the product title, rating, description, size selector (where applicable) and price. A quantity selector and add to cart button follows this along with a product SKU code. Text beow this announces to the user that they receive free shipping when they spend €60 or more.
   - Below the main product information is a tabs area with three sections, for additional product care, delivery and returns information.
   - The icon info section is repeated on this page.
   - A "New In Stock" section follwos withthe 3 most recent additions to the store.

#### Bag Page:
   - Items in the users bag are displayed in rows showing the product info (Title, size and SKU code), price, quantity, subtotal and remove button.
   - The quantity can be updated for each item and items can be removed one by one with the use of the remove *X* button.
   - The items total is calculated at the bottom along with the delivery charge.
   - The grand total is displayed larger beneath this along with an additional line letting the user know how much more they need to spend to avail of the free shipping.
   - Users can proceed to the secure checkout or continue shopping by clicking the respective buttons on the page.

#### Checkout Page:
   - All items in the users bag are again displyed with all relevant info and pricing.
   - A form is dislayed alongside the overview of the items in the order. This form collects all relevant information for the products to be shipped to the customer.
   - The stripe payment section sits beneath for the users credit card information.

#### Checkout Success:
   - When the order and paymnt is successful the user is redirected to a checkout success page that displays the order info, order details, delivery ddetails and billing information.
   - A toast message is also displayed notifyng the user that their order is being processed and their order number is displayed.
   - A button is displayed to direct the user back to the store.

#### Newsletter subscription
   - The website features a newsletter sign-up section where users can subscribe to receive updtes via email about the store. Toast messaging is included to inform the user if they have subscribed successfully.
   - This section is included across various pages of the store.

#### Register/Edit Profile
   - When a user registers, a profile is created for them. Here they can update their default delivery information and view their order history.

#### Login
   - Facebook social login has been added using Django Allauth authentication.
   
#### Add/Edit/Delete Products:
   - Super-admins have the ability to add, edit and delete products.

#### About Page:
   - The about page features a large hero section similar to the landgin/home hero.
   - A scrolling animation is used to control the rotation of a graphi element in the hero section adding a subtle layer of interactivity and feedback response.
   - The page offers information on the story behind the compay and background into their ethos..

#### Contact Page:
   - The contact page features a contact form which sends an email to the store admin notifying them of the contact. The customer messages are viewable via the store admin dashboard.
   - 3 large clickable buttons sit below the contact form - Address, Contact Number and FAQ. The address button links to the location in Google Maps, the contact number allows the user to call the store direct from the browser and the FAQ button carries the user to the FAQ page.


#### Toast Messaging
   - Toast messaging is used to respond to user form inputs highlighting any issues or providing positive feedback on form submission. Four toast messaging styles are used, *error*, *info*, *success* and *warning* to cover all eventualities.

### Payment
To place an order, use the following Strip test card details:

- **Card number:** 4242 4242 4242 4242
- **Expiry date:** Any future date
- **CV2 number:** Any 3 digits
- **ZIP**: Any 5 digits


### Features Left to Implement

* Product image gallery with multiple images for each product.

* Pagination for the products page or lazy loading of product cards.

* Frontend input form for adding blogs.

* I would like to add a page where users can post an image showing how they wore the item bringing a community element to the site.

 - - - - 

## Information Architecture

#### Database:

- Local development - Sqlite3 database.
- Deployment via Heroku - PostgreSQL database.

#### Database Models:

- Django gives you an automatically-generated database-access API based on your models. This provides a table structure to your database when migrations are applied.

#### User Model

The User model provided by Django.

#### Category Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Name | name | max_length=254 | CharField
Friendly Name | friendly_name | max_length=254, null=True, blank=True | CharField

#### Product Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Category | category | null=True, blank=True, on_delete=models.SET_NULL | ForeignKey to Category
SKU | sku | max_length=254, null=True, blank=True | CharField
Name | name | max_length=254 | CharField
Description | description | blank | TextField
Has Sizes | has_sizes |delete=False, null=True, blank=True | BooleanField
Featured | featured | default=False | BooleanField
Price | price | max_digits=6, decimal_places=2 | DecimalField
Rating | rating | max_digits=6, decimal_places=2, null=True, blank=True | DecimalField
Image URL | image_url | max_length=1024, null=True, blank=True | URLField
Image | image | null=True, blank=True | ImageField

#### Order Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order Number | order_number | max_length=32, null=False, editable=False | CharField
User Profile | user_profile | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' | ForeignKey to User
Full Name | full_name | max_length=50, null=False, blank=False | CharField
Email | email | max_length=254, null=False, blank=False | EmailField
Phone Number | phone_number | max_length=20, null=False, blank=False | CharField
Country | country | max_length=80, null=True, blank=True | CharField
Postcode | postcode | max_length=20, null=True, blank=True | CharField
Town / City / Locality | town_or_city | max_length=40, null=False, blank=False | CharField
Street Address 1 | street_address1 | max_length=80, null=False, blank=False | CharField
Street Address 2 | street_address1 | max_length=80, null=False, blank=False | CharField
County | county | max_length=80, null=True, blank=True | CharField
Date | date | auto_now_add=True | DateTimeField
Delivery Cost | delivery_cost | max_digits=6, decimal_places=2, null=False, default=0 | DecimalField
Order Total | order_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
Grand Total | grand_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
Original Bag | Original Bag | null=False, blank=False, default='' | TextField
Stripe PID | stripe_pid | max_length=254, null=False, blank=False, default='' | CharField


#### Order Item Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order | order | null=False, blank=False, on_delete=models.CASCADE | ForeignKey to Order
Product | product | null=False, blank=False, on_delete=models.CASCADE | ForeignKey to Product
Product size | product_size | max_length=2, null=True, blank=True | CharField
Quantity | quantity | null=False, blank=False, default=0 | IntegerField
Line Item Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | DecimalField


#### Contact Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Full Name | full_name | max_length=200 | CharField
Email | email | max_length=200 | EmailField
Message | message || TextField
Contact Date | contact_date |blank=True, default=datetime.now | DateTimeField
User | user_id | User, null=True, on_delete=models.CASCADE | ForeignKey to User


#### Subscribe Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Email | email | max_length=254, null=False, blank=False | EmailField


#### Blog Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Title | title | max_length=250 | CharField
Slug | slug | | SlugField
Image URL | image_url | max_length=1024, null=True, blank=True | URLField
Image | image | null=True, blank=True | ImageField
Intro | intro | | TextField
Body | body || TextField
Date Added | date_added |auto_now_add=True | DateTimeField
Soundcloud | soundcloud_embed | max_length=1200, null=True, blank=True | TextField

 - - - - 


 ## Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * For structuring the site pages.

* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  * For styling the content of each page.

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  * For creating interactivity on the site.

* [Python](https://www.python.org/)
  * For developing and coding the backend.

* [Bootstrap 4](https://getbootstrap.com/)
  * Framework used to form the layout of each page.

* [Django](https://www.djangoproject.com/)
  * Web app framework.

* [Django Allauth](https://django-allauth.readthedocs.io/)
  * For authentication, registration, account management as well as 3rd party (social) account authentication.

* [sqlite3](https://www.sqlite.org/index.html)
  * Development database.

* [PostgreSQL](https://www.postgresql.org/)
  * Heroku database.

* [Autoprefixer CSS](https://autoprefixer.github.io/)
  * Used for adding prefixes to CSS classes to ensure browser consistency and compatibility.

* [PEP 8 Online Validator](http://pep8online.com/)
  * To validate python code.

* [W3C HTML Validator](https://validator.w3.org/)
  * To validate python code.

* [Jigsaw W3](https://jigsaw.w3.org/css-validator/)
  * To validate css code.

* [JS Hint](https://jshint.com/)
  * To validate JavaScript code.

* [Google Fonts](https://fonts.google.com/)
  * For linking fonts for use on the site.

* [Favicon.io](https://favicon.io/favicon-converter/)
  * For generating favicon images and ico file.

* [Line Icons](https://lineicons.com/)
  * For icons used on site.

* [Font Awesome](https://fontawesome.com/)
  * For additional free icons.

* [Tiny PNG](https://tinypng.com/)
  * For reducing image file sizes.

* [Adobe Illustrator](https://www.adobe.com/ie/products/illustrator.html)
  * For logo and element design.

* [Sketch](https://www.sketch.com/)
  * For UI design.

* [Adobe Photoshop](https://www.adobe.com/ie/products/photoshop.html)
  * For image editing and resizing.

* [Visual Studio Code](https://code.visualstudio.com/)
  * Integrated development environment (IDE) used for development.

* [Git](https://git-scm.com/)
  * Used for version control.

* [GitHub](https://github.com/)
  * Used for managing and storing my code.

* [Heroku](https://www.heroku.com/)
  * Used to deploy the web app.

* [AWS S3](https://aws.amazon.com/)
  * Used to store media and static files.

* [Stripe](https://stripe.com/en-ie)
  * Used to handle payments.

 - - - - 

## Testing
Various methods of testing were used throughout all stages of development.

All methods of testing can be viewed within the [testing.md](https://github.com/JustinMcC066/Culture-Webstore/blob/main/testing.md) file.

 - - - - 

## Deployment
Visual Studio Code IDE was used to develop the website. The code was committed to git and pushed to GitHub within Visual Studio Code.

The site is hosted and deployed through [Heroku](https://www.heroku.com/). The Heroku app is connected to the Git Repository and updates automatically as new commits are pushed to Github.


### Local

To run this project locally the following steps are required:
*Please note: You will need to install the following in order to run this app on your local machine:*
*A virtual environment is also recommended for development.*

- Git
- Python 3
- PIP

You will also need to create free accounts with the following services:
- Heroku
- AWS and set up an S3 bucket
- Stripe

#### Instructions

1. Download a copy of this github repository using the instructions below:
    *  Navigate to [https://github.com/JustinMcC066/Culture-Webstore.git](https://github.com/JustinMcC066/Culture-Webstore.git)
    *  Click the green 'Clone or Download' button and copy the text url in the dropdown.
    *  Open up a terminal window in your IDE of choice.
    *  Navigate to your desired file location.
    *  Paste the following code and input it into your terminal to clone.
    ```
    git clone https://github.com/JustinMcC066/Culture-Webstore.git
    ```

2. It is recommended to create a virtual environment to prevent the dependencies from being installed globally on your system. This allows you to install dependenceies on a per-project basis.
To create a virtual environment for your project, in the Terminal, in the project's root directory, enter:

`pipenv install`

and then activate the created virtual environment with

`pipenv shell`

3. Install all requirements from the requirements.txt file using this command:

    `pip3 install -r requirements.txt`

4. In the IDE terminal, use the following command to launch the Django project:
`python3 manage.py runserver`

5. In the root directory of the project, create an `env.py` file and add this to a `.gitignore` file to will prevent your sensitive project info from being pushed to GitHub.

6. In your `env.py` file, set the environment variables as follows:

```
os.environ["AWS_ACCESS_KEY_ID"] = "<your key here>"
os.environ["AWS_SECRET_ACCESS_KEY"] = "<your key here>"
os.environ["AWS_STORAGE_BUCKET_NAME"] = "<your AWS bucket name here>"
os.environ["SECRET_KEY"] = "<your secret key here>"
os.environ["STRIPE_PUBLIC_KEY"] = "<your key here>"
os.environ["STRIPE_SECRET_KEY"] = "<your key here>"
os.environ["STRIPE_WH_SECRET"] = "<your key here>"
```
7. Create a superuser to access the django admin panel and database and then follow all steps to add your admin username and password:

- `python3 manage.py createsuperuser`

8. Next, you'll need to make migrations to create the database schema using the commands as follows:
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`

9. The application can now be run locally.


### Deploying to Heroku

#### To deploy the app, follow the steps below:

1. Commit all files to your Git Repository.
    *  Sign up and log in to Heroku.
    *  ```Create new app``` in Heroku using a unique name. Select your region and create your app.
    *  Add a Heroku Postgres ("Hobby Dev - Free" option) under the resources tab.
    *  From the app dashboard on Heroku select *Settings* and then click *Reveal Config Vars*.

2. Set the following key/value settings for the config vars - see below

#### Heroku Config Vars

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | <"your AWS key here">
AWS_SECRET_ACCESS_KEY | <"your AWS secret key here">
DATABASE_URL | <"your postgres database here">
EMAIL_HOST_PASS | <"your app password as generated by Gmail (if you use it)">
EMAIL_HOST_USER | <"your email address that is used to send emails">
SECRET_KEY | <"your secret key here">
STRIPE_PUBLIC_KEY | <"your stripe public key here">
STRIPE_SECRET_KEY | <"your stripe secret key here">
STRIPE_WH_SECRET | <"your stripe webhook secret key here">
USE_AWS | "True"

3. Create a `requirements.txt` file in project so Heroku can install the required dependencies to run the app using the following command:  
`pip3 freeze -r > requirements.txt`

4. Create a `Procfile` in the root project folder with the following information:  
`web: gunicorn culture.wsgi:application`

7. Migrate the database models to the Postgres database on Heroku using the following commands:

`python3 manage.py makemigrations`

`python3 manage.py migrate`

8. Create the super user as shown in the **Running project locally** section. 

9. Connect the app to your Github repository.

10. Selected 'Enable Automatic Deploys' in the 'Automatic Deployment' section and make sure that the correct branch is selected.

12. Once the build completes, navigate to the 'Open app' button to view the live site in your browser.


### Setting up Social Login (Facebook)

The following steps can be taken to implement Facebook social platform login.  

1. Install django-allauth using the following command:  
`pip3 install django-allauth`

2. Add the following to the **INSTALLED_APPS**  secition in the `settings.py` file:  
```
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'allauth.socialaccount.providers.facebook',
```

3. Add the below to the `settings.py` file:

```
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email','public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'kr_KR',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'}}
```

4. Create a Login App on Facebook for Developers to  - https://developers.facebook.com/. **Please Note:** (A facebook account is required)
5. Create a new app via the dashboard.
6. Name your app and click **Create App**
7. Select **Set Up** under the Facebook Login product and select **Web**.
8. Add website url, e.g. https://culture-webstore.herokuapp.com/ and click save.
9. In **Settings > Basic**, copy the App ID and App Secret Key.
10. Log in the Culture Webstore website admin dashboard. 
11. Under Sites, add site domain name and display name, ensuring it had the Site ID of 1.
12. Navigate to **Social Accounts > Social applications**
13. Select **Add social application**
14. Enter name of social account.
15. Input App ID into Client id.
16. Input App Secret into Secret Key.
17. Add the site to available sites and save.
18. You will now be able to log in using your facebook credentials from the login page created by `django-allauth`.
19. You can now style the login button to match your interface in the allauth socialaccount snippets file `allauth/socialaccount/snippets/provider_list.html`

## Credits

### Code

The following sites were used for inspiration and assistance:

* [Stack Overflow](https://stackoverflow.com/)

The contact app is based on the **Python Django Dev To Deployment** course by Brad Traversy.


### Media
The images used on this site are royalty free and were obtained from [Unsplash](https://unsplash.com/) and [Pexels](https://pexels.com/)

### Disclaimer
This site has been developed for educational purposes as part of the [Code Institute](https://codeinstitute.net/) Full-stack Software Development course.