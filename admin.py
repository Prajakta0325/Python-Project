import random
import json
class admin():
    def __init__(self):
        self.food_details={}

    def add_fooditems(self):
        id=random.randint(1,100)
        name=input("Enter Food Name :")
        stock=input("Enter stock :")
        quantity=int(input("Enter Quantity :"))
        price=int(input("Enter Price :"))
        food_data={"Name":name,"Stock":stock,"Quantity":quantity,"Price":price}

        self.food_details[id]=food_data

        #store in json
        with open("add_food.json","w")as f:
            json.dump(self.food_details,f,indent=4)
        return self.food_details
    
    def view_fooditems(self):
        with open("add_food.json","r") as f:
            content1=json.load(f)
        for k,v in content1.items():
            print(f"Food ID: {k}   Data : {v}")

    def remove_fooditems(self):
        with open("add_food.json","r") as f:
            content1=json.load(f)
        for k,v in content1.items():
            print(f"Food ID: {k}   Data : {v}")
        food_id=int(input("Enter Food Id Wich You Want to delete :"))
        del content1[food_id]
        print("Food Item Deleted Successfully...")

        with open("add_food.json","w") as f:
            json.dump(content1,f,indent=4)
        return content1
    
    def updated_fooditems(self):
        with open("add_food.json","r") as f:
            content1=json.load(f)
        for k,v in content1.items():
            print(f"Food ID: {k}   Data : {v}")




    
    def edit_fooditems(self):
        pass

    
x=admin()
#x.add_fooditems()
#x.view_fooditems()
x.remove_fooditems()
