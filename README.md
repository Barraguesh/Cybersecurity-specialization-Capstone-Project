# NotSignal, a secure web chat messenger!
#### Capstone project of the 4 course specialization by the University of Maryland.

# Project evaluation
Public server located at http://34.245.84.230:8000

The database dump is at http://34.245.84.230:8000/dbdump

When resetting your password, it's gonna send the supposed email (if you enter a correct email address) to the page http://34.245.84.230:8000/email. This can be accessed easily by a button on the bottom of the login page (scroll to see). This is done because I didn't want to setup a mail server. All of this is prompted when going to reset the password but I comment it here as a reminder. Good luck everyone and thanks for reviewing my project!

# Building and testing

## Requirements
* Docker (have it running `systemctl start docker`)
* Docker-compose
* Python 3.6 (Django cryptography doesn't work correctly in 3.9 at this time)

## Development
Use `docker-compose.yml` for development, it uses the Django built in `runserver`. 

The application is already setup for development, but you need to create a `db.sqlite3` file in the root of the Django app.

Once the server is up and running, we need to create the database, Django makes it easy. Run the migrations:

`sudo docker-compose exec notsignal python manage.py migrate`

Now create a superuser:

`sudo docker-compose exec notsignal python manage.py createsuperuser`

## FAQ
* I f*cked up! How do I remove everything inside the containers? Check the containers ID with `sudo docker ps -a` and delete them with `sudo docker stop IDhere otherID`. Then proceed to nuke everything inside of Docker (WARNING THIS WILL REMOVE ALL CONTAINERS AND DATA) with `sudo docker system prune -a`. Yes this has happened to me so much that I needed to do a FAQ to remember it.

