class Student:
    def __init__(self, name, test_stats):
        self.name = name
        self.test_stats = test_stats

class StudentAdministrator:
    def __init__(self):
        self.student_list = []

    def add_student(self, name, test_stats):
        new_student = Student(name, test_stats)
        self.student_list.append(new_student)
        return "Success: Student added."

    def remove_student(self, name):
        for student in self.student_list:
            if student.name == name:
                self.student_list.remove(student)
                return "Success: Student removed."
        return "Error: Student not found."

    def update_student(self, name, test_stats):
        for student in self.student_list:
            if student.name == name:
                student.test_stats = test_stats
                return "Success: Student updated."
        return "Error: Student not found."

