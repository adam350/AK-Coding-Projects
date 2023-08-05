class attendance:
    def __init__(self, name, form_class, studentID, ):
        self.name = name
        self.form_class = form_class
        self.studentID = studentID

    def add_name(self, student_name):
        self.name = student_name

    def add_formClass(self, student_class):
        self.form_class = student_class

    def add_studentID(self, student_ID):
        self.studentID = student_ID

person1 = attendance("Adam", "12B", 12345)

while True:
    action_name = input("Please enter your full name: ")
    action_class = input("Please enter your form class: ")
    action_ID = input("Please enter the last 5 digits of your student ID card: ")

    if action_ID == "":
        print("Error. Please enter your student ID")
        if len(action_ID) > 5 or len(action_ID) <= 4:
            print("Error. Invalid student ID. Please try again.")
    elif action_name == "":
        print("Error. Please try again.")
    elif action_class == "":
        print("Error. Try again.")
    else:
        print("Valid entry. Thank you!")
        continue



