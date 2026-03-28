class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                print(f"Sorry, there is not enough {item}")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        ########
        for recipe in order_ingredients:
            self.machine_resources[recipe] -= order_ingredients[recipe]

        print(f"{sandwich_size} is ready. Bon appetit!")