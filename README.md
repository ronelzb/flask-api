# flask-api
This Flask crash course is a basic introduction to the web framework and learn about basic data structure concepts at the very low level by building a Flask API with Python.

## Features
The data structures covered in this course are:
* Linked List.
* Hash Table.
* Binary Search Tree.
* Stacks and Queues.

An interesting feature in this course is the use of [SQLAlchemy](https://www.sqlalchemy.org/), an Object Relational Mapper which the goal is: to give application developers the full power and flexibility of SQL, and [Sqlite3](https://www.sqlite.org/index.html) to store the testing data.

## Installation
In order to install all the necessary pre-requisites you can do the following (I used Visual Studio Code but it can be easily developed in VIM):
* Install [Python](https://www.python.org/).
  * It is recommended to add Python to PATH.
  * Create a virtual environment or *venv* in your IDE project.
  * Activate the environment.
* Install [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/).
  * Flask can be installed using pip: `pip install Flask`.
* (Optional) if you're asked to update pip inside your virtual environment please read the answers of this [thread](https://stackoverflow.com/questions/15221473/how-do-i-update-upgrade-pip-itself-from-inside-my-virtual-environment) first, as I encountered a couple of issues there and my pip was removed in the process.
* Install [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/).
  * Flask-SQLAchemy can be installed using pip: `pip install flask-sqlalchemy`.
* Install [Sqlite3](https://sqlitebrowser.org/dl/) or download the portable version.
* And the last step (I know), is to download and install [Postman](https://www.postman.com/downloads/) to make dummy testing requests.

## Fork
This project and course is a fork from [selikapro repo](https://github.com/selikapro/FlaskDS) which did a great job putting this together and the best of all there is a [Youtube video](https://www.youtube.com/watch?v=74NW-84BqbA) where everything is explained step-by-step from the installation, configuration to the data structures used across the routes.