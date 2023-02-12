resources = {"water": 1000, "milk": 500, "coffee": 500, "sugar": 300, "money": 0}

coffee_small = {"water": 25, "milk": 15, "coffee": 50, "sugar": 20, "money": 300}

coffee_medium = {"water": 50, "milk": 30, "coffee": 100, "sugar": 35, "money": 500}

coffee_large = {"water": 75, "milk": 40, "coffee": 120, "sugar": 50, "money": 700}

def small_coffee(water, milk, coffee, sugar, money):
    print(f"You will get {water}cl of water, {milk}cl of milk, {coffee}g of coffee, and {sugar}g of sugar at N{money}:00 for Small Cup of Coffee")
    return small_coffee

coffee_small = small_coffee(coffee_small["water"], coffee_small["milk"], coffee_small["coffee"], coffee_small["sugar"], coffee_small["money"])

def medium_coffee(water, milk, coffee, sugar, money):
    print(f"You will get {water}cl of water, {milk}cl of milk, {coffee}g of coffee, and {sugar}g of sugar at N{money}:00 for Medium Cup of Coffee")
    return medium_coffee
coffee_medium = medium_coffee(coffee_medium["water"], coffee_medium["milk"], coffee_medium["coffee"], coffee_medium["sugar"], coffee_medium["money"])

def large_coffee(water, milk, coffee, sugar, money):
    print(f"You will get {water}cl of water, {milk}cl of milk, {coffee}g of coffee, and {sugar}g of sugar at N{money}:00 for Large Cup of Coffee")
    return large_coffee

coffee_large = large_coffee(coffee_large["water"], coffee_large["milk"], coffee_large["coffee"], coffee_large["sugar"], coffee_large["money"])

while True:
    user_input = input("What would you like, small/medium/large?: ").lower()
    if user_input not in ["small", "medium", "large", "report", "off"]:
        print("Invalid input")
    elif user_input == "off":
        break

    if user_input == "small":
        s = small_coffee()
        print(s)
    elif user_input == "medium":
        print(coffee_medium)
    elif user_input == "large":
        print(coffee_large)
