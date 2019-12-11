from Database import *

class user_application():
    def __init__(self):
        return

    def search_all(self):
        print("What are you looking for? \n 1. Restaurants \n 2. Vehicle Repair \n 3. Retail Stores \n 4. Liquor Stores")
        searchval = input()
        print("Enter Location (City or Zip)")
        cityzip = input()
        if searchval.lower() in "restaurants":
            records = dataclass.Restaurant_search(cityzip)
        elif searchval.lower() in "vehicle repair":
            records = dataclass.Repair_search(cityzip)
        elif searchval.lower() in "retail stores":
            records = dataclass.Retail_search(cityzip)
        elif searchval.lower() in "liquor stores":
            records = dataclass.Liquor_search(cityzip)
        else:
            records = []
            print("Error: Could not find what you are looking for")

        self.loop()
        return

    def loop(self):
        print("\nIs there anything else?")
        value1 = input()
        if (value1.lower() == "yes"):
            self.search_all()
        else:
            exit(0)

user_obj = user_application()
user_obj.search_all()
