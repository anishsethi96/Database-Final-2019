import psycopg2
import psycopg2.extras
import xml.etree.ElementTree as ET
from lxml import etree as et
conn = psycopg2.connect("host = localhost dbname = postgres user = postgres password = qwerty4321")
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
treeRetail_Food_Stores_XML = et.parse('Retail_Food_Stores_XML.xml')
rootRetail_Food_Stores_XML = treeRetail_Food_Stores_XML.getroot()
treeZipLookupXML = et.parse('ZipLookupXML.xml')
rootZipLookupXML = treeZipLookupXML.getroot()

def Delivery_truck(cityzip):
    if (cityzip.isdigit()):
        text = cityzip
        path1 = "/root/item[Zip_Code = '{}'][Establishment_Type[contains(text(),'K')]]/DBA_Name/text()".format(text)
        result = rootRetail_Food_Stores_XML.xpath(path1) #returns list of strings
        if (len(result)==0):
            print("There are no food and delivery trucks in your search area.\n")
        elif (bool(result)):
            print("The following food and delivery trucks are in your search area:\n")
            for i in (result):
                print(i)
    elif (not cityzip.isdigit()):
        text1 = str.title(cityzip)
        path2 = "/root/item[City[text() ='{}']][State[text() ='New York']]/zip_Code/text()".format(text1) #returns zips from ziplookup tbl
        result1 = rootZipLookupXML.xpath(path2) #returns list of strings
        if (len(result1) == 0):
            print("There are no food and delivery trucks in your search area.\n")
        elif (bool(result1)):
            print("The following food and delivery trucks are in your search area:")
            for i in (result1):
                path3 = "/root/item[Zip_Code = '{}'][Establishment_Type[contains(text(),'K')]]/DBA_Name/text()".format(i)
                result2 = rootRetail_Food_Stores_XML.xpath(path3)
                print("\nIn zip code " + i + " these establishments have delivery or food trucks: ")
                for j in (result2):
                    print(j)
    return

def restaurant_Details(rest_ID):
    print("\nSelect the information you wish to see\n 1. Violations \n 2. Critical Violations \n 3. Permit Exipration date \n 4. All Other Details")
    rest_choice = input()
    custom_rest = ""
    if rest_choice.lower() in "total noncritical violations":
        custom_rest = "total_noncritical_violations"

    elif rest_choice.lower() in "total critical violations":
        custom_rest = "total_critical_violations"

    elif rest_choice.lower() in "permit expiration date":
        custom_rest = "permit_expiration_date"

    elif (rest_choice.lower() == "all"):
        cursor.execute("SELECT NYS_Health_Operation_Id, facility, total_noncritical_violations, total_critical_violations, permit_expiration_date FROM food_establishment where NYS_Health_Operation_Id = %s", (str(rest_ID), ))
        records = cursor.fetchall()
        for row in records:
            print("\n" + str(row[0]) + " " + row[1] + "\n" + "Total violations: " + str(row[2]) + ", total critical violations: " + str(row[3]) + " permit expires on: " + str(row[4]))
        return
    else:
        records = []
        print("Error: Could not find what you are looking for")
    if(not rest_choice.lower() == "all"):
        cursor.execute("SELECT NYS_Health_Operation_Id, facility, "+ custom_rest +" FROM food_establishment where NYS_Health_Operation_Id = %s", (str(rest_ID),))
    records = cursor.fetchall()
    for row in records:
        print("\n" + str(row[0]) + " " + row[1] + "\n" + custom_rest + ": " + str(row[2]))

    print("\nWould you like to see areas with lower violations?")
    other_areas = input()
    if(other_areas.lower() == "yes" ):
        cursor.execute("select facility_zip_code, (sum(total_noncritical_violations) + sum(total_critical_violations)) from food_establishment where NYS_Health_Operation_Id = %s	group by facility_zip_code", (str(rest_ID),))
        viol_records = cursor.fetchall()
        cursor.execute("select facility_zip_code, ((sum(total_noncritical_violations) + sum(total_critical_violations))/count(facility_zip_code)) as avg_violation from food_establishment, ziplookup z WHERE facility_zip_code = z.zip_code AND z.city = (select city from ziplookup where zip_code = %s) group by facility_zip_code", (str(viol_records[0][0]),))
        records = cursor.fetchall()
        print("\nThe following zip codes in your city have lower average violations :")
        for row in records:
            if(row[1] <= viol_records[0][1]):
                print("\nZip Code: " + str(row[0]) + ", Average Number of violations are: " + str(row[1]))

    print("\nDo want any other information")
    reinfo = input()
    if (reinfo.lower() == "no"):
        return
    else:
        restaurant_Details(rest_ID)

