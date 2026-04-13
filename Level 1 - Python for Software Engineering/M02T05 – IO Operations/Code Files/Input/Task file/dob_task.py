with open("DOB.txt", "r") as file:
    lines = file.readlines()

names = []
birthdates = []

for line in lines:
    temp = line.split()
    if temp:  # Check if  list is empty, learned from stack overflow        
        names.append(temp[0] + " " + temp[1])
        birthdates.append(temp[2] + " " + temp[3] + " " + temp[4])

print("Name")
for name in names:
    print(name)

print("\nBirthdate")
for date in birthdates:
    print(date)
