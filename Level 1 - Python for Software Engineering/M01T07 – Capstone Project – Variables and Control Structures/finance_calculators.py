import math

# Display menu options to user
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a homeloan.")
# Ask user to choose calculation type
invest_type = input("Enter either “investment” or “bond” from the menu above to proceed: ")

# Convert input to uppercase to make input case-insensitive
cap_invest_type = invest_type.upper()

# Investment type
if cap_invest_type == "INVESTMENT":
    capital  = float(input("Enter amount of money depositing: "))
    int_rate = float(input("Enter the interest rate without a percentage symbol: "))
    time     = float(input("Enter the number of years you plan on investing for: "))
    interest = input("Enter the type of interest (compound/simple): ")
    cap_int  = interest.upper() # Convert to uppercase to make input case-insensitive
    
    if cap_int == "SIMPLE":
        output = capital * (1 + int_rate/100 * time)
    elif cap_int == "COMPOUND":
        output = capital * math.pow((1 + int_rate/100), time)
    
    # Handle invalid interest type
    else:
        print("Please only enter the words 'compound' or 'simple'")
        exit()  # Exit the program to prevent errors (learned from external help)

    print(f"The amount you get back on your investment with {interest} interest is {output:.2f}") # Round to 2 decimal places for currency (learned from stack overflow)

# Bond Type
elif cap_invest_type == "BOND":
    value     = float(input("Enter the present value of the house: "))
    int_rate  = float(input("Enter the interest rate without a percentage symbol: "))
    time      = float(input("Enter the number of months you plan to take to repay the bond over: "))
    i         = (int_rate / 100) / 12      # Convert annual interest rate to monthly rate
    repayment = (i * value) / (1 - (1 + i)**(-time))

    print(f"The amount of your monthly repayment on an interest rate of {int_rate} over {time} months is {repayment:.2f}") # Round to 2 decimal places for currency (learned from stack overflow)

# Handle invalid input
else:
    print("Please only enter the words investment or bond")


