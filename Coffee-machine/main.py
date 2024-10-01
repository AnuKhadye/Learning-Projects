
from replit import clear
import time

from menu import *


def show_resources():
    return f'Water : {resources["water"]}\nMilk : {resources["milk"]}\nCoffee : {resources["coffee"]}\nMoney : {resources["money"]}'

def process_coins(cost,drink):
    global resources
    quaters = int(input("Enter the quarters: "))
    dimes = int(input("Enter the dimes: "))
    nickels = int(input("Enter the nickels: "))
    pennies = int(input("Enter the pennies: "))
    amount_provided = (quaters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if cost <= amount_provided:
        resources["money"] += cost
        water_req = menu[drink]["ingredients"]["water"]
        milk_req = menu[drink]["ingredients"]["milk"]
        coffee_req = menu[drink]["ingredients"]["coffee"]
        resources["water"] -= water_req
        resources["milk"] -= milk_req
        resources["coffee"] -= coffee_req
        return amount_provided - cost


    else:
        return 0
    
def check_resources(drink):
    water_req = menu[drink]["ingredients"]["water"]
    milk_req = menu[drink]["ingredients"]["milk"]
    coffee_req = menu[drink]["ingredients"]["coffee"]
    
    
    if resources["water"] >= water_req and resources["coffee"] >= coffee_req and resources["milk"] >= milk_req:
        return 1
    else: 
        return 0




water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = resources['money']
    
is_running = True
while is_running:
    
    print("---------------------------------------------------------------")
    
    user_choice = input("Hello!!\nWhat would you like: ").lower()
    # When the user asks report he needs all the report of resources available.
    if user_choice == "report":
        clear()
        print(show_resources())
    elif user_choice.lower() == "latte" or user_choice == "espresso" or user_choice == "cappuccino":
        if check_resources(user_choice) == 1:
            cost = menu[user_choice]["cost"]
            print(f"The prices of {user_choice} is: {cost}")
            amount_processed = process_coins(cost,user_choice)
            if amount_processed == 0:
                print("Not enough amount provided\nRefunding all the money")
            else:
                print(f"Here is your change of ${round(amount_processed, 2)}")
                print(f"Enjoy your {user_choice}")
                print("---------------------------------------------------------------")
                time.sleep(5)
                
                
                
                
        else:
            print("Sorry not enough resources!")
            print("---------------------------------------------------------------")
    elif user_choice == "off":
        print(f'Closing machine the resources left are:\nWater : {resources["water"]}\nMilk : {resources["milk"]}\nCoffee : {resources["coffee"]}\nMoney : {resources["money"]}')
        print("---------------------------------------------------------------")
        is_running = False
        
    



