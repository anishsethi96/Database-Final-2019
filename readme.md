# Final Project Anish Sethi and Ronald Joseph

This project is based around the concept of people coming to certain cities in New York for the first time and wish to look for Restaurants in the area, their violations (see zipcode which have a lesser avg violations per restaurant than their choice), license details, address and so on. They can also look for vehicle repair shops and on choosing a shop they are given an option to look for restaurants in the area, they can also search for retail stores to shop in and see what stores have a delivery truck option. The Liqour search option lets the users look for places that have a valid liqour license and can specify which type of liqour they are looking for (Beer, Wine and so on).

The enitre application is created using python and the data is stores in Postgres database and XML. The application.py file serves as the entry and exit points of the application whereas all database functionality is performed in the databse.py file.

## What's in the application

`Application.py` contains python code that enables users to enter the application and perfrom their search. It is also the exit point for the code.

`database.py` contains PSQL and Python code to fetch and execute queries and return them.

`data_load.py` it populates the Postgres database from the CSV format. This will load the CSV files to the concerned tables

`HW4-DBSchema-josepr_&_sethia` contains the PSQL code to create the tables with restraints based on zip code reference.

## Setup

This relies on the [psycopg2](http://initd.org/psycopg/) module to connect to a Postgres database. You'll need to have that available when you run your python code.

It also relies on the XML.ETree.elementtree, eTREE from LXML modules for the connection to the non relational XML data.

The application expects a user named `postgres` (with password `qwerty4321`) to have full privileges to a database named `postgres` on `localhost`. You could also use whatever database and user you want if you change the `connection_string` variable in `restaurant_test.py`.)

## Running

From the a terminal (or command prompt) in the `sethia-josepr/` directory, you can run the application suite by running:

``` 
python application.py
```