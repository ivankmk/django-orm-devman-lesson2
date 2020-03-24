# Bank Security Control Panel

This is an internal repository for the staff of the Shining Bank. If you accidentally got into this repository, then you will not be able to start it, because you do not have access to the database, but you can freely use the layout code or see how the database queries are implemented.

Security desk is a site that can be connected to a remote database with visits and pass cards of employees of our bank.

# Requirements

 - Python 3.7
 - For packages, please execute: ```bash pip install -r requirements.txt```

 # How to get an access
 Request access to the database from your bank manager. To access you will need a host, port, engine, name, user and password. You need to keep this value-pair data in environment ``` .env``` file.


 # How to launch

 ```bash
  $ python manage.py runserver 0.0.0.0: 8000
 ```


# Project Goals

Accountant Valentin has been with the bank for 15 years. And he knows for sure: the best way to prevent financial losses is to closely monitor employees and their operations. - [DEVMAN.org](https://dvmn.org)