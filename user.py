import random
import json
class user:
    def __init__(self):
        self.user_details={}
        self.order_food=[]
        self.ordered_dic={}
        self.count=0
        
    def registration(self):
        self.count=self.count+1
        id=self.count
        self.name=input("Enter name :")
        self.phone_no=input("Enter Mobile Number :")
        self.email_id=input("Enter Email id :")
        self.password=input("Enter Password :")
        self.address=input("Enter Address :")

        user_data={"Name":self.name,"Phone Number":self.phone_no,"Email ID":self.email_id,"Address":self.address}

        id=random.randint(1,100)
        self.user_details[id]=user_data
        print("Successfully Register")

        with open("user_details.json","w")as f:
            json.dump(self.user_details,f,indent=4)

    def user_login(self):
        #while True:
            username=print("Enter Your Username :")
            password=print("Enter Your Password :")
            if username==self.email_id and password==self.password:
                print("Login Successfully...")
            else:
                print("Enter Valid Credential..")

    def place_order(self):
        key=random.randint(1,100)
        fooditem_list=[{"name":"Tandoori Chicken","Quantity":"(4 pieces)","Price":"[INR 240]"},{"Name":"Vegan Burger","Quantity":"(1 Piece)","Price":"[INR 320]"}]
        for i in range(len(fooditem_list)):
            print(fooditem_list[i])
        print("Press 1-- For Tanduri Chicken")
        print("Press 2-- For Vegan Burger")
        choice=input("Enter Your choice :")
        if choice==1:
            self.order_food.append(fooditem_list[0])
        elif choice==2:
            self.order_food.append(fooditem_list[1])
        else:
            print("Order Valid item")
        ordered = {"Ordered Item":self.order_food}
        print(ordered)
        self.ordered_dic[key]=ordered

        order= int(input("Do you want to confirm your order\n 1. Yes\n 2. No"))
        if order==1:
            print("Order Place Successfully...")
        else:
            print("Order not Placed...")

        with open("order_details.json","w") as f:
             json.dump(self.ordered_dic,f,indent=4)

        
u=user()
#u.registration()
#u.user_login()
u.place_order()