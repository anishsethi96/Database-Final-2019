# Final Project Anish Sethi and Ronald Joseph

This project is based around the concept of people coming to certain cities in New York for the first time and wish to look for Restaurants in the area, their violations (see zipcode which have a lesser avg violations per restaurant than their choice), license details, address and so on. They can also look for vehicle repair shops and on choosing a shop they are given an option to look for restaurants in the area, they can also search for retail stores to shop in and see what stores have a delivery truck option. The Liqour search option lets the users look for places that have a valid liqour license and can specify which type of liqour they are looking for (Beer, Wine and so on).

The enitre application is created using python and the data is stores in Postgres database and XML. The application.py file serves as the entry and exit points of the application whereas all database functionality is performed in the databse.py file.

## What's in the application

`Application.py` contains python code that enables users to enter the application and perfrom their search. It is also the exit point for the code.

`database.py` contains PSQL and Python code to fetch and execute queries and return them.

`data_load.py` it populates the Postgres database from the CSV format. This will load the CSV files to the concerned tables

`HW4-DBSchema-josepr_&_sethia` contains the PSQL code to create the tables with restraints based on zip code reference.

`XML Files` contains 5 XML files that contain some aspect of the CSV datasets and are merged with the PSQL to give varied results. Currenlty we only query Retail Store.XML and ZipLookup.XML but this can be easily scaled to all 5 XML datasets

`XSD Files` contains the XML schema and descriptions

## Setup

This relies on the [psycopg2](http://initd.org/psycopg/) module to connect to a Postgres database. You'll need to have that available when you run your python code.

It also relies on the XML.ETree.elementtree, eTREE from LXML modules for the connection to the non relational XML data.

The application expects a user named `postgres` (with password `qwerty4321`) to have full privileges to a database named `postgres` on `localhost`. You could also use whatever database and user you want if you change the `connection_string` variable in `restaurant_test.py`.)

## Running

Running the HW4-DBSchema-josepr_&_sethia.sql loads the CSV files to the postgres tables and creates the XML files as well

This repo has the retail and ziplookup XML files that are used. The others were too large I didn't push them as well, running the above mentioned sql file creates all the XML files.

From the a terminal (or command prompt) in the `sethia-josepr-final/` directory, you can run the application suite by running:

``` 
python application.py
```
