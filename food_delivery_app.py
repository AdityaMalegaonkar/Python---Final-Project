# Admin id : restaurant24x7@gmail.com
# Admin password : restaurant

# User id : user24x7@gmail.com
# User password : user

from exceptions import *
import re
import datetime as dt
print("********Welcome to our restaurant app********")
num = int(input("Enter \n 1. to login as Admin \n 2. to login as user :\n"))
dict1 = {"id" : 1 , "Name" : "Tandoori Chicken" , "Quantity" : "4 pieces" ,"Price" : 240 , "Discount" : 50 , "Stock" : "400 pieces"}
dict2 = {"id" : 2 , "Name" : "Vegan Burger" , "Quantity" : "1 piece" ,"Price" : 320 , "Discount" : 75 , "Stock" : "50 pieces"}
dict3 = {"id" : 3 , "Name" : "Truffle Cake" , "Quantity" : "500gm" ,"Price" : 900 , "Discount" : 150 , "Stock" : "30 pieces of 500gm"}
class admin:
    dict4 = {}

    def add_items(self):
        print("********Add Item********")
        admin.dict4 = dict1.copy()
        admin.dict4.update({"id" : update_id , "Name" : update_name , "Quantity" : update_quantity , "Price" : update_price , "Discount" : update_discount , "Stock" : update_stock})
        return f"\n********Item Added Successfully******** \n {admin.dict4}"
    
    def edit_items(self):
        if edit == dict1["id"]:
            edit_name = input("Update name of item :")
            edit_quantity = input("Update quantity :")
            edit__price = float(input("Update price :"))
            edit_discount = int(input("Update discount :"))
            edit_stock = input("Update Stock :")
            dict1.update({"Name" : edit_name , "Quantity" : edit_quantity , "Price" : edit__price , "Discount" : edit_discount , "Stock" : edit_stock})
            return f"\n********Updated Successfully******** \n {dict1}"

        if edit == dict2["id"]:
            edit_name = input("Update name of item :")
            edit_quantity = input("Update quantity :")
            edit__price = float(input("Update price :"))
            edit_discount = int(input("Update discount :"))
            edit_stock = input("Update Stock :")
            dict2.update({"Name" : edit_name , "Quantity" : edit_quantity , "Price" : edit__price , "Discount" : edit_discount , "Stock" : edit_stock})
            return f"\n********Updated Successfully******** \n {dict2}"

        if edit == dict3["id"]:
            edit_name = input("Update name of item :")
            edit_quantity = input("Update quantity :")
            edit__price = float(input("Update price :"))
            edit_discount = int(input("Update discount :"))
            edit_stock = input("Update Stock :")
            dict3.update({"Name" : edit_name , "Quantity" : edit_quantity , "Price" : edit__price , "Discount" : edit_discount , "Stock" : edit_stock})
            return f"\n********Updated Successfully******** \n {dict3}"

    def remove_item(self):
        print("********Remove Food Item********")
        if remove_id == dict1["id"]:
            dict1.clear()

        if remove_id == dict2["id"]:
            dict2.clear()

        if remove_id == dict3["id"]:
            dict3.clear()
        print("\n","********Item removed successfully********")

    def view_items(self):
        for k,v in dict1.items():
            print(k , "-" , v)
        print("\n")
        for i,j in dict2.items():
            print(i , "-" , j)
        print("\n")
        for m,n in dict3.items():
            print(m , "-" , n)
        print("\n")
        for o,p in admin.dict4.items():
            print(o , "-" , p)
    

