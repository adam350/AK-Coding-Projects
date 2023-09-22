class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.attendance = []

    def mark_late(self, date):
        self.attendance.append(date)

class Attendance:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def mark_late(self, student_id, date):
        for student in self.students:
            if student.student_id == student_id:
                student.mark_late(date)
                print(f"{student.name} marked as late on {date}.")
                break
            else:
                print(f"student with {student_id} not found.")

    def get_late_students(self, date):
        late_students = []
        for student in self.students:
            if date in student.attendance:
                late_students.append(student.name)
            return late_students