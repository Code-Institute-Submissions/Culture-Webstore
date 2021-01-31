# Testing

## Contents

1.  [Browsers](#Browsers "Goto Browsers")
2.  [Responsiveness](#Responsiveness "Goto Responsiveness")
3.  [Code Validation](#Code-Validation "Goto Code Validation")
4.  [User Story Testing](#User-Story-Testing "Goto User Story Testing")
5.  [Manual Testing](#Manual-Testing "Goto User Manual Testing")
    * [Design](#Design "Goto Design")
    * [Responsive](#Responsive "Goto Responsive")
    * [Functionality](#Functionality "Goto Functionality")

## Browsers
The site was tested across multiple browsers - Chrome, Safari, Firefox and Opera to ensure each page displayed correctly.
Browser compatibility was also tested using the Lambdatest App.

## Responsiveness
The site's reponsiveness was continuously monitored during the development stage using Chromes *Dev Tools*.
Media queries have been added to ensure all elements resize with any issues at the various Bootstrap breakpoints.

![Responsiveness Testing](https://raw.githubusercontent.com/JustinMcC066/Culture-Webstore/main/readme_images/culture-responsive-screens-update.jpg)
![Testing Feedback Table](https://raw.githubusercontent.com/JustinMcC066/Culture-Webstore/main/readme_images/site-testing.jpg)

## Code Validation
All html pages were checked using [W3C Markup Validation](https://validator.w3.org/) and passed with no errors.

The CSS file was checked using [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) and passed with one error (Parse Error). When corrected, the animation fails to work.
I have decded to leave this intact as this is a known error in the w3 CSS validator. [Parse Errors with calc values](https://stackoverflow.com/questions/18035088/parse-errors-when-using-calc-with-rem-and-px)

All JavaScript files were checked using [JS Hint](https://jshint.com/) No errors were reported.

The Python apppy file was checked using [PEP8 Online](http://pep8online.com/) to ensure it met PEP8 requirements. No errors were reported.

## User Story Testing

#### New Users

**As a new user of the site I want:**

* "To get a sense of the brand from the landing page"
  * Landing page is minimal, modern and contains imagery of a prticular style. Hero section is engaging and animated.

* "To see a breakdown of categories to choose from"
  * Links to the categories (Colleciton / Womens / Mens) are featued on the home screen as large image links.

* "To see a selection of products to engage with"
  * A "Featured Products section is located on the landing page."

* "To easily navigate the site from each page"
  * A fixed navbar features across all pages with links to all pages.

* "To search the store for a particular item"
  * A "Search" button is located in the navbar which opens a full-screen search modal.

* "To view further information about each individual product"
  * Each product has its own details page complete with all necessary product info.

* "To purchase a product or multiple of the same item"
  * The product details page has an "Add to Cart" and quntity selector.

* "To add multiple items to my bag"
  * Multiple items can be aded to the users shopping bag.

* "To edit quantities of items or remove items from my cart"
  * The user can update the item quantities or remove iems from the bag page.

* "To pay by credit card and receive a confirmation email for my order"
  * Stripe is inegrated allowing the users to make payments using their credit card.

* "To see an about page form more information on the brand/company"
  * An about page is included on the site

* "To view a clear returns policy"
  * A brief returns icon and text sectio appears across multiple pages. A returns policy is also located on each product details page.

* "To see view a FAQ page should I have any questions"
  * An FAQ page is included on the site. It is accessable from the footer menu and contact page.

* "To view a contact page should I have any direct queries"
  * A contact page is included on the site. and is accessable from the footer.

* "To have the ability to create an account with the store and view my previous orders"
  * Users can register and view their previous orders from a "My Profile" page.


#### Return Users

**As a returning user of the site I want:**

* "To have the ability to view my previous orders"
  * Users can register and view their previous orders from a "My Profile" page.

* "To have the ability to update my stored information"
  * Users can their profile/delivery info from their "My Profile" page.


#### Store Admin

* "To have the ability to add, edit or delete a product from the front end"
  * An "Add Product" page is included along with an Edit product for site superusers. A superuser can also delete a product from the product details page or in the edit product view.

* "To have the ability to access the admin dashboard to view/edit all products, categories, emails, users and blog posts"
  * The superuser has access to the site admin dashboard where all database elements are viewable/editable.


## Manual Testing

Manual testing was completed at various stages throughout development. This ensured all elements responded correctly to each interaction as intended and functions ouput the correct result.
Printing values to the python terminal was key to identifying incorrect calculations and outcomes. [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) Chrome Developer Tools was used throughout all stages of development.
The site was shared with real users to test usability and reveal any bugs.

#### Design

1.  ##### Issue
  * Line-breaks in the body text of each blog were not being honoured.
1.  ##### Fix
  * I used {{ value|linebreaksbr }} for the template to render the body text with the whitespace intact as per the admin panel input.

2.  ##### Issue
  * Links could not be embedded in the blog section. Text was instead being rendered in the template.
2.  ##### Fix
  * I used {{ model.field|safe }} to display embeded code correctly.

3.  ##### Issue
  * In some blogs an embedded soundcloud link may not be wanted/needed. In this case an input would be blank. When left blank, the text "None" was rendering on the frontend.
3.  ##### Fix
  * I used {{ model.field|default_if_none:''" }} to ensure the text "None" wasnt being rendered in the template.

#### Responsiveness

1.  ##### Issue
  * Menu text was overlapping.
1.  ##### Fix
  * Icons were used for tablet size to prevent the text from overlapping.


#### Functionality

1.  ##### Issue
  * Webhooks could not be tested from my local eveloment environmnt as the local url could not be used for webhook testing on Stripe.
1.  ##### Fix
  * I used ngrok to expose a https:// url so I coul complete the webhook testing locally.

2.  ##### Issue
  * Blog image wasnt rendering from the url input.
2.  ##### Fix
  * I used {% firstof.model second.model %} to display the first one that meets requirements.

3.  ##### Issue
  * Products were not showing when being added to the bag.
3.  ##### Fix
  * I replaced product.objects.get with get_object_or_404 which fixed the issue. 


#### Warnings

1. *  W3 Validation: The type attribute is unnecessary for JavaScript resources. 
  * I decided not to fix this as it caused errors with the stripe webhook.