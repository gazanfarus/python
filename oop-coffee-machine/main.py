from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
make_coffee = CoffeeMaker()
money = MoneyMachine()
is_on = True

while is_on:
    make_coffee.report()
    money.report()
    choice = input(f"Select your drink {menu.get_items()}: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        make_coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if drink != None:
            if make_coffee.is_resource_sufficient(drink):
                if money.make_payment(drink.cost):
                    make_coffee.make_coffee(drink)

