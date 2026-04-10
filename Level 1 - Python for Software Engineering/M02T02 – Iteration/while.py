numbers=[]
while True:
    num = int(input("Enter a number: "))
    if num == -1:
        break
    
    elif num == 0:
        continue
    else:
        numbers.append(num)

if numbers.count != 0:
    sum = 0
    for x in numbers:
        sum +=x
    average = sum / len(numbers)
else:
    average = -1
print(f"The average of the valid numbers is {average}")