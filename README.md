# American Express

I made this application on 24th June, 2017 for American Express Bank. They conducted an online competition where we have to build a web application in 12 hours. The goal of the competition was that the banker can search 6 months credit card statement of credit card holders by their ID. They provided a sample csv file of more than 1000 card holder's 6 months statements.

CreditCardStatement application is based on Python-3.4.1,Django-1.11.2,Twitter Bootstrap and sqlite

# Installation

To install the required libraries for this file, simply run the following:

    pip install -r requirements.txt


# Running the project

To run this project:

	# Navigate into directory containing manage.py
    cd AmericanExpress

    # Setup the database
    python manage.py migrate
    python manage.py makemigrations

    # Run the server
    python manage.py runserver

You can now visit the following URLS:

	* http://127.0.0.1:8000/CreditCardStatement/profile
	
