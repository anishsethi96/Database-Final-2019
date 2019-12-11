--create lookup table for zip, county, city etc
CREATE TABLE ZipLookup (
Zip_Code INT,
County Varchar (40),
City Varchar (60),
State Varchar (30),
PRIMARY KEY (zip_Code)
);

--create table for vehicle_Repair_shops
CREATE TABLE Vehicle_Repair (
facility_Number Varchar (30), 
facility_Name Varchar (110),
address Varchar (95),
facility_Zip Int,
owner_Name Varchar (75),
business_Type Varchar (90),
orignal_IssuanceDate Date,
last_RenewalDate Date,
expiration_Date Date,
PRIMARY KEY (facility_Number),
FOREIGN KEY (facility_Zip) REFERENCES ZipLookup (zip_Code)
);

--create table for NY food establishment's health violations
CREATE TABLE Food_Establishment (
Facility Varchar (70),
Address Varchar (65),
Total_Critical_Violations SMALLINT,
Total_Critical_Violations_Not_Corrected SMALLINT,
Total_Noncritical_Violations SMALLINT,
Description Varchar (75), 
Local_Health_Department Varchar (45),
Facility_Address Varchar (70),
Facility_Zip_Code INT,
Operation_Name Varchar (120),
Permit_Expiration_Date Date,
Permitted Varchar (125),
Permitted_Corporation_Name Varchar (150),
Permitted_Operator_Last_Name Varchar (50),
Permitted_Operator_First_Name Varchar (35),
NYS_Health_Operation_Id Int,
Inspection_Type Varchar (15),
PRIMARY KEY (NYS_Health_Operation_Id),
FOREIGN KEY (Facility_Zip_Code) REFERENCES ZipLookup (Zip_Code)
);

--create table for NY Liquor Authority Quarterly List of Active Licenses
CREATE TABLE Liquor_Licenses (
License_Serial_Number INT,
License_TypeName VARCHAR (35), 
License_Class_Code VARCHAR (3),
License_Type_Code VARCHAR (2),
Agency_Zone_Office_Name VARCHAR (13),
Agency_Zone_Office_Number SMALLINT,
Premises_Name VARCHAR (52),
Doing_Business_As VARCHAR (68),
Address VARCHAR (150),
Zip INT,
LicenseCertificateNumber INT,
LicenseExpirationDate DATE,
PRIMARY KEY (License_Serial_Number),
FOREIGN KEY (Zip) REFERENCES ZipLookup (Zip_Code)
); 

--create retail NY state retail food establishment table
CREATE TABLE Retail_Food_Stores (
License_Number INT,
Operation_Type VARCHAR (5),
Establishment_Type VARCHAR (10),
Entity_Name VARCHAR (45),
DBA_Name VARCHAR (45),
Street_Number VARCHAR (45),
Street_Name VARCHAR (45),
Zip_Code INT,
Square_Footage INT,
Retail_Address VARCHAR (255),
PRIMARY KEY (License_Number),
FOREIGN KEY (Zip_Code) REFERENCES ZipLookup (Zip_Code)
);



INSERT INTO ZipLookup(Zip_Code, County, City, State) VALUES (12223,'Albany','Albany','New York');
INSERT INTO ZipLookup(Zip_Code, County, City, State) VALUES (12229,'Albany','Albany','New York');
INSERT INTO ZipLookup(Zip_Code, County, City, State) VALUES (12227,'Albany','Albany','New York');
INSERT INTO ZipLookup(Zip_Code, County, City, State) VALUES (12107,'Albany','Knox','New York');
INSERT INTO ZipLookup(Zip_Code, County, City, State) VALUES (12240,'Albany','Albany','New York');
INSERT INTO ZipLookup(Zip_Code, County, City, State) VALUES (12230,'Albany','Albany','New York');
INSERT INTO ZipLookup(Zip_Code, County, City, State) VALUES (12239,'Albany','Albany','New York');
INSERT INTO ZipLookup(Zip_Code, County, City, State) VALUES (13762,'Broome','Endicott','New York');