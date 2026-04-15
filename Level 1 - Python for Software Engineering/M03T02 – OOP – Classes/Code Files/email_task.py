"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #


class Email:

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True


def populate_inbox(email_address, subject_line, email_content):
    your_email = Email(email_address, subject_line, email_content)
    inbox.append(your_email)


def list_emails():
    # learned from https://www.geeksforgeeks.org/python/enumerate-in-python/
    for index, email in enumerate(inbox):
        print(f"{index}: {email.subject_line}")


def read_emails(index):
    print(f"Email Address: {inbox[index].email_address}")
    print(f"Email subject: {inbox[index].subject_line}")
    print(f"Email content: {inbox[index].email_content}")

    inbox[index].mark_as_read()


def view_unread_emails():
    for x in range(len(inbox)):
        if not inbox[x].has_been_read:
            print(f"{x} {inbox[x].subject_line}")


# --- Email Program --- #
# Populate emails
inbox = []
populate_inbox(
    "Murray.lucy04@gmail.com", "Important", "please print these letters for me"
)
populate_inbox("Murray.lucy04@gmail.com", "not important", "Did you see this meme")
populate_inbox("Murray.lucy04@gmail.com", "Hyperion dev", "I have started a course")


# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        list_emails()
        try:
            email_index = int(
                input("Enter the index of the email you would like to read: ")
            )
        except ValueError:
            print("Please enter a valid number")
            continue
        if email_index < len(inbox):
            read_emails(email_index)
        else:
            print("There is no email with that index")
            continue

    elif user_choice == 2:
        view_unread_emails()

    elif user_choice == 3:
        exit()

    else:
        print("Oops - incorrect input.")
