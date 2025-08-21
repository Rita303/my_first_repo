#Name= ("Rita  Ogechi")
#print(Name.endswith("i"))
#from math import *
#my_num = 5
#print(pow(my_num ,3 ))
#num_1= input("Enter a number:") #simple calculator project
#num_2= input("Enter a second number:")
#result= int(num_1) + int(num_2)
#print(result)

#MADLIBS GAME

#age= input("Enter an age: ")

#wish_1 = input("Enter a wish: ") 
#wish_2 = input("Enter a second wish: ") 

#print("MY BIRTHDAY WISHLIST")
#print(f"This year, I am turning {age}. Below are my two wishes for this new year ,")
#print(f"I wish that my {wish_1} be processed and ready. \n Though it seems hard, I do believe that with God all things are possible! ")
#print("Secondly, I wish to have a " + wish_2 + " for my " + age + "th birthday. ")
#DAY 2: LISTS
#my_list = ["Apples are red", "mango", 1, "Äll are yummy!"]
#my_list.append("Apples are red")
#my_preferences= ["plum", 3, "Äll fruits are yummy!"]
#my_list. extend(my_preferences)
#my_list.remove(1)
#my_list.append(["Goodluck", "to you"])
#print(my_list)
#is("mango") in my_list
#print(my_list)

#TUPLES
#Graph_A = ["x","y", "a","b"]
#Graph_B = (1, 2)
#Graph_C = sorted(Graph_A)
#Graph_A.sort()
#print(Graph_A)

#print(Graph_C)

#FUNCTIONS
#def greet(user, age):
    #user = (name_1, name_2)
    #if user == "Frank" and age == 50:
 #       print(f"Good morning {user}, you are {age} years old")
    #elif user == "Kate":
     #   print(f"Hi {user}, nice to know that you are {age} years old")
    #else:
     #   print(f"Invalid username, Please enter the correct {user}, and {age}")
#greet("Frank", 54)
#A PROJECT ON USING DUAL FUNCTIONS AND VARIABLES
def dispensing_machine():
    product = input("Choose a product: (drinks: coke, Fanta, Sprite), Water")
    prices = {"coke": 2, "Fanta": 3, "Sprite": 4, "Water":1}
    quantity = int(input(f"How many {product} do you want? ")) 
    if product != 'Water':
        price = prices[product]* quantity 
        print(f" Your {product} is ${price}" )
    elif product == " Water ":
        price = prices[product] * quantity  
        print(f" Your {product} is ${price}")
    else: not product == ("drink" and "Water")
    price = 0
    return product, quantity, price
                         
def payment_method(product, quantity, price):
    method= input("Please choose a payment method: (card or cash?) ")
    #cash = "note" or "coins"
    if method == 'cash':
     cash_type = input(f"Will you pay with note or coins: ")
     if cash_type == 'note' :    
      print("Please put your note in the box")
     else: cash_type == "coins"
    print("Kindly insert your coin in the hole")    
    if method == 'card' :
     card = input(f"Enter your card type for discount: ")
    card_types = {"Gold" : 0.2, "visa" : 0.1, "Shukran": 0.1, "Others":0}
    if card == 'Gold':
      discount = 0.2
    elif card== 'Shukran' or 'visa' :
      discount = 0.1
    else: card == 'Others'
    discount = 0
    return card_types, discount
    #while card in card_types ==  "visa" or "Shukran":
     #discount == 1   
    #try: 
    if card_types == "Gold" and product != "water":
       price = prices[product]*discount* quantity
       print(f"Your drink is ${price}, you got a 20% discount with your Gold card")
    elif card_types == ("visa" or "Shukran"):
       price = prices[product]*discount* quantity
       print(f"Your drink is ${price}, you got a 10% discount with your card")
    #except
    #if card_types == "Others":
    else:
     price = prices[product]* quantity
    print(f"Sorry, there is no discount for this card type, your drink is ${price}")

product,quantity, price=dispensing_machine()
payment_method(quantity, product,price)