import psycopg2
import pandas as pd
from dicttoxml import dicttoxml

filename = "ZipLookup.csv"
# Read in the data
data = pd.read_csv(filename)
# Convert dataframe to dictionary object
data_dict = data.to_dict(orient="records")
# Convert dict to XML,
xml_data = dicttoxml(data_dict).decode()
# Load XML to file
with open("ZipLookupXML.xml", "w+") as f:
    f.write(xml_data)

# hold filename
filename = "Vehicle_Repair.csv"
# Read in the data
data = pd.read_csv(filename)
# Convert dataframe to dictionary object
data_dict = data.to_dict(orient="records")
# Convert dict to XML,
xml_data = dicttoxml(data_dict).decode()
# Load XML to file
with open("Vehicle_Repair_XML.xml", "w+") as f:
    f.write(xml_data)

# hold filename
filename = "Food_Service_Establishment__Last_Inspection.csv"
# Read in the data
data = pd.read_csv(filename)
# Convert dataframe to dictionary object
data_dict = data.to_dict(orient="records")
# Convert dict to XML,
xml_data = dicttoxml(data_dict).decode()
# Load XML to file
with open("Food_Establishment_XML.xml", "w+") as f:
    f.write(xml_data)

# hold filename
filename = "Liquor_Authority_Quarterly_List_of_Active_Licenses.csv"
# Read in the data
data = pd.read_csv(filename)
# Convert dataframe to dictionary object
data_dict = data.to_dict(orient="records")
# Convert dict to XML,
xml_data = dicttoxml(data_dict).decode()
# Load XML to file
with open("Liquor_Licenses_XML.xml", "w+") as f:
    f.write(xml_data)

# hold filename
filename = "Retail_Food_Stores.csv"
# Read in the data
data = pd.read_csv(filename)
# Convert dataframe to dictionary object
data_dict = data.to_dict(orient="records")
# Convert dict to XML,
xml_data = dicttoxml(data_dict).decode()
# Load XML to file
with open("Retail_Food_Stores_XML.xml", "w+") as f:
    f.write(xml_data)
