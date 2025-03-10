MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUARTERS = 0.25
DIMES = 0.10
NICKELS = 0.05
PENNIES = 0.01
resources["money"] = 0


def report():
    for item in resources:
        print(f"{item}: {resources[item]}")


def check_resources(user_drink):
    for ingredient in resources:
        if resources[ingredient] < MENU[user_drink]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            return True


def update_resources(user_drink):
    for ingredient in resources:
        if ingredient in resources and ingredient in MENU[user_drink]["ingredients"]:
            resources[ingredient] -= MENU[user_drink]["ingredients"][ingredient]


def process_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_coins = float(quarters*QUARTERS + dimes*DIMES + nickels*NICKELS + pennies*PENNIES)
    return total_coins


def check_money(user_drink, money_input):
    drink_price = MENU[user_drink]["cost"]
    if drink_price > money_input:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(money_input - drink_price, 2)
        resources["money"] += drink_price
        return change


def coffee_machine():
    switch = True
    while switch:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        if user_input == "off":
            switch = False
        elif user_input == "report":
            report()
        else:
            resource_check = check_resources(user_input)
            if resource_check:
                user_money = process_coins()
                return_change = check_money(user_input, user_money)
                print(f"Here is ${return_change} dollars in change.")
                update_resources(user_input)
                print(f"Here is your {user_input}. Enjoy!")
            else:
                coffee_machine()


coffee_machine()
