# Developer Installation

* Python 3 and pip are required.
* Change to the ``service`` directory.
* Install the project dependencies:

``pip -r requirements.txt``

* Install the project source:

``pip install -e .``

* Populate the database. This needs to be done prior to the first installation
  and on any subsequent database schema change. From a fresh checkout, sqlite
  will be used; an external database is not needed.

``python manage.py migrate``

* To run the server:

``python manage.py runserver``

