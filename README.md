# App Manager

### Description
The purpose of this app is to provide a birds eye view of an orgs dependency architecture. What does that mean?
Take the CoLab homepage colab.duke.edu for example.
* I want the app to tell me all the tech it uses (Ruby,Rails, Postgres, etc.).
* I want to know who maintains the app both technically (CoLab Dev Team), and functionally (Academic Tech)
* I want to know what other app/infastructre this depends on (e.g. it relies on Shibboleth to login, grouper for permissions, etc.)
* I want to be able to search apps (group, developer, tech, common dependency, etc.)
We want this to be used by the greater Duke OIT, BUT (and this is important) we want to be able to be agnostic about institution. So think about authentication.



### How to run the project locally.
- Clone the project using either SSH or HTTPS links made available to you on gitlab

#### Without Docker
##### Frontend Application
- change the directory to the frontend `cd frontend`
- Install dependencies. run `npm install`.
- start the app. run `npm start`

##### Backend Application
- change the directory to the frontend `cd backend`
- create a virtual environment `python3 -m virtualenv venv`
- Install the requirements `pip install -r requirements.txt`
- to start the app without docker run `python3 manage.py runserver`

#### With docker
##### Frontend Application
- change the directory to the frontend `cd frontend`
- build an image `docker build -t am:frontenddev . `
- run the image `docker run --publish 3000:3000 am:frontenddev`

##### Backend Application
- change the directory to the backend `cd backend`
- build an image `docker build -t am:backenddev . `
- run the image `docker run --publish 8000:8000 am:backenddev`

#### How to update the database after making changes to the models
- First check if there are any migrations to apply `python manage.py showmigrations`
- If there are empty [] without [*] then apply migrations with `python manage.py makemigrations`
- Then apply the new migrations to the database with `python manage.py migrate`
