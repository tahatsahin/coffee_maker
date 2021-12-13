from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


def not_enough_resources(ingredient):
    """Function which prints not enough information. """
    print("Sorry there is not enough {0}".format(ingredient))


def get_money():
    """Function that takes inputs from user to calculate the total money inserted. """
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickels + pennies


menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

while True:
    """Main program. """
    user_input = input("What would you like? {0}: ".format(menu.get_items()))
    if user_input == "off":
        break
    elif user_input == "report":
        machine.report()
        money.report()
        continue
    else:
        item = menu.find_drink(user_input)
    if item is None:
        continue
    if not machine.is_resource_sufficient(item):
        continue
    cost = item.cost
    payment_done = money.make_payment(cost)
    if payment_done:
        machine.make_coffee(item)
