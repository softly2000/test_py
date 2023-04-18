class Course:
    def __init__(self, course_id, course_name, course_description):
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description
        self.tests = []
        self.students = []
        
    def add_test(self, test):
        self.tests.append(test)
        
    def remove_test(self, test):
        self.tests.remove(test)
        
    def get_tests(self):
        return self.tests
    
    def add_student(self, student):
        self.students.append(student)
        
    def remove_student(self, student):
        self.students.remove(student)
        
    def get_students(self):
        return self.students
    
    def get_course_id(self):
        return self.course_id
    
    def set_course_name(self, course_name):
        self.course_name = course_name
        
    def get_course_name(self):
        return self.course_name
