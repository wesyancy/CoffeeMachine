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
    "money": 0.00,
}


# TODO 1: Create a function that prints report showing current resources
def report(resource):
    print(f"Water: {resource.get('water')}ml")
    print(f"Milk: {resource.get('milk')}ml")
    print(f"Coffee: {resource.get('coffee')}g")
    print(f"Money: ${resource.get('money')}")


# TODO 2: Create 'Check Resources' function: Check if all resources are sufficient before making any coffee
def check_resources(pick):
    if pick == 'espresso':
        water_req = MENU['espresso']['ingredients']['water']
        coffee_req = MENU['espresso']['ingredients']['coffee']
        if (resources['water'] < water_req) or (resources['coffee'] < coffee_req):
            print("Sorry, there are not enough ingredients to make this drink.")
            return False
        else:
            return True
    if pick == 'latte':
        water_req = MENU['latte']['ingredients']['water']
        milk_req = MENU['latte']['ingredients']['milk']
        coffee_req = MENU['latte']['ingredients']['coffee']
        if (resources['water'] < water_req) or (resources['milk'] < milk_req) or (resources['coffee'] < coffee_req):
            print("Sorry, there are not enough ingredients to make this drink.")
            return False
        else:
            return True
    if pick == 'cappuccino':
        water_req = MENU['cappuccino']['ingredients']['water']
        milk_req = MENU['cappuccino']['ingredients']['milk']
        coffee_req = MENU['cappuccino']['ingredients']['coffee']
        if (resources['water'] < water_req) or (resources['milk'] < milk_req) or (resources['coffee'] < coffee_req):
            print("Sorry, there are not enough ingredients to make this drink.")
            return False
        else:
            return True


# TODO 4: In 'Make Coffee': If sufficient resources available, make sure user provides sufficient payment
def check_payment(selection):
    espresso_cost = MENU['espresso']['cost']
    latte_cost = MENU['latte']['cost']
    cappuccino_cost = MENU['cappuccino']['cost']

    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))

    total_payment = 0
    total_payment += quarters * .25
    total_payment += dimes * .10
    total_payment += nickels * .05
    total_payment += pennies * .01

    # TODO 6 cont: All excess money should be refunded

    if selection == 'espresso':
        if total_payment > espresso_cost:
            resources['money'] += espresso_cost
            change = round(total_payment - espresso_cost, 2)
            return change
        else:
            return False
    if selection == 'latte':
        if total_payment > latte_cost:
            resources['money'] += latte_cost
            change = round(total_payment - latte_cost, 2)
            return change
        else:
            return False
    if selection == 'cappuccino':
        if total_payment > cappuccino_cost:
            resources['money'] += cappuccino_cost
            change = round(total_payment - cappuccino_cost, 2)
            return change
        else:
            return False


def brew(selection):
    # TODO 7: In 'Make Coffee': After making coffee, resource count should reflect deducted totals
    if selection == 'espresso':
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        print("Here's your espresso! ☕️")
        return
    if selection == 'latte':
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
        print("Here's your latte! ☕️")
        return
    if selection == 'cappuccino':
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        print("Here's your cappuccino! ☕️")
        return


# TODO 3: Create 'Make Coffee' function: Prompt user and ask "What would you like?"
def make_coffee():

    keep_brewing = True
    # TODO 5: There should be an 'off' switch built in, process should repeat until 'off' is input

    while keep_brewing:
        if (resources['water'] < 50) or (resources['coffee'] < 18):
            print("Not enough resources to make any more drinks, goodbye.")
            keep_brewing = False

        selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if selection == 'off':
            keep_brewing = False
        if selection == 'report':
            report(resources)
        elif check_resources(selection):
            sufficient_payment = check_payment(selection)
            if not sufficient_payment:
                print("Sorry that's not enough money. Money refunded")
            else:
                # TODO 6: In 'Make Coffee': If money provided is sufficient and enough resources are present,
                #  make coffee.
                brew(selection)
                print(f"Here is ${sufficient_payment} in change.")
                # print(resources)
    return


make_coffee()