class user(admin):
    username = "Aditya Malegaonkar"
    userphone = "9407852755"
    useremail = "malegaonkar25@gmail.com"
    useraddress = "Jabalpur"
    userpassword = "Aditya@0306"
    lst = []
    def order(self):
        print("\n********Menu********\n")
        print(dict1["id"] ,"." , dict1["Name"] ,"(" , dict1["Quantity"] ,")" , "[" , dict1["Price"] , "]""\n",dict2["id"] ,"." , dict2["Name"] ,"(" , dict2["Quantity"] ,")" , "[" , dict2["Price"] , "]""\n",dict3["id"] ,"." , dict3["Name"] ,"(" , dict3["Quantity"] ,")" , "[" , dict3["Price"] , "]""\n")
        order_lst = []
        size = int(input("How many items you want to order :"))
        for item in range(size):
            select = int(input("Enter FoodID of the item you want to order :"))
            order_lst.append(select)
        print("\n""------------------------------------------------------------------")
        print("********Your Cart********""\n")
        for order in order_lst:
            if order == dict1["id"]:
                user.lst.append(dict1)
            if order == dict2["id"]:
                user.lst.append(dict2)
            if order == dict3["id"]:
                user.lst.append(dict3)
            else:
                try:
                    raise WrongID()
                except Exception as ex:
                    print(ex)
        for i in user.lst:
            print(i , "\n")
        place_order = int(input("Enter\n1. To place order\n2. To cancel order :\n"))
        if place_order == 1:
            current = dt.datetime.now()
            print("-----------------------------------------------------------------------------------")
            print("\n","********Order Details********","\n")
            for i in user.lst:
                print(i,"\n")
            if dict1 in user.lst:
                price_dict1 = dict1["Price"] - dict1["Discount"]
                print("Order placed on :" , current,"\n",dict1["Name"] , dict1["Quantity"] , "->" , "Price :" , dict1["Price"] , "-" , "Discount :" , dict1["Discount"],"\n")
                print("Price in INR :" , "->" , price_dict1,"\n")
            if dict2 in user.lst:
                price_dict2 = dict2["Price"] - dict2["Discount"]
                print("Order placed on :" , current,"\n",dict2["Name"] , dict2["Quantity"] , "->" , "Price :" , dict2["Price"] , "-" , "Discount :" , dict2["Discount"],"\n")
                print("Price in INR :" , "->" , price_dict2,"\n")
            if dict3 in user.lst:
                price_dict3 = dict3["Price"] - dict3["Discount"]
                print("Order placed on :" , current,"\n",dict3["Name"] , dict3["Quantity"] , "->" , "Price :" , dict3["Price"] , "-" , "Discount :" , dict3["Discount"],"\n")
                print("Price in INR :" , "->" , price_dict3,"\n")
            else:
                try:
                    raise WrongID()
                except Exception as ex:
                    print(ex)
            for i in user.lst:
                if dict1 in user.lst:
                    total_price = price_dict1
                if dict2 in user.lst:
                    total_price = price_dict2
                if dict3 in user.lst:
                    total_price = price_dict3
                if dict1 in user.lst and dict2 in user.lst:
                    total_price = price_dict1 + price_dict2
                if dict1 in user.lst and dict3 in user.lst:
                    total_price = price_dict1 + price_dict3
                if dict2 in user.lst and dict3 in user.lst:
                    total_price = price_dict2 + price_dict3
                if dict1 in user.lst and dict2 in user.lst and dict3 in user.lst:
                    total_price = price_dict1 + price_dict2 + price_dict3
            print("\n","Total Price :" , total_price , "\n")
            print("-----------------------------------------------------------------------------------")
            print("\n","********Order Placed********","\n")
            print("Cash On Delivery","\n")
            print("Our Delivery Partner will reach in 30 mins, kindly pay him Rs",total_price,"\n")
        elif place_order == 2:
            print("-----------------------------------------------------------------------------------")
            user.lst.clear()
            print("Order Cancelled")
            print("\n","********Your cart is Empty********")
        else:
            try:
                raise NoOptionError()
            except Exception as ex:
                print(ex)

    def history(self):
        print("\n","********Order History********","\n")
        if len(user.lst) == 0:
            print("\n","Empty : You have not ordered anything yet!!","\n")
        else:
            for i in user.lst:
                print("\n",dt.datetime.now(),"\n",i,"\n")

    def update_login(self):
        print("\n","********Update Profile********","\n")
        print("\n","Name :" , user.username,"\n","Mobile number :" , user.userphone,"\n","Email :" , user.useremail,"\n","Address :" , user.useraddress,"\n","Password :" , user.userpassword,"\n")       
        update_name = input("Update your full name :")
        res1 = re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', update_name)
        if res1:
            update_phone = input("Update your mobile number :")
            res2 = re.findall(r'^[789]\d{9}$' , update_phone)
        else:
            try:
                raise TryAgain()
            except Exception as ex:
                print(ex)
        if res2:
            update_email = input("Update your email address :")
            res3 = re.findall("^[A-z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$",update_email)
        else:
            try:
                raise TryAgain()
            except Exception as ex:
                print(ex)
        if res3:
            update_address = input("Update your address :")
        if update_address:
            update_password = input("Create a password\nIt should be 6-20 characters long, atleast one character in capital, atleast one digit, and atleast one special character :")
            res5 = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" , update_password)
        else:
            try:
                raise TryAgain()
            except Exception as ex:
                print(ex)
        user.username = update_name
        user.userphone = update_phone
        user.useremail = update_email
        user.useraddress = update_address
        user.userpassword = update_password
        print("\n","********Profile Successfully Updated********","\n")
        print("\n","Name :" , user.username,"\n","Mobile number :" , user.userphone,"\n","Email :" , user.useremail,"\n","Address :" , user.useraddress,"\n","Password :" , user.userpassword,"\n")
        
    def update_register(self):       
        update_name = input("Update your full name :")
        res1 = re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', update_name)
        if res1:
            update_phone = input("Update your mobile number :")
            res2 = re.findall(r'^[789]\d{9}$' , update_phone)
        else:
            try:
                raise TryAgain()
            except Exception as ex:
                print(ex)
        if res2:
            update_email = input("Update your email address :")
            res3 = re.findall("^[A-z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$",update_email)
        else:
            try:
                raise TryAgain()
            except Exception as ex:
                print(ex)
        if res3:
            update_address = input("Update your address :")
        if update_address:
            update_password = input("Create a password\nIt should be 6-20 characters long, atleast one character in capital, atleast one digit, and atleast one special character :")
            res5 = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" , update_password)
        else:
            try:
                raise TryAgain()
            except Exception as ex:
                print(ex)
        u_name = update_name
        u_mobile = update_phone
        u_email = update_email
        u_address = update_address
        u_pass = update_password
        print("\n","********Profile Successfully Updated********","\n")
        print("\n","Name :" , u_name,"\n","Mobile number :" , u_mobile,"\n","Email :" , u_email,"\n","Address :" , u_address,"\n","Password :" , u_pass,"\n")
        
