class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def printhead_office(self):
        print("The head office location is Cape Town")


class OOPCourse(Course):
    def __init__(self, description="OOP Fundamentals", trainer="Mr Anon A. Mouse"):
        # Call the parent class constructor to initialise inherited attributes
        super().__init__()
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        print(f"Course Description: {self.description}")
        print(f"Trainer Name: {self.trainer}")

    def show_course_id(self):
        print("The course ID is #12345")


# Create an instance of the Course class
course = Course()
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()


# Call the contact_details method to display contact information
course.contact_details()
