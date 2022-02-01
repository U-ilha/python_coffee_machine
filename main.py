from data import resources
from data import MENU
import sys

turn_on = True
money = 0.00
inserted = 0.0
pay = False


def report():
    """Give the quantity of water, milk, coffee and money in the coffee maker"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def spend(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if choice != 'espresso':
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


def check_resource(drink):
    global pay
    if resources['water'] < MENU[drink]["ingredients"]["water"]:
        print('Sorry there is enough water')
        report()
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print('Sorry there is enough coffee')
        report()
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print('Sorry there is enough milk')
        report()
    else:
        charge(drink)
        if pay:
            spend(drink)
            pay = False
            print(f'Here is your {drink}. Enjoy it!')


def process_coin():
    global inserted
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    penny = int(input('How many pennies? '))
    inserted = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (penny * 0.01)


def charge(drink):
    global money, pay, inserted
    if inserted < MENU[drink]['cost']:
        print("Sorry that's not enough money. Money refund")
        if money == 0:
            money -= inserted
    else:
        pay = True
        if inserted > MENU[drink]['cost']:
            change = inserted - MENU[drink]['cost']
            money += inserted - change
            print(f'Here is ${change} in change.')
            inserted = 0.0
        else:
            money += inserted
            inserted = 0.0


while turn_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    print('Please, insert coins.')
    process_coin()

    if choice == 'report':
        report()
    elif choice == 'off':
        sys.exit()
    elif choice == 'espresso':
        check_resource(choice)
    elif choice == 'latte':
        check_resource(choice)
    elif choice == 'cappuccino':
        check_resource(choice)
