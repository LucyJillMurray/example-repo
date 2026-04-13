import statistics

number = input("Enter ten floats: ")
numbers = number.split(",")
float_numbers = [float(x) for x in numbers]

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
