from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = MenuItem()
make_coffee = CoffeeMaker()
money = MoneyMachine()

choice = input(f"Select your drink {menu.get_items()}")