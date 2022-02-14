## Vet Project

### 1. Abstract

Vet project is an open to development project created using Django framework. The aim of the project is to create an interactive platform that includes a user model with login/register operations, login require and authorization mechanisms. It contains pages where users can post and view articles. 
People who will use this project can customize the project and develop it for their own use. 
The project can be run with the command `python manage.py runserver` without the need for any ide. 

The admin panel URL is "/admin" as in Django default. Admin panel login information is “id = admin, password = password”. For security reasons, these default settings must be changed before the project is published.
<br><br>

### 2. Requirements and Third-party Software Used 
<br>

#### 2.1. Django
The project was developed with Django v4.0.2 on Python v3.8
<br><br>

#### 2.2. Bootstrap and jquery
HTML pages were created using .css and .js files of Bootstrap v4.0.0 and jquery v3.2.1 software placed in the static folder. 
<br><br>

#### 2.3. Other Third-party Software / Dependencies


#### 2.3.1. Pillow

It is a Python display library for viewing images uploaded by users. 
Type the following command on the command line to install. 
<br>

`pip install Pillow`


#### 2.3.2. Django_cleanup

It is a auxiliary tool that allows users to delete the media that they upload via HTML pages from the static media folder in case they delete it later. 
Type the following command on the command line to install. 
<br>

`pip install django_cleanup`

#### 2.3.3. Django_phone_field

It is an auxiliary tool that organizes the appearance of the phone information that users share in their profiles. 
Type the following command on the command line to install. 
<br>

`pip install django_phone_field`

#### 2.3.4. Crispy Forms

It is an auxiliary tool used to make the pages that contain forms look neat. 
Type the following command on the command line to install. 
<br>

`pip install django-crispy-forms`

<br><br>
### 3. Methods
<br>

#### 3.1. Embedding Bootstrap Files in the Project 

Javascript and CSS files in Bootstrap are buried under the static folder within the project because it is not considered safe to call from outside the project. All the files that Boostrap needs are in the project.
The person who will use the project can use Javascript and CSS files manually by removing the boostrap links in the settings.py file.
<br><br>

#### 3.2. Templates Folder

All HTML codes used within the project are combined under templates folder. This folder interacts with the static folder.
<br><br>

#### 3.3. Collecting Project Files Under Statics Folder 

All files in the project are gathered under the static folder as suggested in the Django documentation. This folder ensures stable execution of files.
<br><br>

#### 3.4. Media Folder

Media files uploaded by users are saved in a folder named media. If users delete the article linked to this file, the associated file in the media folder is also deleted.
<br><br>

#### 3.5. Apps

#### 3.5.1. Apps Abstract

The project consists of three Django apps. These are contact, pets and user. These applications have their own models and URL patterns and work in conjunction with each other.

#### 3.5.2. Register and Login

Register and Login processes take place according to the models in the user app. After logging in, the user is authorized to see pages such as dashboard and can share articles.

#### 3.5.3. Dependencies Between Contact App and User App

After the registration process, the user can fill in the profile information and this information is saved in the contact model. The main reason why the detailed profile information of the user is saved in a different application than the user is to not manipulate Django's own user model so that the people who will develop on the project have a simple workspace. Both applications have their own model and are interactive with each other.

#### 3.5.4. Pet App

This application allows users to create a new article and view the articles. It is associated with the user application. It contains a model that will allow the user to create a pet post.
<br><br>

#### 3.6. Dashboard

Dashboard page allows users to create, view and update their own articles.
<br><br>

	
#### 3.7. Authorization

#### 3.7.1. Superusers

Only superusers have the authority to delete own articles. It also has the authority to update and delete all posts. It can display all pages.

#### 3.7.2. Users

Users can share. There is no authority to delete an article, Users can only update it. Users has the authority to view pages such as Dashboard and profile. 

#### 3.7.3. Visitors

They can not share. They can inspect public pages. If they try to access user pages with URL addresses, they will get HTTP protocol error codes.
<br><br>

### 4. Tests

4.1. Unit Tests

URL and model tests were performed in accordance with Django documentation. Test classes are available in test.py files. These tests are run with the following command.

`python manage.py test`

<br>

### 5. Security 

During the registration process, the user password is saved in the database by being encrypted with SHA-256. While the user is logging in, this password is resolved and the password is matched. No one except the user can know what the password is. While sending forms such as Register, Login, protection against “Man In The Middle” attack is provided by using CSRF token in accordance with Django documentation.
<br><br>

### 6. Product Stage 

Before the application is published, DEBUG mode must be turned off in `settings.py` and `ALLOWED_HOSTS` section must be set. In addition, the language and time settings to be used should be changed by the developer in the `settings.py` file.
Django security keys should be changed with a unique key.
Admin information must be changed and must have a password that is not written in the project.
The project can be run on the local server without the need for an ide, with a single command that `python manage.py runserver` in order to be able to review and develop even when debug mode is on.
<br><br>





	




