from data import menu, resources


# TODO 1: print report of available resources
def report():
    """prints a report of the available resources in machine"""
    print(f"Available Resources:\n"
          f"Water: {resources['water']} ml \n"
          f"Milk: {resources['milk']} ml \n"
          f"Coffee: {resources['coffee']} g")


# TODO 3 Check for resource availability of ingredients for the order
def resource_availability(order):
    """Returns "Yes" if ingredients are available, insufficient if not available"""
    if order == 'espresso':
        if resources["water"] > menu["espresso"]["ingredients"]["water"]:
            if resources["coffee"] > menu["espresso"]["ingredients"]["coffee"]:
                return "Yes"
            else:
                return "Insufficient Coffee"
        else:
            return "Insufficient Water"
    if order == 'latte':
        if resources["water"] > menu["latte"]["ingredients"]["water"]:
            if resources["coffee"] > menu["latte"]["ingredients"]["coffee"]:
                if resources["milk"] > menu["latte"]["ingredients"]["milk"]:
                    return "Yes"
                else:
                    return "Insufficient Milk"
            else:
                return "Insufficient Coffee"
        else:
            return "Insufficient Water"

    if order == 'cappuccino':
        if resources["water"] > menu["cappuccino"]["ingredients"]["water"]:
            if resources["coffee"] > menu["cappuccino"]["ingredients"]["coffee"]:
                if resources["milk"] > menu["cappuccino"]["ingredients"]["milk"]:
                    return "Yes"
                else:
                    return "Insufficient Milk"
            else:
                return "Insufficient Coffee"
        else:
            return "Insufficient Water"


# TODO 4 : Calculate money
def accounts(pennies, quarters, dimes, nickels, order):
    """Calculates inserted amount and returns balance amount if transaction is accepted or -1 rejected"""
    inserted_amount = pennies * 0.01 + quarters * 0.25 + dimes * 0.1 + nickels * 0.05
    bill = menu[order]["cost"]
    if inserted_amount >= bill:
        resources["money"] += bill
        return round(inserted_amount - bill, 2)
    else:
        return -1


is_on = True

# TODO 2: Ask for user input from menu
while is_on:
    order = input("What would you like to have espresso/latte/cappuccino?\n")
    if order == 'report':
        report()
    else:
        availability = resource_availability(order)
        if availability == "Yes":
            pennies = int(input("How many pennies?\n"))
            nickels = int(input("How many nickels?\n"))
            dimes = int(input("How many dimes?\n"))
            quarters = int(input("How many quarters?\n"))
            return_amount = accounts(pennies=pennies, nickels=nickels, dimes=dimes, quarters=quarters, order=order)
            # TODO 5 Deliver Order and update resources
            if return_amount == -1:
                print("Sorry that is not enough money, Amount refunded")
            else:
                if order == "espresso":
                    resources["milk"] -= menu[order]["ingredients"]["milk"]
                resources["water"] -= menu[order]["ingredients"]["water"]
                resources["coffee"] -= menu[order]["ingredients"]["coffee"]
                print(f"Here is your {order}, and change ${return_amount}")
        else:
            print("Sorry", availability)
            is_on = False
