# BLS Digital


Welcome to [BLS Digital](#)!

![Application on different screens](#)

## Contents
- [User Experience](#user-experience)
    - [User Stories](#user-stories)
    - [Agile Methodology](#agile-methodology)
    - [Wireframes/Flowchart](#wireframesflowchart)
    - [Design](#design)
- [Features](#features)
    - [Existing Features](#existing-features) 
    - [Future Features](#future-features)
- [Tecnologies Used](#technologies-used)
    - [Technologies Used](#technologies-used)
    - [Libraries](#libraries)
- [Testing](#testing)
- [Bugs](#bugs)
    - [Solved](#solved)
    - [Left to Solve](#left-to-solve)
- [Deployment](#deployment)
    - [To Deploy The Project](#to-deploy-the-project)
    - [Forking The Repository On GitHub](#forking-the-repository-on-github)
    - [How To Clone The Project](#how-to-clone-the-project)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)


## User Experience
### User Stories
#### Site User

#### Staff Memmber


[Back to top](#contents)
### Agile Methodology
#### GitHub Project Board


![Screenshot of project board](#)


[Back to top](#contents)
### Wireframes



### Database



### Design
#### Typography


#### Colors


![Colors](#)

[Back to top](#contents)
## Features
### Existing Features For All Users
#### Navigation Bar


[Back to top](#contents)
#### Home


[Back to top](#contents)
#### About


[Back to top](#contents)
#### Footer


![Footer](#)

[Back to top](#contents)
#### Login Page


![Login](#)

[Back to top](#contents)
#### Sign Up Page


![Sign up](#)

[Back to top](#contents)
#### Custom 404 Page


![404](#)

[Back to top](#contents)
### Existing Features For Staff Memebers
#### All Bookings


[Back to top](#contents)
#### All Users


[Back to top](#contents)
#### All Reviews


[Back to top](#contents)
### Future Features


[Back to top](#contents)
## Technologies Used
- [Django](https://www.djangoproject.com/) - A model-view-template framework used to create Locksmith Booking
- [Bootstrap](https://getbootstrap.com/) - A CSS framework used for the front end development.
- [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality of the website.
- [a11y](https://color.a11y.com/Contrast/) - Used to test the contrast and accessibility.
- [Gitpod](https://gitpod.io/) - Used to create and edit the website.
- [GitHub](https://github.com/) - Used to host the repository.
- [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal used to push changes to the GitHub repository.
- [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to test responsiveness and debug.
- [Balsamiq](https://balsamiq.com/) - Used to create the wireframes for the project.
- [Cloudinary](https://cloudinary.com/) - Used to host all static files and images.
- [Heroku](https://dashboard.heroku.com) - Used to deploy the website.
- [PEP8 Validation](http://pep8online.com/) - Used to validate Python code.
- [HTML Validation](https://validator.w3.org/) - Used to validate HTML code.
- [CSS Validation](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code.
- [JSHint Validation](https://jshint.com/) - Used to validate JavaScript code.
- [drawSQL](https://drawsql.app/) - Used to draw the database schema.

[Back to top](#contents)
### Libraries
The following libraries are used in the project and are located in the requirements.txt file.


[Back to top](#contents)
## Testing
### Validator Testing
Locksmith Booking have been tested by using validation tools for HTML, CSS, JavaScript and Python.
- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [JSHint JavaScript Validator](https://jshint.com/)

#### HTML Validation
![HTML](#)

#### CSS Validation
![CSS](#)

#### JavaScript Validation
![JS](#)

#### Python Validation
![Python](#)

[Back to top](#contents)
### Lighthouse Testing
The application has been tested with Chrome Dev Tools Lighthouse Testing which tests the application for:
- Performance
- Accessibility
- Best Practices
- SEO 

#### Home page
![Home](#)

#### About Page
![About](#)


[Back to top](#contents)
### Accessibility Testing
I checked so the contrast was enough on the site using [a11y](https://color.a11y.com/Contrast/).

![Contrast](#)

[Back to top](#contents)
### Responsiveness Testing
Test for responsiveness was made with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/).

[Back to top](#contents)
### Browser Testing


[Back to top](#contents)
### Manual testing


[Back to top](#contents)
## Bugs
### Solved


[Back to top](#contents)
### Left to Solve


[Back to top](#contents)
## Deployment
### To deploy the project
This application is deployed using [Heroku](https://heroku.com/).

- Before doing the following steps I created a env.py file in gitpod that contains the sensitive information that should not be pushed to github/heroku. And added that file to the .gitignore file.
- Created a Procfile so Heroku knows what kind of application it is.
- Created a requirements.txt file with all the necessary requirements for the app to run.

The steps for deploying through [Heroku](https://heroku.com/) is as follows:

1. Visit [Heroku](https://heroku.com/) and make sure you are logged in.
2. Click on New and then choose New App.

![First step](#)

3. Choose a name for your app and then choose your region.
4. Then press 'Create app'.

![Second step](#)

5. Make sure you are on the 'Deploy' tab.
6. Choose connect to GitHub account.
7. Search for your repository that you want to deploy.
8. Press 'Connect'

![Third step](#)

9. Choose if you want automatic deploys from your repository on GitHub.
10. Choose which branch you want to deploy.
11. Press 'Deploy Branch'.

![Fouth step](#)

12. When the installation is done. Go to the settings tab.
13. Press on 'Reveal Config Vars'.

![Fifth step](#)

14. Add config vars that are necessary. I'm not showing the keys beacuase they are secret.

![Sixth step](#)

15. Add the buildpacks needed.

![Seventh step](#)

16. Now you are done and can open the app!


[Back to top](#contents)
### Forking the repository on GitHub
A copy of the repository can be made. This copy can be viewed and changed on another account without affecting the original repository.

The steps for doing this:
1. Make sure you are logged in on GitHub and then find the repository.
2. On the top right there is a button called Fork.
3. Press the Fork button to make a copy to your account.

![Image showing how to fork](#)

[Back to top](#contents)
### How to clone the project
This is how you make a clone of the repository:

1. Click on the code tab under the repository name.
2. Then click on "Code" button to the right above the files listed.
3. Click on the clipboard icon to copy the URL.

![Imge that shows where to find the URL for cloning](#)

4. Open Git Bash in the IDE of your choice.
5. Change the working directory to where you want your cloned directory.
6. Type `git clone` and then paste the URL that you copied.
7. Press enter and clone has been finished.

[Back to top](#contents)
## Credits
### Content
- [Bootstrap](https://getbootstrap.com/) is used alot in this project when adding the design to the front end.

[Back to top](#contents)
### Media


[Back to top](#contents)
## Acknowledgements


[Back to top](#contents)