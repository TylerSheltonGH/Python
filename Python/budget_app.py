# Function to create a spend chart based on spending percentages of categories
def create_spend_chart(categories):
    # Calculate the total amount spent in each category and store it in a list
    spent_percentages = []
    for category in categories:
        withdrawals = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        total_spent = abs(withdrawals)
        spent_percentages.append(total_spent)

    # Calculate the bar heights for each category (in multiples of 10) for the spend chart
    bar_heights = [(spent // 10) * 10 for spent in spent_percentages]

    # Construct the spend chart string with percentage bars and category names
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for height in bar_heights:
            if height >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Find the maximum length of category names and align them properly in the chart
    max_name_length = max(len(category.name) for category in categories)
    padded_names = [category.name.ljust(max_name_length) for category in categories]

    for i in range(max_name_length):
        chart += " " * 5
        for name in padded_names:
            chart += name[i] + "  "
        chart += "\n"

    return chart

# Define the Category class
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # String representation of the Category object showing the name, transactions, and total balance
    def __str__(self):
        title = f"{self.name.center(30, '*')}"
        result = title + '\n'
        for item in self.ledger:
            result += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
        result += f"Total: {self.get_balance():.2f}"
        return result

    # Method to deposit funds to the category
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # Method to withdraw funds from the category if there are enough funds available
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    # Method to calculate and return the current balance of the category
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    # Method to transfer funds from this category to another category if enough funds are available
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    # Method to check if there are enough funds available in the category for withdrawal or transfer
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

# Test cases
# Create instances of the Category class
food_category = Category("Food")
clothing_category = Category("Clothing")
entertainment_category = Category("Entertainment")

# Perform transactions on the categories
food_category.deposit(2500, "initial deposit")
food_category.withdraw(73.45, "groceries")
food_category.withdraw(32.44, "restaurant and more food")
food_category.transfer(50, clothing_category)

clothing_category.deposit(250, "initial deposit")
clothing_category.withdraw(123.46, "clothes")

entertainment_category.deposit(560, "initial deposit")
entertainment_category.withdraw(53.64, "movie tickets")

# Print the category details (transactions and total balance) and spend chart
print(food_category)
print(clothing_category)
print(entertainment_category)

print(create_spend_chart([food_category, clothing_category, entertainment_category]))