if num == 1:
    admin_id = input("Enter your ID :")
    admin_pass = input("Enter your password :")
    if admin_id == "restaurant24x7@gmail.com" and admin_pass == "restaurant":           
        admin_obj = admin()
        choice = int(input("Enter \n1.To add items \n2.To edit items \n3.To view all items \n4.To remove item :\n"))
        if choice == 1:
            print("-----------------------------------------------------------------------------------")
            print("\n","Menu before adding items","\n")
            admin_obj.view_items()
            update_id = int(input("Add Food ID :"))
            if update_id != dict1["id"] and update_id != dict2["id"] and update_id != dict3["id"]:
                update_name = input("Add name of food item :")
                update_quantity = input("Add quantity :")
                update_price = int(input("Add price :"))
                update_discount = int(input("Add discount :"))
                update_stock = input("Add stock :")
                print(admin_obj.add_items()) 
                print("-----------------------------------------------------------------------------------")
                print("\n","Menu after adding items","\n")
                admin_obj.view_items()
            else:
                try:
                    raise SimilarID()
                except Exception as ex:
                    print(ex) 
        elif choice == 2:
            print("-----------------------------------------------------------------------------------")
            print("\n","********Edit Food Item********","\n")
            print("\n","Menu before editing items","\n")
            admin_obj.view_items()
            edit = int(input("Enter food id of item you want to edit :"))
            if edit == dict1["id"] or edit == dict2["id"] or edit == dict3["id"]:
                print("-----------------------------------------------------------------------------------")
                print("\n",admin_obj.edit_items(),"\n")
                print("\n","Menu after editing items","\n")
                admin_obj.view_items()
            else:
                try:
                    raise WrongID()
                except Exception as ex:
                    print(ex)
        elif choice == 3:
            print("-----------------------------------------------------------------------------------")
            print("\n","********Menu********","\n")
            admin_obj.view_items()
        elif choice == 4:
            print("-----------------------------------------------------------------------------------")
            print("\n","Menu before removing items","\n")
            admin_obj.view_items()
            remove_id = int(input("Enter id of food you want to remove :"))
            if remove_id == dict1["id"] or remove_id == dict2["id"] or remove_id == dict3["id"]: 
                admin_obj.remove_item()
                print("-----------------------------------------------------------------------------------")
                print("\n","Menu after removing items","\n")
                admin_obj.view_items()
            else:
                try:
                    raise WrongID()
                except Exception as ex:
                    print(ex)
        else:
            try:
                raise NoOptionError()
            except Exception as ex:
                print(ex)
    else:
        try:
            raise WrongCredentials()
        except Exception as ex:
            print(ex)
