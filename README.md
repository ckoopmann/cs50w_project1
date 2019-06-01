# Project 1

## Overview
This repository contains the code for project 1 in the edx course CS50 - Web Programming.

The code for the application itself is packaged in a package called `application` in a directory of the same name.

## Requirements
* Python 3.6+
* Flask
* Flask-Session
* Flask-Login
* Flask-SQLAlchemy
* Flask-Bcrypt
* Flask-Wtf
* requests
* simplejson
* SQLAlchemy


## Run the application

To run the flask application all you have to do is:
Install the requirements:

`$pip install -r requirements.txt`

and run the application using the run script:

`$python3 run.py`

## Usage

When you visit the index route of the running application at  `http://localhost:5000/login`
without being logged in you will be redirected to the log in page. In the navigation bar you can find the link to the register section where you can register a new user account.

After registering you can go back to the login page and log in. After succesfull log in you will be redirected to the search mask for the book search. There you can search for a book by author, title and isbn. The search will be done matching on all filters that were entered simultaneously (via SQLs 'AND'). The individual filtering is done using SQLs `LIKE` keyword with `%` wildcard characters before and after each argument. For example if you enter 'William' for author and '1' as ISBN it will match all books whose author contains 'William' and whose ISBN number contains at least one '1'.

If you click the title of any search result you will be redirected to that books detail page containing past reviews, goodreads avg. score as well as the input form to submit a review yourself.

## Import Books
To import the books from `books.csv` into the database all you have to do is:

`$ python3 import.py`

Note however that if you run this script multiple times the same book will have multiple entries in the database (with different values for the autoincrement primary key id column).
