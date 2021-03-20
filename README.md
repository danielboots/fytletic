# **Milestone Project 4**  - Full Stack. 

## 🎵 **Fytletic - Fighter Networking Solution**

![Apollo logo and strap line ](static/img/responsive.png)

![index gif](Link)
![user gif](link)

Fytletic is currently deployed and can be visited directly at Heroku **[Fytletic  ](https://fytletic.herokuapp.com/)**


--
## 📓 **About the project:**

**Fytletic**  - A webite which allows

## 💻️ **Technologies Used:**
___

* **[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML):** - Is the main language used in this project which allowed me to correctly structure the website, whereby using best practices to use semantic tags where appropriate.

* **[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS):** - Was used via an external stylesheet using best practices to style format and visually present the HTML.

* **[DJANGO](https://www.djangoproject.com/):** - A Python framework 

* **[BOTO3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html):** - Allows you to directly create, update, and delete AWS resources from your Python scripts.

* **[GUNICORN](https://gunicorn.org/):** - The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server. 

* **[PILLOW](https://pillow.readthedocs.io/en/stable/):** - A functional drop-in replacement for the Python Imaging Library

* **[PSYCOPG](https://www.psycopg.org/):** - A PostgreSQL adapter for the Python programming language.

* **[AWS](https://aws.amazon.com/):** - Amazon Web Services, used to store Media.

* **[STRIPE](https://stripe.com):** - A payments processor allowing us to handle card payments on the site.

* **[HEROKU](https://www.heroku.com/):** - Heroku is a container-based cloud Platform as a Service (PaaS). Used in this project to deploy the live site to the web.

* **[PYTHON](https://www.python.org/):** - Python is a backend programming language used for the CRUD functionality of this application.

* **[MYSQL LITE](#):** - MYSQL-LITE database,

* **[POSTGRES]():** - Used in user password hashing and security for the application.

* **[RANDOMKEYGEN](https://randomkeygen.com/):** - Website used to generate secure passwords, used in this application for ***SECRET_KEY***.

* **[JAVASCRIPT](https://developer.mozilla.org/en-US/docs/Web/JavaScript):** - *As part of Bootstrap* Javascript although I haven't programmed it, was included in the site as part of the Bootstrap framework so that some Bootstrap components such as the navigation toggler would work.

* **[BOOTSTRAP](https://getbootstrap.com/):** - The framework for the site allowing the use of the Bootstrap grid and responsive mobile-first approach. I Used many components from Bootstrap mainly, the Carousel, Navbar, forms and modals. 
* **[MDBOOTSTRAP](https://mdbootstrap.com/):** - The framework based on Google Material Design for Bootstrap. 

* **[GITPOD](https://gitpod.io/):** - IDE for this project. Allowed me to fork the Code Institute template from Github and open in Gitpod so that all extensions were available.

* **[GIT](https://git-scm.com/):** Git employed as version control

* **[GITHUB](https://github.com/):** - Github was used to host the repository for this project.

* **[SQUOOSH](https://squoosh.app/):** - I used Squoosh to reduce the image sizes

* **[PHOTOSHOP](https://www.adobe.com/uk/products/photoshop.html):** - For editing images associated with this project.

* **[BALSAMIQ](https://balsamiq.com/):** - Mac version to develop wireframes for this project.

* **[CHROME](https://www.google.com/intl/en_uk/chrome/):** - Not only did I use Chrome extensively for testing and bug fixing but I used the following extensions :

* **[PESTICIDE](https://www.google.com):** -  This extension inserts (with auto-reload) the Pesticide CSS into the current page, outlining each element. - Giving a good visual representation of containers rows etc, as I was using a material design from MDBootstrap I was inserting containers into containers in points to get the desired layout and style, this extension allowed me to view the layout correctly. 

* **[RESPONSIVE VIEWER](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb):** -  An excellent extension suggested to me by my Mentor Allen - A Chrome extension to show multiple screens in one view. the extension will help front-end developers to test multiple screens while developing responsive websites/applications.

* **[GIFY](https://giphy.com/):** - Used to create the .gif file in readme depicting the responsive viewer in action and showing my testing on different screen sizes. 

* **[WEB FONT GENERATOR](https://www.fontsquirrel.com/tools/webfont-generator):** - Used to bring in a custom font I wanted to use for the main H1/ H2 sections, custom branding.

* **[AM I RESPONSIVE](http://ami.responsivedesign.is/):** - Used to generate the header image displayed at top of Readme.MD file depicting 4 screen displays.

* **[CSS BEAUTIFIER](https://www.freeformatter.com/css-beautifier.html):** - Formats a CSS files with the chosen indentation level for optimal readability. Supports 4 indentation levels: 2 spaces, 3 spaces, 4 spaces and tabs.

* **[PRETTIER](https://prettier.io/):** - Prettier is an opinionated code formatter for HTML CSS JavaScript etc

* **[PEP8 COMPLIANCE CHECKER](http://pep8online.com/):** - A free tool to allow the user to check their python code, to ensure it conforms to the PEP 8 standard. 
 

___

## 🧑‍🎨 **UX:** **User Experience Design (UX)**

 __Developed from the coding institute full stack web developer module on UX design.__

**What is UX:**

User Experience Design is the work, processes and skillsets involved in creating useful useable products which provide value not only to the customer but the business owner ensuring that a product not only works but is intuitive, simple, and enjoyable to use. A good UX experience is achieved by following a defined process called User Centred Design or UCD for short.

I have chosen to create a Fight network with ecommerce and full C.R.U.D functionality and also login and registration forms, following best practice UX principals and will apply them to reassess the current needs and wants of my customers and future potential clients.

It will have the ability for users to register to the site upload their fighter data and create gyms if they own such facilities. 

With this full stack project i aim to cover all user stories and cover all of the planes of UX and development.



## 💡 **Strategy plane: The Initial idea.**
___
The basis behind Fytletic was to create a full stack Django web app which allows established and upcoming fighters from all disciplines a place to register their details online to create a fighter community and network. 

It’s prime function is to  provide a simple profile that fighters can create for themselves and keep it updated with all essential criteria linked to their profile(criteria which will be addressed in my models and schemas later). Creating a user based personal online fight CV. 
Not only that but Gym owners can create specific gym listings, showcasing their skills, facilities, opening hours and even link to fighters who train there.

A function which will be initially built in the first phase of production will also be a news center of sorts which registered users will be able to read, information will include nutrition advice, training tips, fight news and more. The data will be blocked for unregistered users however a small snippet somewhat like Medium may be enforced in order to encourage people to sign up to the site. 

The over all goal of the site is to become the worlds largest database of fighters, fight gyms and fight/Athelete information. 

There will be a merchandise shop and system in place using technologies for payment Gateway for example stripe. The webshop will track orders and link them to individuals profiles. Initially this service isnt needed to create the MVP however for an example of my developement skills i will include these models for this project version. 


As a developer and from a development standpoint my primary aim is to bring together many of the technologies I have learned so far to then use these technologies and comprehensively display data in a comprehensive and easy to digest manner. I aim to bring in user-generated data using forms (through an Add gym or fighter form page using Django FORMS) and python linked to Postrgres. Thus highlighting the many skills I have obtained during this course. 

 By completing a fully functioning profiling site, I will have demonstrated my experience in developing a Python-based web application with CRUD functionality.


 ## **About the business:**

The web application will be entirely online and is concerned with real-life professional and amateur fight profiles from users who can sign up to the site for zero cost to themselves, simply by registering for an account. The primary aim of the website is to display fight and gym profiles from users and allow them to display their achievements / stats and information to accomplish two things, 1. Exponential growth through sharing of the website and 2. Expand awareness of their profile as an athlete and fighter. This may be from using the web app to connect and reach out to other fighters, or use it as an online 'CV' to showcase their statistics. 

**Strategy to deliver above.**

* A clear and simple design starting with the Hero section displaying the Name and tag line to establish the message of the site.
In this case FYTLETIC - Professional Fight Network.


**Branding:** 


**Branding:**
* I own the domain name https://fytletic.com and my business name follows suit with the strapline and business idea name. Fytletic is a play on two words , Fighting and Athletic. I beleive Fytletic is an easily rememberable name which translates well to a brand name.

* Logo - will be a simple design based on the letter F and L . Or will be based simply on the business name of Fytletic.

**Strategy to deliver above.**

All of the below points should fulfil 'user first impressions' (see table below) and is especially important in our B2C business.

*	Develop a logo – which is simple but effective, based on the letters F and L  and try to symbolise a link between fitness, wellbeing and the relationship of the letters. See Logo on the deployed site for the final design. The logo will also act as a link back to the home page as common practice. Increasing credibility and trustworthiness.
After some developement, i have found that the best option for the logo is to use the Fytletic play on words, using a combination of Bold italic and thin variations of the “Montserrat” font, which subsequently is also used as the main type face of the web app, i feel this works as it adds to the simlistic approach to the branding of the site.

* A simple design structure with a navigation bar and side navigation on smaller screen resolutions accessible on every page will be essential for allowing users and readers to 'learn' the site and layout/functionality with ease. There should also be a home button/link on the logo for each page and subsequent back/return to the fighters and gyms profile. I will ensure that a back button is generated on each page so that the user doesn't have to use the browser back button as this is bad UX. 

*	Develop a professional colour scheme – check out competitors in not only UFC but other athletic based business websites. Use consistently throughout the site. For this colour scheme, I have gone with a dark blue and greys signifying trust, honesty and dependability, therefore helping to build customer and userbase loyalty, i also feel like i wanted the site to come across as a professional body. 

* I have also researched colour palettes and other brands before making any decisions on my final approach you can find that here: 


* **[PDF- Colour Pallete research.](LINK):**


*	Choose a font type for the project which reflects what we are trying to achieve – research other platforms and use similar fonts.  “Montserrat”  will be used consistently throughout this site. The logo and business name  will employ ‘Montserrat font’ consistently. Again I have used this method from my previous milestone projects as I feel in my portfolio I wish to create a style for myself, following on from similar design and practices.

*	Utilise the bootstrap card and grid system to display the user's fight and gym data in a logical and easy to ‘learn’ manner.

*	Develop a footer with info section or simple copyright info bar.


| User first impressions        | How to achieve          |
| ------------- |:-------------:|
| **_Does it look credible and trustworthy?_**  | Yes – through the colour palette, fonts,  logo, social proof of good quality control and reviews. |
| **_Does it offer what I want?_**  | Yes – Simple use of CRUD functionality and achieves only what is intended, users the ability to register to the site, add fighters, gym data and also edit and delete that data. Readers of the site can view fighter stats and gym data on the home page and view extended versions of the individual generated templated pages , with easy access back to the main home page and or relevant sections of the site they are on. |
| **_Does it look valuable enough for me to stay?_**  |.Professional design, clear and simple navigation, displayed is an easy to read manner. Mobile responsive. |
| **_Does it look valuable enough for me to return?_**  | Yes, free to use but professional design, deployed on a secure platform, quick responsiveness and easy to 'learn' with all features of a review site available |
| **_What actions can I take now?_**  | Users who aren't logged in will see a clear navigation item which says 'register' and also registered users will see an enhanced menu structure to allow them to use the site effectively |
| **_How do I learn more?_**  | An F.A.Q section on the site will be made available in the footer section to allow users to find the answers to their questions with relative ease  |
| **_How do I contact someone?_**  | Footer provides direct contact details for the webmaster. Similarly, a web form can be accessed from a menu item called 'Contact'|




