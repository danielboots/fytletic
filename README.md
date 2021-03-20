# **Milestone Project 4**  - Full Stack. 

## **Fytletic - Fighter Networking Solution**

![Ftyletic logo and strap line ](static/img/responsive.png)

![index gif](Link)
![user gif](link)

Fytletic is currently deployed and can be visited directly at Heroku **[Fytletic  ](https://fytletic.herokuapp.com/)**



###  **For testing the following login and test card credentials are valid:**


**Member Login**
- Username: fytletic_test
- Email: test@fytletic.com
- Password: fyt_001

**Card payments**
- Card number: 4242 4242 4242 4242
- Zip & CCV: any integer values are valid



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
* I own the domain name https://fytletic.com and my business name follows suit with the strapline and business idea name. Fytletic is a play on two words , Fighting and Athletic. I beleive Fytletic is an easily rememberable name which translates well to a brand name.

* Logo - will be a simple design based on the letter F and L . Or will be based simply on the business name of Fytletic.

**Strategy to deliver above.**

All of the below points should fulfil 'user first impressions' (see table below) and is especially important in our B2C business.

*	Develop a logo – which is simple but effective, based on the letters F and L  and try to symbolise a link between fitness, wellbeing and the relationship of the letters. See Logo on the deployed site for the final design. The logo will also act as a link back to the home page as common practice. Increasing credibility and trustworthiness.
After some developement, i have found that the best option for the logo is to use the Fytletic play on words, using a combination of Bold italic and thin variations of the “Montserrat” font, which subsequently is also used as the main type face of the web app, i feel this works as it adds to the simlistic approach to the branding of the site.

* A simple design structure with a navigation bar and side navigation on smaller screen resolutions accessible on every page will be essential for allowing users and readers to 'learn' the site and layout/functionality with ease. There should also be a home button/link on the logo for each page and subsequent back/return to the fighters and gyms profile. I will ensure that a back button is generated on each page so that the user doesn't have to use the browser back button as this is bad UX. 

*	Develop a professional colour scheme – check out competitors in not only UFC but other athletic based business websites. Use consistently throughout the site. For this colour scheme, I have gone with a dark blue and greys signifying trust, honesty and dependability, therefore helping to build customer and userbase loyalty, i also feel like i wanted the site to come across as a professional body. 


- After researching other fitness and fighting related sites combined with reading this medium article [How to use color Psychology ](https://medium.com/@jelly.shah/how-to-use-color-psychology-to-create-a-perfect-fitness-website-7e9f200c7f16), I developed the colour pallete below  using [Adobe Colour Pallete](https://color.adobe.com/create). 

* I have also researched colour palettes and other brands before making any decisions on my final approach you can find  the extra infomation on that research here: 

* **[PDF- Colour Pallete research.](/media/fytletic_research.pdf):**

**Final Colour Pallete**

![Colour Pallete ](media/colour.png)

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


**What is culturally appropriate**

As this is primarlily a fighter and gym network  I have found that the brand name stands for a lot right from the offset. Our website is only concerned with displaying information within the fight (for example UFC / Boxing) industry, and the fitness industry. We will not be extending our reach in to other similar industries for example cooking (which may be related to nutrition and fitness)


We keep the site strictly about professional organised and amateur fighting  and focus solely on providing the users with the ability to create their professional online CVS , edit and delete them. They will also be able to build up their name as an athlete and fighter. 
By giving the user the ability to update their own profiles, it is encouraging to the user to frequent the site and keep the data being stored about them up to date, including contact details, fight statistics training regimes etc. So again allowing us to create a self building site of relevant user generated content. Not only that but by building on a Django base alongside python we can ensure that we can consistently keep adding improvments and features which users may want and request, for example a follow or messaging service, this allowing users to contact each other and stay on the platform.

I have also developed the site to be mobile-first as our demographic for clients looking for our services seems to be in the male category and age range of 16-34, whereby we know its highly likely that users have access to a smartphone and will be accessing our website from mobile.



**Tracking and cataloguing content in an intuitive way.**

Regarding the display of the content I have opted for a typical section style layout to the site, this meaning I have a hero section and subsequent blocks of content each separated by alternating background colours, an off white and white to ensure content separation is apparent. 

The use of Djngo /Python for loops will allow the display of user generated content in a card, each iteration will generate a new card with the subsequent fighter name image and more button. In time I may break these loops down to fighter Discipline specific headings, for example Boxing, UFC  and even make fighters and gyms searchable by these extended options, however as the site is in its infancy I have opted to generate all reviews in cards utilising the bootstrap grid system displaying no more than three cards per row, time permitting i may employ a pagination system, instead of generating long loops of data.

Typically in modern web design, a hero section is employed so I have taken advantage of that with a centred H1 and H2 Heading for the site title and strapline, using a more bolded font to make an impact from the first-page load. This screams to the user, this is the site title and this is what you can do here.

I also used a background image which is relevant (in this case a glove on rope) to display the field the website is addressing (fighting /combat of some description). One concern is that on fighter profiles, if a user uploads a  bright image it may distract  from the Hero text, so a background overlay maybe used in order to fix this. At present i havent employed this on user generated data however with keeping to the branding pallete of the site i have employed an overlay system on the main navigation hero sections.  Not only that but the background overlay is the main colour in the colour palette chosen again adding to our branding and overall UX experience for the potential client.

**What is the importance of this.**

* From the first time the user visits the website we want to display a level of professionalism and ease of use, not only that our straplines, branding and colour palettes are correct but our content is distraction-free and displayed easily enough that a user can learn about our website and feel at ease very quickly. 

* With minimal distractions and a simple interface, it will become easy for the user to quickly learn the site and sign up for an account and start creating custom content for the site. 

**Why would a user want this.**

 Its important to quickly allow the user to learn the site sign up and create content with little distractions as possible. I have deliberately simplified the application to allow for this. After re watching the sections on development of software i have become well aware of the YAGNI  and KISS principles, this i have designed the site to be deliberatly simple and learned easily by any kind of user.  Typically a user from visiting the site can sign up and create their fighter profile in less than 5 steps. 

1. Visit the application 
2. Click Register
3. Register account.
4. Click claim fighter profile. / gym profile (limited to one fighter and gym profile per registered user.)
5. View Published profile. 

This ease of use and free registration will encourage return users to the platform and again allow users to grow through external content creation. 


**What creates a good User Experience concerning this online Fighter and gym profile business.**

*	Strong branding – colour palette – typical industry typography.
*	Displaying relevant content. - From only hosting/allowing correct and verified data from users and displaying content which is of value to readers.
*	Social proof – adding social sharing to all fight and gym submissions allows for users to share their profiles and in return increases traffic to our web application.
*   Overall ease of use, as highlighted above, the 5 steps from learning the site to publishing is imperative. I have used previous sites which require far more effort and are often more complicated to learn. Simplicity is key.


**What does the user/client expect?**

*	Strong Branding- Does this website come across as an authority in its field. I feel this is true by the use of correctly structured content, branding font type and also consistency throughout.
*	Pricing – This is completely free, we may in our terms allow free use to contact users at a later date to offer other premium services. 
*	Ease of use? - 5 steps from initial visit to signing up and publishing the first review.
* Support - this is currently only available from a contact form, however as the site is simple and efficient I believe this is a minor addition to the free service provided. 



**Prioritisation – To launch a Minimal Viable Product.**

We can address which features should be prioritised primarily by developing a map of importance and viability/ feasibility.
For this project, we will be focusing on UX efforts of higher importance and developing features of lower importance and viability/feasibility further in the timeline of this project.


| Opportunity/Problem       | Importance         | Viability  |
| ------------- |:-------------:| -----:|
| **_A.     Allow users to register and create publishing account_**       | 5 | 5 |
| **_B.     Display each review on their own page_**      | 5      |   5 |
| **_C.     develop a follow /twitter type system for users to follow each other_** | 3      |    2 |
| **_D.     _** | 2      |    3 |
| **_E.     Group fight profiles to categories_** | 3      |    2 |


**Graph of importance to launch our MVP from the previous table.**

![Fytletic MVP prioritisation ](###)


As referencing the above prioritisation matrix my UX efforts will be hence focused on areas A and B which will satisfy the CRUD app criteria of the grading process. 
Thus I will develop the application to allow users to register and create their accounts whilst also displaying their profiles for fighters and gyms. 


## 🧰 **Scope Plane - requirements and functional specifcation**
___
### **What users and stakeholders - Say they need**
**User Stories**


* Speaking to several professional and unprofessional fighters from a number of disciplines, I concluded that they want somewhere which provides the correct tools such as their own personal branded page to display their fighter stats and data, not only do they want this for their own record keeping, but they feel it would be a great tool to expand their network and gain exposure, an online fighters Cv as it were, they also would like to create their own blogs and news, which could then be associated to their own public channel. 

* Again this helps with their self promotion and ability to gain better exposure in order to promote themselves within the fight world as this is a crucial step in helping them progress with their career endevours. 

* The user visiting this type of website wants a professional website easy to navigate and also read profiles of upto date and relevant content, for in this instance - Other like for like fighters or gyms which suit their fighting expertise. 


* They need to be able to to search for these gyms and fighters the user can increase their network and make connections which would have previously not been available to them. 

* Not only that but if the user wishes to use the site to publish their own news reports they will also require a site that will allow full CRUD functionality, simplistic to use and allow their content to be displayed in an easy to read and eye inviting manner. 

* They need to be able to share their work across platforms. 


### **What users and stakeholders - Actually need**
They need a clean and tidy designed website which is mobile responsive, highlighting the latest fighters, gyms and up to date news and information. A button from the front page known as a CTA will take them straight to the latest updates for the site, this was a primary reason for including entries in the database models such as profile CREATED on, so this is possible from the beginning of production.

* As a user/publisher on the site, they require ease of use with full CRUD functionality, to publish amend or even delete their fighter profile stats and associated information. 

* They will also need a means of sharing said content with others on their social networks or to potential sponsors. 

### **What users and stakeholders - Don't know they need.**

* As the site owner, they will want to be able to monitor and update the site, I have initially started this process by creating an admin user who can create new entries for all applications in a customised and ordered backend admin area, this can be found by logging in as the super user and navigating to the admin panel. 

* As a working business website, we have to abide by GDPR rules, so a pop up advising the client on our privacy and how we use their information would be needed down the production line. This production app will not have this in place but will be if deployed.

* Other desirable features may include, more services for advertisement and online merchandise store with inventory (at current the shop functions as a working shop but doesnt fulfil orders.)

* Social networking feature – not essential but desirable, perhaps a Twitter/Facebook like entity where users can register to the site share their tips and advice, this would allow for content to be shared cross-platform and to other social media accounts, drastically increasing awareness of our web application. Or for people to use the site as a personal fight blog, create friends and discover shared interests. Being able to interact with other users on the site i feel would drastically improve the useablility of the site in general.

* Figher connections and online status - being able to chat and speak with online fighters will create more of a network feel to the site unlike a database of fighters, i feel the two would work well together.

* An iOS and android app – it is true that many users now if these features down the line are implemented that developing an application would be of extreme benefit, it would allow extra monetisation brand awareness and next-level professionalism.


## User Stories continued - table ammended  and added to from user stories set out in **_Project ADO_**


|                   | As a     | I want to...                                              | So that..                                                                                       |
|--------------------------------|--------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| **_Viewing and Navigation_**         |              |                                                                     |                                                                                                      |
| 1                              | Site Visitor | Discover Fytletic                                   | Learn more about what the website plans to achieve - Fighter and Gym Profiles alongside news and fitness information.                                                |
| 2                              | Site Visitor | View a list of products                                             | Select a product to view more details                                                                |
| 3                              | Site Visitor | View a list of Fighters and Gyms                                          | Select a fighter or gym to view more details to learn more about that fighter or gym.                                                           |
| 4                              | Site Visitor | View a specific category of products using search functionality                              | Quickly find products I’m interested in without having to search through all the available products on the site, this will initially be grouped in to order by price and search by category.
| 5                              | Site Visitor | View individual product details                                     | Identify the description, price, available sizes, product image, and rating, being able to add them to the basket which keeps a running total of the basket.                           |
| 6                              | Site Visitor | Access up to date fighter and gym profiles                                    | view the latest and upto date infomation, use Fytletic as a reliable source of fighter stats.                                        |
| 7                              | Site Visitor | Easily access a contact page or F.A.Q section                                      | Send a message or read already answered questions regarding any queries I have.                                                      |
| 8                              | Site Visitor | See  ratings on products                 | Be reassured that the product is good                                                      |
| 9                              | Site Member  |          |                            |
| 10                             | Site Member  | Access a member only news desk                                                              | Read members only content, to keep uptodate with the latest news fitness advice and infomation all from one account.                                    |
| **_Registration and user accounts_** |              |                                                                     |                                                                                                      |
| 11                             | Site Visitor | Easily register for an account                                      | Have a personal account and be able to view my main profile, add a public figher or gym profile, so that i can manage my relevant fight data quickly and easily.                                               |
| 12                             | Site Visitor | Receive an email confirmation after registering                     | Verify that my account registration was successful                                                   |
| 13                             | Site Member  | Easily login or logout                                              | Access my personal account information, update that infomation and logout securely not only regarding login but adding a query to see if i really want to logout, instead of mistakes.                                                              |
| 14                             | Site Member  | Easily update my personal details                                   | Update profile details as expected, add a fighter profile or gym detail.                                                                       |
| 15                             | Site Member  | Easily recover my password in case I forget it                      | Recover access to my account and prevent others from claiming my account.                                                                        |
| 16                             | Site Member  | Have a personalised user profile add a public fighter profile (if a fighter)                                   | View my personal order confirmations, order history and save payment details for future purchases such as membership fees and to link this to my fighter profile where i can display public infomation about myself if i am a fighter professional.|
| 17                             | Site Member  | Enable my details to be prefilled                                   | Save time entering my details when making future purchases                                          |
| **_Sorting and Searching_**          |              |                                                                     |                                                                                                      |
| 18                             | Site Visitor | Sort and filter the list of available products and memberships (in production)                | Find the products suitable to which i require.                                                            |
| 19                             | Site Visitor | Search the site by keywords                                         | Easily find what I am looking for using keyword queries, such as 'protein powder'                                                                   |
| 20                             | Site Visitor | Easily see what I’ve searched for and the number of results         | Quickly decide whether the product is available                                  |                                                                                |
| **_Purchasing and checkout_**        |              |                                                                     |                                                                                                      |
| 21                             | Site Visitor | Easily select the size and quantity of a product with sizes, for example t-shirts and ensure that its available before adding to basket  | buy the correct products the first time, and not have to send an incorrect sized product back.                              |
| 22                             | Site Visitor | View items in my bag to be purchased                                | Identify the total cost of my purchase and all items to be ordered.                                  |
| 23                             | Site Visitor | Adjust the quantity of individual items in my bag                   | Easily make changes to my purchase before checkout                                                   |
| 24                             | Site Visitor | Easily enter my payment information and feel my personal and payment information is safe and secure                                  | Check out with the correct relevant card and billing  needed to make a purchase, processed through a third party payment gateway called Stripe.                   
| 25                             | Site Visitor | View an order confirmation after I checkout                           | Verify that the order has been accepted and is correct                                                            |
| 26                             | Site Visitor | Receive an email confirmation after checking out                    | Recieve an email confirmation of what I’ve purchased and any other relevant infomation which may be needed for future reference.                                         |
| **_Admin and Store Management_**     |              |                                                                     |                                                                                                      |
| 27                             | Site Owner   | Add a product                                                      | Add new products to the store                                                                                  |
| 28                             | Site Owner   | Edit/Update a product                                              | Change product prices, descriptions, images, and any other details which are relevant.                             |
| 29                             | Site Owner   | Delete a product/programme                                                    | Remove items that are no longer available                                                 |
| 30                             | Site Owner   | Add a blog                                                          | Add new blogs to share with site members                                                        |
| 31                             | Site Owner   | Links to Social Media                                | To connect with our clients  using already established social networking sites                                                       |

| 32                             | Site Owner   | Develop the site in to a networking site                                 | To allow users of the site to gain ever increasing exposure to their profiles, giving them a chance of making a career out of their ability. |

| 33                             | Site Owner   | Provide support for fighers and gyms to grow the network                                 | To encourage on boarding of investors and sponsorship. |




**First-time visitor Goals**

* Allow visitors to learn that the site is a Fighter and Gym Network.
* Home screen prompting registration if logged out. 
* See snippets and general rating of latest created or top fighters and Gyms on the home page.

**Frequent visitor Goals**

* Encouragement to register for more functionality, such as adding profile and writing news topics.
* Read and learn more about the Fighters and gyms on the site.
* Share these profiles on other social media outlets increasing site and fighter exposure.
* Publish their fighter news complete with CRUD functionality so the ability to edit and delete if needed (encouraging publication as can be deleted if not confident)


**Development Goals**

* Demonstrate a solid foundational knowledge of the Python language and the Django framework.
* Increase knowledge of Postrgres and also database relationships in general through CRUD dev and Django models. 
* Learn more indepth about Model View Controller and increase my ability to follow the YAGNI and KISS principals.
* Build up a portfolio of relevant projects suited to my needs  

**Website owner Goals**

* Encourage site use and exposure from allowing sharing and having a site that is easy to learn and use. Simple and effective interaction. 
* Fewer steps to publishing as possible vs competitors. 
* Easy registration to onboard new fighters and gyms, allowing for exponential growth through 3rd party content creation.



## 🏗️ **Structure: How we present information:**
___

The web application will consist of typical navigation and structure which will conform to web best practices. By this, we would expect the navigation menu items to be located to the top right-hand corner of the web app. To the left, we will employ a Navigation bar logo which doubles as the main Home or index.html link.