from data import MENU, resources


def check_resources(coffee):
    if MENU[coffee]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is no enough water.")
        quit(0)
    if MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is no enough coffee.")
        quit(0)
    if coffee != "espresso" and MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is no enough milk.")
        quit(0)


def espresso():
    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]


def latte():
    resources["water"] -= MENU["latte"]["ingredients"]["water"]
    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]


def cappuccino():
    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]


def report():
    print(f'water: {resources["water"]}')
    print(f'milk: {resources["milk"]}')
    print(f'coffee: {resources["coffee"]}')
    print(f'amount: {resources["amount"]}')


def game():
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == "report":
        report()
        return
    elif user_input == "off":
        print("Turning off....")
        quit(0)
    check_resources(user_input)
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount = (0.25*quarter) + (0.1*dimes) + (0.05*nickles) + (0.01*pennies)
    if MENU[user_input]["cost"] > amount:
        print("Sorry that's not enough money. Money refunded.")
        return
    resources["amount"] += MENU[user_input]["cost"]
    refund = amount - MENU[user_input]["cost"]
    if refund>0:
        print(f"Here is ${refund} in change.")
    if user_input == "espresso":
        # check resources intake and outtake
        espresso()
    elif user_input == "latte":
        latte()
    elif user_input == "cappuccino":
        cappuccino()



if __name__ == "__main__":
    while True:
        game()




