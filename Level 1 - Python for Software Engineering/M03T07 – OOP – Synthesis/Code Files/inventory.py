from tabulate import tabulate


# ========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        country = self.country
        code = self.code
        product = self.product
        cost = self.cost
        quantity = self.quantity

        return f"{country},{code},{product},{cost},{quantity}"


# =============Shoe list===========
"""
The list will be used to store a list of objects of shoes.
"""
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

        # Skip over header
        for index, line in enumerate(lines[1:], start=2):
            line = line.strip()
            line = line.split(",")

            # Check each line has exactly five items
            if len(line) == 5:
                shoe = Shoe(line[0], line[1], line[2], line[3], line[4])
                shoe_list.append(shoe)
            else:
                print(f"Incorrect number of items in file on line {index}")
                raise (ValueError)

    except FileNotFoundError as error:
        print("There is no inventory file")
        print(error)


def capture_shoes():
    country = input("Enter the shoes country: ").capitalize()
    code = input("Enter the shoes code: ")
    product = input("Enter the shoes product name: ").capitalize()
    try:
        cost = int(input("Enter the shoes cost: "))
        quantity = int(input("Enter the quantity of shoes: "))
    except ValueError:
        print("Please input a number for cost and quantity")
        return

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    with open("inventory.txt", "a") as file:
        file.write(f"{shoe}\n")
    print(f"{shoe} added!")


def view_all():
    """
    This function will iterate over the shoes list and print
    """
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    #  Create list of lists for tabulate
    rows = []
    for s in shoe_list:
        rows.append([s.country, s.code, s.product, s.cost, s.quantity])

    # Learned from geeksforgeeks
    table = tabulate(rows, headers=headers)
    print(table)


def re_stock():
    """
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked.
    This quantity is updated on the file for this shoe.
    """
    min_stock = min(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"{min_stock.product} has {min_stock.quantity} in stock")

    # Ask for input until yes or no is inputted
    while True:
        restock = input(f"Would you like to restock {min_stock.product}: ")
        if restock.upper() == "YES":
            increase = int(input("Enter the quantity of stock to be added: "))
            shoe_index = shoe_list.index(min_stock)
            shoe_list[shoe_index].quantity += increase
            print(f"New quantity is {shoe_list[shoe_index].quantity}")
            #  use right to overwrite the previous file
            with open("inventory.txt", "w") as file:
                file.write("Country,Code,Product,Cost,Quantity\n")
            # Use append to not overwrite the title
            with open("inventory.txt", "a") as file:
                for shoe in shoe_list:
                    file.write(f"{shoe}\n")
            break
        elif restock.upper() == "NO":
            break
        else:
            print("please input 'YES' or 'NO'")


def search_shoe():
    """
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    """
    code = input("Enter the shoe code: ")
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe

    return None


def value_per_item():
    """
    This function will calculate the total value for each item.
    value = cost * quantity.
    """
    for shoe in shoe_list:
        value = shoe.get_quantity() * shoe.get_cost()
        print(f"Value of {shoe.product} is R{value}")


def highest_qty():
    """
    Finds the shoe with the highest stock
    Print this shoe as being for sale.
    """
    max_stock = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"{max_stock.product} is for sale")


# ==========Main Menu=============
"""
Takes a number input to decide on what to do
"""

read_shoes_data()
while True:
    try:
        user_choice = int(
            input(
                """\nWould you like to:
        1. View the inventory
        2. Query the value of the inventory
        3. Search for a specific product
        4. Check which stock has the highest quantity
        5. Restock
        6. Add a new product
        7. Quit application

        Enter selection: """
            )
        )

        if user_choice == 1:
            view_all()

        elif user_choice == 2:
            value_per_item()

        elif user_choice == 3:
            shoe = search_shoe()
            if shoe:
                print(shoe)
            else:
                print("There is no shoe with that code")

        elif user_choice == 4:
            highest_qty()

        elif user_choice == 5:
            re_stock()

        elif user_choice == 6:
            capture_shoes()

        elif user_choice == 7:
            exit()

        else:
            print("Oops - incorrect input.")

    except ValueError:
        print("Please enter a number")
        continue
