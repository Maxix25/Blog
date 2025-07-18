# Blog
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
<img width="1874" height="886" alt="image" src="https://github.com/user-attachments/assets/9ff7e7be-f665-4410-8c7d-736a59cc91c4" />

## Features
- Comment on posts
- Edit profile picture and user detials (bio, username, email)
- Login and Register
- Unit tests

## How to run
  - First, clone the repository using ```git clone https://github.com/Maxix25/Blog.git``` and cd into the new folder using ```cd Blog```
  - Secondly, create a virtual environment using ```python3 -m venv env``` and activate it using ```source env/bin/activate```
  - Install the dependencies using ```pip3 install -r requirements.txt```
  - Commit all migrations to create the database using ```python3 manage.py migrate```
  - Generate the server's secret key using ```python3 generate_key.py```
  - Add a line to the ```.env``` file and set the timezone appending ```TIME_ZONE=<your_timezone>```, you can find your time zone <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank">here</a> an example is `America/Santiago`
  - Run the server using ```python3 manage.py runserver```

## How to run (Docker container)
  - Run ```docker compose up -d --build```
  - Now you can access the server on http://127.0.0.1:8000/

## Creating superuser
  - To create a superuser use the command ```python3 manage.py createsuperuser```
  - Choose a username and password and you can now login in /admin

## Routes
  - ```/```: Home page
  - ```/admin```: Admin panel
  - ```/auth/login```: Login page
  - ```/auth/register```: Register page
  - ```/auth/logout```: Logout page
  - ```/posts/create```: Create a post page *Login Required*
  - ```/posts/view/<int:post_id>```: Given an post ID, view the post
  - ```/posts/post_comment```: Comment on a post *Login Required*
  - ```/profile/settings```: Settings page *Login Required*
  - ```/profile/<int:user_id>```: Given an ID, view the user's profile
  - ```/404```: 404 page

## Before pushing changes
  - Test the app using ```python3 manage.py test```
  - If all the tests succeed you can push your changes using ```git add <files>```
  - Commit and push your changes using ```git commit -m <commit_message>``` and ```git push origin <your_branch>```

