# Importing
from menu_resources import MENU, resources

# ********** Greeting
print("******************************")
print("Welcome To Coffee Magic")
print("******************************")

# ********** Condition Variables
is_on = True
profit = 0


# ********** Checking Resources
def checking_resources(order_ingredients):  # Function for checking if there is enough resources
    """Function for checking if there is enough resources"""
    for item in order_ingredients:  # Loops through each item in ingredients and compares it to resources
        if order_ingredients[item] >= resources[item]:  # If ingredient needs more than resources available
            print(f"Sorry there isn't enough {item} to make that order:")
            return False  # Sorry not enough of a particular resource
    return True  # If resources is enough


# ********** Tacking and Processing Payment
def process_payment():
    """Returns the total calculated from the coins inserted"""  # Known as a doc-string
    print(f"The cost of your drink is ${drink['cost']} Please insert coins. ")
    total = int(input("How many quarters? ")) * 0.25  # Multiplies the number by the value of each denomination
    total += int(input(
        "How many dimes? ")) * 0.10  # Multiplies the number by the value of each denomination and adds to the total
    total += int(input(
        "How many nickles? ")) * 0.05  # Multiplies the number by the value of each denomination and adds to the total
    total += int(input(
        "How many pennies? ")) * 0.01  # Multiplies the number by the value of each denomination and adds to the total
    return total


# ********** Checking If Transaction Is Accepted
def transaction_successful(money_received, drink_cost):
    """Returns True when payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"You have paid ${round(money_received, 2)} and your change is ${change}")
        global profit  # Needed, In order to access the profit outside this function, Global Scope, Local Scope
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money being refunded. ")
        return False


# ********** Deducting Ingredients From Resources
def make_coffee(drink_name, order_ingredients):
    """Deducting the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕:")

# ********** While loop: While condition is true run, otherwise finish
while is_on:
    user_choice = input(
        "What would you like to order? (espresso/Latte/cappuccino) Or type 'off' to turn the machine off: ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print("******************************")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        print("******************************")
    else:
        drink = MENU[user_choice]
        if checking_resources(drink["ingredients"]):
            payment = process_payment()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
