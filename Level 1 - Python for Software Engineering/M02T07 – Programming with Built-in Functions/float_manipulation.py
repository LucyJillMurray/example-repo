import statistics

number = input("Enter ten floats separated by commas: ")
numbers = number.split(",")
# Check exactly ten numbers have been added
if len(numbers) == 10:
    # Error handling in case non numbers are entered
    # learned w3schools
    try:
        # Convert strings to floats
        float_numbers = [float(x) for x in numbers]
    except ValueError:
        print("Please only enter numbers")
        exit()

    # Find total
    total = sum(float_numbers)
    print(f"The total is {total}")

    maximum = float_numbers.index(max(float_numbers))
    print(f"The index of the maximum is {maximum}")

    minimum = float_numbers.index(min(float_numbers))
    print(f"The index of the minimum is {minimum}")

    mean = statistics.mean(float_numbers)
    print(f"The mean is {round(mean, 2)}")

    median = statistics.median(float_numbers)
    print(f"The median is {round(median, 2)}")

else:
    print("Please enter exactly ten numbers")
