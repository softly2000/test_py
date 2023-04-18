class TestSession:
    def __init__(self, test, students):
        self.test = test
        self.students = students

    def start_test(self):
        test_questions = self.test.get_questions()
        for student in self.students:
            input("Press enter to start the test, " + student.name)
            student_answers = []
            for question in test_questions:
                student_answer = student.answer_question(question)
                student_answers.append(student_answer)
            student.test_results = self.test.check_answers(student_answers)
        return self.get_test_results()

    def save_test_results(self):
        for student in self.students:
            student.save_test_results()
        return "Test results saved successfully."

    def get_test_results(self):
        test_results = []
        for student in self.students:
            test_results.append({"name": student.name, "test_results": student.test_results})
        return test_results
