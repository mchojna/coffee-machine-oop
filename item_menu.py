class Item:
    def __init__(self, name, water, milk, coffee, price):
        self.name = name
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
        self. price = price


class Menu:
    def __init__(self):
        self.menu = [Item(name="latte", water=200, milk=150, coffee=24, price=2.5),
                     Item(name="espresso", water=50, milk=0, coffee=18, price=1.5),
                     Item(name="cappuccino", water=250, milk=50, coffee=24, price=3.0)
                     ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, that item is not available.")