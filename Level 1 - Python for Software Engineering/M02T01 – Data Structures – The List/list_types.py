friends_names = ["Sarah" , "Elizabeth" , "Benjamin"]
friends_ages = [30 , 32 , 28]

print(f"First Friend: {friends_names[0]}")
print(f"Last Friend: {friends_names[-1]}")
print(f"Length of Friends list: {len(friends_names)}")

for x in range(len(friends_names)): # learned for loops from w3schools
    print(f"{friends_names[x]} is {friends_ages[x]} years old")