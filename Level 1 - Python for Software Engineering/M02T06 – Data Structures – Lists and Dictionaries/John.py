input_string = ""
incorrect_names = []
while True:
    input_string = input("Enter your name: ").upper()
    if input_string == "JOHN":
        break
    incorrect_names.append(input_string.capitalize())

print(f"Incorrect Names: {incorrect_names}")
