number_students = int(input("Enter the number of students registering: "))

for i in range(number_students):
    student_id = input("Enter student id number: ")

    with open("reg_form.txt", "a") as file:
        file.write(f"{student_id} ..........\n")