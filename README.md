<h1 align='center'>
Full Stack Website with Django - Milestone Project 4 -Antiques E-commerce -Marzena Chodnicka
</h1>

<div align='center'>

[Antiques](https://marzdell-antiques.herokuapp.com/)  This website is an E-Commerce website where end-users can purchase antiques.
To partake within the secure area of the website the user must be registered and logged in. 
They make their order and proceed to the checkout. Once they have entered the required payment details they will be notified by an alert message that states how the payment process went. 
Unregistered users can just browse through the products list. 

<br><br>
[**View Antiques website here**](https://marzdell-antiques.herokuapp.com/),
[**View Website Development in Github here**](https://github.com/MarzDell/full-stack-frameworks-with-django)
</div>

## Contents Table

1. [**UX**](#ux)
    - [**Project Purpose**](#project-purpose)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features to implement**](#features-to-implement)

3. [**Technologies Used**](technologies-used)

4. [**Testing**](#testing)

5. [**Deployments**](#deployments)

6.  [**Credits**](#credits)
    - [**Contents**](#contents)
    - [**Images**](#images)
    - [**Help with code**](#help-with-code)
    - [**Acknowledgements**](#acknowledgements)

## UX

### Project Purpose

The main goal of Antiques E-commerce is to make perfect place for users to get their own unique furniture which now a days it is difficult to find now a days.

### Design

The design of the page is simple and easy to move around, it is intuitive as well as colours are light which improves user experience.

- #### Fonts
    
    - The font **'Playfair Display'** was used as it is simple and easy to read also it is commonly used on popular websites.

- #### Colours
    
    - **All Pages -** A white background was chosen to keep good looking design.
    - **Buttons -** Colours of the buttons were left same as on Bootstrap. 
    - **Links -** An orange colour was chosen once hovering to match the colour of the button and make connection of styles on the website.
    - **Social Links -** A black colour was chosen as a good contrast between the background, an orange was chosen once hovering to match links colours.
    
- #### Styling

    Style on each page were chosen to match all website, the user changing from one page to another will see more as a flow then just a page.
    I created short and simple way of display that the user will be not overload of content. Style on the website fits to every generation of the user due to having 
    modern layout but well-known to the rest.
    
- #### Website Pictures

All images have been chosen to match and have been downloaded from Pinteres.
    
### Wireframes

Wireframes were made using print screen.

## Features

### Existing Features

1. #### Navigation

    This provides highlighted link choices on every page for easy navigation and takes the end-user to their desired location. 
    
2. #### Search function

    On Navigation bar you can find search function where the user can type in a keyword to find type of antiques. It is created to save them some time and make it simple.
    
3. #### Home Page

     On Home page the user see container with picture where can use link to Product page.
    
4. #### Products Page

    Here the user can browse through the various products
    
5. #### Register

    This is where the new user can submit their details so they can register.

6. #### Login

    From here a registered user can log in to the website and continue to purchase a product. 
    On the login page there is also a link to aquire a new password if you have forgotten your one. 
    
7. #### Logout

    From here a registered user can logout from the website. 
    This view is only possible when a logged in user is active within the website.
    
8. #### Checkout

    Displays the proposed order and it's amount. From here the user can still decide not to purchase and empty their cart or 
    amend it if they see fit to do so, again this is if the user is logged in, if not, they are reverted to the login page.
    
9. #### Shopping Cart 
    This area holds the users choices of purchase until they proceed to the checkout area to complete their transaction. 
    Once the choices have been made the Cart then is populated by the product choices and they sit there until the user wants
    to checkout or amend their choices or if they would like to remove their items from the Cart. 
    If you are not logged in choosing to checkout will revert the user back to the login page.


### Features to Implement

Due to lack of time remaining the following features were not implemented:

1. #### Linking product info to open on a new html page that displays the information for just one product, which may improve UX.

2. #### Option for auction some of the rare items.

3. #### A cart order list and shipping facility.

4. #### Rate us will be made with javascript and will be connected with link where user can leave feedback.

## Technologies Used

- This project uses HTML, CSS, JavaScript and various different technologies to work as helpers to the languages.
- #### [Gitpod](https://www.gitpod.com)
    - **Gitpod** is an IDE used to develop the website.
- #### [Bootstrap](https://www.bootstrapcdn.com/)
    - **Bootstrap** is used to create easier & cleaner responsiveness in addition with helping maintain padding and margins.
    - It's also used to include modal features to the website to give it a professional look.
- #### [Google Fonts](https://fonts.google.com/)
    - **Google Fonts** has been used to provide clean and eye-catching fonts to the website.
- #### [JQuery](https://jquery.com)
    - **JQuery** has been used to simplify DOM manipulation.
- #### [Font Awesome](https://www.bootstrapcdn.com/fontawesome/)
    - **Font Awesome** has been used to add icons to the website.
- #### [GitHub](https://github.com/)
    - **Github** is used: 
    1. As a remote backup of code used in the project.
    2. As a remote server for another user to see the code used in the project.
    3. For users to view the deployed version of the website. The deployed version can be viewed [here!](https://github.com/MarzDell/full-stack-frameworks-with-django)
- #### [Python3](https://www.python.org/downloads/)
    - **Python3** was used to compile and utilise the logic for the project.
- #### [Django 2.2](https://www.djangoproject.com/)
    - **Django** is used as my Python web framework.
- #### [Stripe API](https://stripe.com/docs/api)
    - **Stripe API** is used to make secured payments at the checkout.
- #### [Whitenoise](http://whitenoise.evans.io/en/stable/)
    - **Whitenoise** is simplified static file serving for Python web apps.
- #### [PostgreSQL](http://whitenoise.evans.io/en/stable/)
    - **PostgreSQL** is used as relational SQL database plugin via Heroku.
- #### [Heroku](https://www.heroku.com/)
    - **Heroku** This is a cloud platform where the project is deployed to. The website can be viewed [here!](https://marzdell-antiques.herokuapp.com/)


## Testing

<h1 align="center">
Antiques- Testing
</h1>

## Automated Testing

### Validating Code

Validation services were used to ensure that code was valid code used to develop the website.

- [W3C Markup Validation Service](https://validator.w3.org/) was used to test HTML code to ensure it was valid code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to test CSS code to ensure it was valid code.
- [PEP8 online check](http://pep8online.com/) was used to test Python code to ensure it was valid code.

## Manual Testing

A number of manual tests were done to ensure the website is working as it should be and that the user can use without any problems.

### Testing on Desktop

The website was tested in Browsers: Chrome, Safari, FireFox and Internet Explorer. 
The website was tested and used on a Laptop, Macbook & Desktop PC and Iphone and Samsung Galaxy.

### Testing on tablet and mobile devices

The website was tested on iPhone 6, Samsung Galaxy. It's also been run through Chrome Developer tools
in the 'Responsive' setting.

## Testing

I checked that:

 All the links are working correctly and the page does not show any error.

Note: DEBUG in settings.py is set to True as when I set to False the app does not display any pictures, I try different ways to fix it 
      but i could not find whats the reason and code seems to be correct.

## Deployments

The project is deployed on the Heroku Cloud Platform by using a local Git repository linked to Heroku. 

To run this project locally I needed the following to be installed:

    -Python3 to run the application.
    -PIP to install all app requirements.
    -Any IDE. I used Gitpod.
    -GIT for version control.
    
## Credits

### Contents

All Content has been thought of and written by the Developer. 


### Images

Images were downloaded from the webpage [Pinterest](https://www.pinterest.co.uk/).
  

### Help with code

- Ideas on how to start with my project a took from youtuber that I follow: [Traversy Media](https://www.youtube.com/user/TechGuyWeb)
- I use help as well from:
    - Website about tutorial [Python3](https://www.tutorialspoint.com/python3/index.htm)
    - Django Documentation [Django 2.2](https://docs.djangoproject.com/en/2.2/)

### Acknowledgements

- Spencer Barriball (spence_mentor) - For discussing ideas, providing help with project and any ideas related to the project. 
    As well offering me help outside of mentor sessions if I will need anything or if i have an issue that I cannot solve by myself.
- Slack app that whenever I needed help or tips, I could check on app.
