import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    ###  write the rest of the codes ###
    is_on = True

    while is_on:
        user_input = input("What would you like? (small/medium/large/off): ").lower()

        if user_input == "off":
            is_on = False
        elif user_input in ["small", "medium", "large"]: # Code doesn't have report anymore since it isn't in the skeleton
            ingredients = recipes[user_input]["ingredients"]
            cost = recipes[user_input]["cost"]

            # Uses new instances
            if sandwich_maker_instance.check_resources(ingredients):
                coins = cashier_instance.process_coins()

                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(user_input, ingredients)
        else:
            print("Sorry, that is not a valid input.")


if __name__=="__main__":
    main()