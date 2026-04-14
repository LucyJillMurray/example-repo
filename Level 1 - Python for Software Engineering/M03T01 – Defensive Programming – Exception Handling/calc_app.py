def calculator(x, y, operator):
    """
    Apply an operation to two numbers
    Parameters: Two numbers and an operator (+,-,*,/)
    """
    result = 0
    if operator == "+":
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "*":
        result = x * y
    elif operator == "/":
        if y == 0:
            print("Cannot divide by zero")
            return
        result = x / y
    else:
        raise Exception(f"{operator} is not supported by this calculator")
    # Write equation to history file (equations.txt)
    with open("equations.txt", "a") as file:
        file.write(f"{x} {operator} {y} = {result}\n")
    print(f"The result is {result}")
    return result


process = input(
    "Would you like to see the history or perform a calculation:(hist/calc): "
).lower()
if process == "calc":
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number")

    operator = input("Enter operator: ")
    calculator(x, y, operator)

elif process == "hist":
    try:
        with open("equations.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)
    except FileNotFoundError as error:
        print("There is no history yet")
        print(error)

else:
    print("Please enter calc or hist")
