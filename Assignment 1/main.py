### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}

# Constants for when we process coins
VAL_DOL = 1
VAL_HALF_DOL = 0.5
VAL_QUARTER = .25
VAL_NICKEL = .05

### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, user_ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in user_ingredients:
            if self.machine_resources[item] < user_ingredients[item]:
                print(f"Sorry, there is not enough {item}")
                return False
        return True


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        current_amount = [] # Append all amounts to this and add together
        total = 0
        print("Please insert coins:")

        num_dollars = int(input("How many dollars?: ")) * VAL_DOL
        current_amount.append(num_dollars)
        num_half_dollars = int(input("How many half dollars?: ")) * VAL_HALF_DOL
        current_amount.append(num_half_dollars)

        num_quarters = int(input("How many quarters?: ")) * VAL_QUARTER
        current_amount.append(num_quarters)

        num_nickels = int(input("How many nickels?: ")) * VAL_NICKEL
        current_amount.append(num_nickels)

        for amount in current_amount:
            total += amount

        return round(total, 2) # So we can have the proper format

    def transaction_result(self, user_coins, user_cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if user_coins < user_cost:
            print("Sorry, that is not enough money. Money refunded.")
            return False
        else:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for recipe in order_ingredients:
            self.machine_resources[recipe] -= order_ingredients[recipe]

        print(f"{sandwich_size} is ready. Bon appetit!")

    def report(self):
        """Print remaining resources."""
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} ounce(s)")

### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwich_maker = SandwichMachine(resources)
is_on = True

while is_on:
    user_input = input("What would you like? (small/medium/large/off/report): ").lower()

    if user_input == "off":
        is_on = False
    elif user_input == "report":
        sandwich_maker.report()
    elif user_input in ["small", "medium", "large"]:
        ingredients = recipes[user_input]["ingredients"]
        cost = recipes[user_input]["cost"]

        if sandwich_maker.check_resources(ingredients):
            coins = sandwich_maker.process_coins()

            if sandwich_maker.transaction_result(coins, cost):
                sandwich_maker.make_sandwich(user_input, ingredients)
    else:
        print("Sorry, that is not a valid input.")
