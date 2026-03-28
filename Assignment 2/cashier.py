class Cashier:
    VAL_DOL = 1
    VAL_HALF_DOL = 2
    VAL_QUARTER = .25
    VAL_NICKEL = .05
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        current_amount = []  # Append all amounts to this and add together
        total = 0
        print("Please insert coins:")

        num_dollars = int(input("How many dollars?: ")) * self.VAL_DOL
        current_amount.append(num_dollars)
        num_half_dollars = int(input("How many half dollars?: ")) * self.VAL_HALF_DOL
        current_amount.append(num_half_dollars)

        num_quarters = int(input("How many quarters?: ")) * self.VAL_QUARTER
        current_amount.append(num_quarters)

        num_nickels = int(input("How many nickels?: ")) * self.VAL_NICKEL
        current_amount.append(num_nickels)

        for amount in current_amount:
            total += amount

        return round(total, 2)  # So we can have the proper format

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##
        if coins < cost:
            print("Sorry, that is not enough money. Money refunded.")
            return False
        else:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True