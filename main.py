from item_menu import Menu
from coffee_machine import CoffeeMachine
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMachine()
money_machine = MoneyMachine()

on = True

while on:

    while True:
        order = input(f"What would you like ({menu.get_items()}): ").lower()
        if order in menu.get_items().split("/") or order == "off":
            if order == "latte":
                order_index = 0
            elif order == "espresso":
                order_index = 1
            elif order == "cappuccino":
                order_index = 2
            break
        elif order == "report":
            coffee_machine.report()
            money_machine.report()

    if order == "off":
        on = False
        break

    condition_1 = coffee_machine.resources_check(menu.menu[order_index])

    if condition_1:
        condition_2 = money_machine.make_payment(menu.menu[order_index].price)

    if condition_1 and condition_2:
        coffee_machine.make_coffee(menu.menu[order_index])
