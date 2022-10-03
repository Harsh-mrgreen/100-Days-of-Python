from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
total_cost = 0
print("Welcome to bhakti coffee :)")
def coffee_machine():
    order_coffee = True
    while order_coffee == True:

        
        menu_obj = Menu()
        #print(menu_obj.get_items())
        order = input(f"what would you like? : {menu_obj.get_items()}")
        final_order = menu_obj.find_drink(order)
        print(final_order)

        if final_order != None:
        # menu_item = MenuItem('name','water', 'milk', 'coffee','cost')
            print(final_order.name)
            print(final_order.cost)
            print(final_order.ingredients)
            order_coffee = False
        

# preparation
    make_coffee = CoffeeMaker()
    make_coffee.report()
    print(make_coffee.is_resource_sufficient(final_order))
    make_coffee.make_coffee(final_order)

    return final_order.cost


while input("Would you like to order? type y or n").lower() == 'y':
    total_cost += coffee_machine()


# money machine
bill = MoneyMachine()
bill.report()
print(bill.make_payment(total_cost))



