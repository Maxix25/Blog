# Forum
## How to run
  - First, clone the repository using ```git clone https://github.com/Maxix25/Forum.git``` and cd into the new folder using ```cd Forum```
  - Secondly, create a virtual environment using ```python3 -m venv env``` and activate it using ```source env/bin/activate```
  - Install the dependencies using ```pip3 install -r requirements.txt```
  - Commit all migrations to create the database using ```python3 manage.py migrate```
  - Generate the server's secret key using ```python3 generate_key.py```
  - Run the server using ```python3 manage.py runserver```
