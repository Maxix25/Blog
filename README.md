# Forum
## How to run
  - First, clone the repository using ```git clone https://github.com/Maxix25/Forum.git``` and cd into the new folder using ```cd Forum```
  - Secondly, create a virtual environment using ```python3 -m venv env``` and activate it using ```source env/bin/activate```
  - Install the dependencies using ```pip3 install -r requirements.txt```
  - Commit all migrations to create the database using ```python3 manage.py migrate```
  - Generate the server's secret key using ```python3 generate_key.py```
  - Add a line to the ```.env``` file and set the timezone appending ```TIME_ZONE=<your_timezone>```, you can find your time zone [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
  - Run the server using ```python3 manage.py runserver```

## Creating superuser
  - To create a superuser use the command ```python3 manage.py createsuperuser```
  - Choose a username and password and you can now login in /admin

## Routes
  - ```/```: Home page
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
  - Commit and push your changes using ```git commit -m <commit_message>``` and ```git push origin master```
