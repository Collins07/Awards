# Awards

This is a Django project was generated with [Python](https://www.python.org/) version 3.9


## Author's Name
Collins Nyakoe
 

## Table of Contents

+ [Description](#description)
+ [User Story](#user-story)
+ [Requirements](#requirements)
+ [Project setup instructions](#project-setup-instructions)
+ [Technology Used](#technology-used)
+ [Reference](#reference)
+ [Live Link](#live-link)
+ [Contact Information](#contact-information)
+ [Licence](#licence)


## Description
This is a web app that enables users to post their projects, view the projects and rate them in 3 different categories. A user is also able to view their own profile and other users' posts as well us rate them too. The projects posted have a date and time posted and a button to view the project through a redirector link.

The app has`template` folder where the markup langauge is written, a `static` folder where
the stylesheet is stored and media files and the `manage.py` file where the main function is run. Other severall python files too that are used to import data

<p>The images, description,date and unique ID are stored and managed in a database</p>


## User Story  
  
* Sign in to the application to start using.  
* Upload a pictures to the application. 
* Search for different users using their usernames.  
* See your profile with all your pictures.  
* Follow other users and see their pictures on my timeline.  
* Leave a comment on posts. 

[Go Back to the top](##Table-of-Contents)


### Requirements

* A laptop or a desktop computer

* An access to the reliable Internet connection


## Project setup instructions
1. Pull project from github Repository.

```bash
git clone https://github.com/Collins07/Awards.git
``` 
2. Move to the folder and create a virtual environment
3. Install requirements
  ```bash
  pip install -r requirements.txt
  ```
4. Create a new postgress database

5. Make migrations on postgres using django
    ```bash
    $ python manage.py makemigrations <database name>
    ```
    ```bash
    $ python3 manage.py migrate
    ```
6. Run the application
    ```bash
    $ python3 manage.py runserver
    ``` 
5. Open the application on your browser `http://127.0.0.1:8000/`

[Go Back to the top](##Table-of-Contents)





## Technology Used
* [Python3](https://www.python.org/)
* [Django3.2.2](https://docs.djangoproject.com/en/3.2/releases/3.2.2/)
* [Heroku](https://heroku.com)


## Reference

* python official website ```https://packaging.python.org```

* Programming with Mosh

* Code With Harry (youtube channel)
[Go Back to the top](##Table-of-Contents)


##  Live Link  
 Click [View Site]()  to visit the site

 [Go Back to the top](##Table-of-Contents)

## Contact Information 
Any query? Contact me at [collinsabaya07@gmail.com]


## Licence

MIT License

Copyright (c) [2022] [Collins07]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
[Go Back to the top](##Table-of-Contents)