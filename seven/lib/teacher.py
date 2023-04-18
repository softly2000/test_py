from user import User  # Импорт класса User из файла user.py

class Teacher(User):  # Класс Teacher наследуется от класса User
    def __init__(self, login, password, access_rights, courses, student_groups):
        super().__init__(login, password, access_rights)  # Вызов конструктора родительского класса
        self.courses = courses
        self.student_groups = student_groups
    
    def get_courses(self):
        return self.courses
    
    def set_courses(self, courses):
        self.courses = courses
    
    def get_student_groups(self):
        return self.student_groups
    
    def set_student_groups(self, student_groups):
        self.student_groups = student_groups
