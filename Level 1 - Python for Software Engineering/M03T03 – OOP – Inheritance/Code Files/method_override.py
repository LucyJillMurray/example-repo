class Adult:
    def __init__(self, name, age, hair, eye_color):
        self.name = name
        self.age = age
        self.hair = hair
        self.eye_color = eye_color

    def can_drive(self):
        print(f"{self.name} is old enough to drive")


class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive")


name = input("Enter your name: ")
try:
    age = int(input("Enter your age: "))
except ValueError:
    print(f"Enter a valid number")
    exit()
hair = input("Enter your hair color: ")
eye_color = input("Enter your eye color: ")

# Check if person created is child or adult
if age >= 18:
    person = Adult(name, age, hair, eye_color)
else:
    person = Child(name, age, hair, eye_color)

person.can_drive()