class dataclass():

    def Restaurant_search(cityzip):
        print("Are you looking for a specific restaurant in your area? (If yes, enter name or keyword)")
        keyname = input()
        if (keyname.lower() == "no"):
            keyname = ""
        elif(not keyname.isalpha()):
            print("Invalid Input")
            return
        name = '%' + keyname + '%'
        if (cityzip.isdigit()):
            cursor.execute("select facility, address, z.city, z.state, z.zip_code, NYS_Health_Operation_Id from food_establishment, ziplookup z where facility ILIKE %s AND facility_zip_code = z.zip_code AND facility_zip_code = %s LIMIT 10", (name, str(cityzip),))
        elif (cityzip.isalpha()):
            cursor.execute("select facility, address, z.city, z.state, z.zip_code, NYS_Health_Operation_Id from food_establishment, ziplookup z where facility ILIKE %s AND facility_zip_code = z.zip_code AND z.city ILIKE %s LIMIT 10", (name, str(cityzip),))
        records = cursor.fetchall()
        for row in records:
            print("\nID: " + str(row[5]) + " " + row[0] + "\nthe address is " + row[1] + ", " + row[2] + ", " + row[3] + ", " + str(row[4]))
        print("\nEnter Id if you would like to select a retaurant (Otherwise, enter no)")
        rest_ID = input()
        if (rest_ID.lower() == "no" or not rest_ID or not rest_ID.isdigit()):
            print("\nInvalid ID")
            return
        restaurant_Details(rest_ID)

    def Repair_search(cityzip):
        print("Enter type of repair shop \n 1. RS \n 2. RSB \n 3. All")
        keyname = input()
        if (keyname.lower() == "all"):
            keyname = ""
        elif(not keyname.isalpha()):
            print("Invalid Input")
            return
        name = '%' + keyname + '%'
        if (cityzip.isdigit()):
            cursor.execute("select facility_name, address, z.city, z.state, z.zip_code, business_type, facility_Number from vehicle_repair, ziplookup z where business_type ILIKE %s AND facility_zip = z.zip_code AND facility_zip = %s LIMIT 10", (name, str(cityzip),))
        elif (cityzip.isalpha()):
            cursor.execute("select facility_name, address, z.city, z.state, z.zip_code, business_type, facility_Number from vehicle_repair, ziplookup z where business_type ILIKE %s AND facility_zip = z.zip_code AND z.city ILIKE %s LIMIT 10", (name, str(cityzip),))
        records = cursor.fetchall()
        for row in records:
            print("\nID: " + str(row[6]) + " " + row[0] + "\nthe address is " + row[1] + ", " + row[2] + ", " + row[3] + ", " + str(row[4]))

        print("\n \nWhile you are waiting would you like to eat? (If yes, enter ID of the repair shop of your chioce)")
        rest_ans = input()
        if (rest_ans.lower() == "no" or not rest_ans):
            return
        cursor.execute("select facility, address, z.city, z.state, z.zip_code, NYS_Health_Operation_Id from food_establishment, ziplookup z where facility_zip_code = (SELECT facility_zip from vehicle_repair where facility_Number = %s) AND facility_zip_code = z.zip_code LIMIT 10", (rest_ans,))
        records = cursor.fetchall()
        for row in records:
            print("\nID: " + str(row[5]) + " " + row[0] + "\nthe address is " + row[1] + ", " + row[2] + ", " + row[3] + ", " + str(row[4]))
        print("\nWould you like to select a retaurant (If yes, enter ID)")
        rest_ID = input()
        if (rest_ID.lower() == "no" or not rest_ID.isdigit()):
            return
        restaurant_Details(rest_ID)


    def Retail_search(cityzip):
        print("Enter the type of Retail Store you're looking for \n 1. J(Multiple Operations) \n 2. A(Store) \n 3. B(Bakery) \n 4. C(Food Manufacturer) \n 5. D(Food Warehouse) \n 6. H(Wholesale Manufacturer) \n 7. All")
        keyname = input()
        if (keyname.lower() == "all"):
            keyname = ""
        elif(not keyname.isalpha()):
            print("Invalid Input")
            return
        name = '%' + keyname + '%'
        if (cityzip.isdigit()):
            cursor.execute("select dba_name, CONCAT(CONCAT(street_number, ' '),street_name) as address, establishment_type, z.city, z.state, z.zip_code from retail_food_stores r, ziplookup z where establishment_type ILIKE %s AND r.zip_code = z.zip_code AND r.zip_code = %s LIMIT 10", (name, str(cityzip),))
        elif (cityzip.isalpha()):
            cursor.execute("select dba_name, CONCAT(CONCAT(street_number, ' '),street_name) as address, establishment_type, z.city, z.state, z.zip_code from retail_food_stores r, ziplookup z where establishment_type ILIKE %s AND r.zip_code = z.zip_code AND z.city ILIKE %s LIMIT 10", (name, str(cityzip),))
        records = cursor.fetchall()
        for row in records:
            print("Name: " + row[0] + row[2] + "the address is " + row[1] + ", " + row[3] + ", " + row[4] + ", " + str(row[5]))

        print("\nDo you want to see which stores have daelivery trucks?")
        truck_ans = input()
        if(truck_ans.lower() == "yes"):
            Delivery_truck(cityzip)
        elif(truck_ans.lower() == "no"):
            return

    def Liquor_search(cityzip):
        print("What are you looking for? \n 1. Beer \n 2. Liquor \n 3. Cider \n 4. Wine \n 5. Clubs \n 6. All")
        keyname = input()
        if (keyname.lower() == "all"):
            keyname = ""
        elif(not keyname.isalpha()):
            print("Invalid Input")
            return
        name = '%' + keyname + '%'
        if (cityzip.isdigit()):
            cursor.execute("select premises_name, address, z.city, z.state, z.zip_code from liquor_licenses, ziplookup z where license_typename ILIKE %s AND licenseexpirationdate > now() AND zip = z.zip_code AND zip = %s LIMIT 10", (name, str(cityzip),))
        elif (cityzip.isalpha()):
            cursor.execute("select premises_name, address, z.city, z.state, z.zip_code from liquor_licenses, ziplookup z where license_typename ILIKE %s AND licenseexpirationdate > now() AND zip = z.zip_code AND z.city ILIKE %s LIMIT 10", (name, str(cityzip),))
        records = cursor.fetchall()
        for row in records:
            print("\n" + row[0] + "\nthe address is " + row[1] + ", " + row[2] + ", " + row[3] + ", " + str(row[4]))
        return
