from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# from replicant import clear

# Building Objects
Coffee_Menu = Menu()
Coffee_Machine = CoffeeMaker()
Casher = MoneyMachine()

# Building Coffee query
types_coffe = Coffee_Menu.get_items()
coffee_query = Coffee_Menu.find_drink( types_coffe[1] )


# Making the coffee
if Coffee_Machine.is_resource_sufficient( coffee_query ):
   
    Coffee_Machine.make_coffee( coffee_query )
    print( "Please pay " + str( coffee_query.cost ) + " for " + coffee_query.name )
    
    while Casher.make_payment( 2 ) != True :
        # clear()
        print( " Not enough Money " )
        print( "Please pay " + str( coffee_query.cost ) + " for " + coffee_query.name )
    
    print( "Thanks for use our services, I hope you like " + coffee_query.name )
    
else:
    print("Sorry, the current machine not have enough resources")



