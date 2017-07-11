restaurant_detail={"Domino's":{"Owner's name":"Tom Monaghan","rating":"0","Food":{"Margherita":"350","Peppy Paneer":"450","Veg Extravaganza":"500","Mexican Green Wave":"475"}},
                "pizza hut":{"Owner's name":"Virag Joshi","rating":"0","Food":{"Paneer & Capsicum":"370","Chicken keema & Corn":"480","Chicken Hot N Spicy":"500","Onion":"375"}}}

print"WELCOME"
type=raw_input("\npress 1 if you are customer\npress 2 if you are owner\nwaiting for your response::")
if type=="2":
        choice=raw_input("\npress 1 to update information \npress 2 to quit\nwaiting for your response::")
if choice=="1":
        rest_name=raw_input("\npress 1 to update domino's information\npress 2 to update pizza hut information\nwaiting for your response::")
       if rest_name=="1":
                update_ch=raw_input("\npress 1 to update owner's information\npress 2 to update food information\nwaiting for your response::")
       if update_ch=="1":
                    new_name=raw_input("enter new name")
                    restaurant_detail["Domino's"]["Owner's name"] = new_name
                    if update_ch=="2":
                    choice2=raw_input("\npress 1 to update price\npress 2 to add food\npress 3 to remove food\nwaiting for your response::")
                        if choice2=="1":
                        name=raw_input("enter the name of food item::")
                        if name in restaurant_detail["Domino's"]["Food"]:
                            price=raw_input("enter new price")
                            restaurant_detail["Domino's"]["Food"][name] = price
                        else:
                            print"Food item not found try again"
                            exit()