elif num == 2:
    user_obj = user()
    login = int(input(("Enter\n1. To Log In\n2. to Register your ID :\n")))
    if login == 1:
        print("\n********Login********\n")
        user_id = input("Enter your ID :")
        user_pass = input("Enter your password :")
        if user_id == "user24x7@gmail.com" and user_pass == "user":
            print("-----------------------------------------------------------------------------------")
            print("\n","Name :" , user.username,"\n","Mobile number :" , user.userphone,"\n","Email :" , user.useremail,"\n","Address :" , user.useraddress,"\n")
            print("-----------------------------------------------------------------------------------")
            while True:
                option = int(input("Enter\n1. To place new order\n2. To view Order History\n3. To update Profile :\n"))
                if option == 1:
                    user_obj.order()
                elif option == 2:
                    user_obj.history()
                elif option == 3:
                    user_obj.update_login()
                else:
                    try:
                        raise NoOptionError()
                    except Exception as ex:
                        print(ex)
        else:
            try:
                raise WrongCredentials()
            except Exception as ex:
                print(ex)
    elif login == 2:
        u_name = input("Enter your full name :")
        res1 = re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', u_name)
        if res1:
            u_mobile = input("Enter your mobile number :")
            res2 = re.findall(r'^[789]\d{9}$' , u_mobile)
        else:
            try:
                raise TryAgain()
            except Exception as ex:
                print(ex)
        if res2:
            u_email = input("Enter your email address :")
            res3 = re.findall("^[A-z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$",u_email)
        else:
            try:
                raise TryAgain()
            except Exception as ex:
                print(ex)
        if res3:
            u_address = input("Enter your address :")
        if u_address:
            u_pass = input("Create a password\nIt should be 6-20 characters long, atleast one character in capital, atleast one digit, and atleast one special character :")
            res5 = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" , u_pass)
        else:
            try:
                raise TryAgain()
            except Exception as ex:
                print(ex)
        if res5:
            print("Registered Successfully")
        else:
            try:
                raise TryAgain()
            except Exception as ex:
                print(ex)
        print("-----------------------------------------------------------------------------------")
        print("Full Name :",u_name,"\n","Mobile Number :",u_mobile,"\n","Email Address :",u_email,"\n","Address :",u_address)
        print("-----------------------------------------------------------------------------------")
        while True:
            option = int(input("Enter\n1. To place new order\n2. To view Order History\n3. To update Profile :\n"))
            if option == 1:
                user_obj.order()
            elif option == 2:
                user_obj.history()
            elif option == 3:
                print("\n","********Update Profile********","\n")
                print("\n","Name :" , u_name,"\n","Mobile number :" , u_mobile,"\n","Email :" , u_email,"\n","Address :" , u_address,"\n","Password :" , u_pass,"\n")
                user_obj.update_register()
            else:
                try:
                    raise NoOptionError()
                except Exception as ex:
                    print(ex)
    else:
        try:
            raise NoOptionError()
        except Exception as ex:
            print(ex)
else:
    try:
        raise NoOptionError()
    except Exception as ex:
        print(ex)
