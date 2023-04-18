class CourseInfoDisplay:
    def __init__(self, courses, students):
        self.courses = courses
        self.students = students
    
    def get_student_grades(self, student_id):
        grades = {}
        for course in self.courses:
            if student_id in course.get_student_ids():
                grades[course.get_course_name()] = course.get_student_grade(student_id)
        return grades
    
    def get_course_info(self, course_name):
        for course in self.courses:
            if course.get_course_name() == course_name:
                return {
                    "name": course.get_course_name(),
                    "start_date": course.get_start_date(),
                    "end_date": course.get_end_date(),
                    "teacher": course.get_teacher(),
                    "students": course.get_students(),
                }
        return None
    
    def display_student_info(self, student_id):
        student = self.students.get_student_by_id(student_id)
        if not student:
            print("Student not found")
            return
        print(f"Student: {student.get_full_name()}, Group: {student.get_group_number()}")
        grades = self.get_student_grades(student_id)
        if grades:
            print("Grades:")
            for course_name, grade in grades.items():
                print(f"{course_name}: {grade}")
        else:
            print("No grades found.")
    
    def display_course_info(self, course_name):
        course_info = self.get_course_info(course_name)
        if not course_info:
            print("Course not found")
            return
        print(f"Course: {course_info['name']}, Teacher: {course_info['teacher']}")
        print(f"Start date: {course_info['start_date']}, End date: {course_info['end_date']}")
        if course_info['students']:
            print("Students and grades:")
            for student_id, grade in course_info['students'].items():
                student = self.students.get_student_by_id(student_id)
                if student:
                    print(f"{student.get_full_name()} ({student_id}): {grade}")
                else:
                    print(f"{student_id}: {grade}")
        else:
            print("No students found.")
    
    def display_all_courses_info(self):
        for course in self.courses:
            self.display_course_info(course.get_course_name())
            print()
