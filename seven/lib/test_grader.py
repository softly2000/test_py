class TestGrader:
    
    def __init__(self, test):
        self.test = test
        self.student_answers = {}
        self.grades = {}
        
    def grade_test(self):
        for student, answers in self.student_answers.items():
            grade = 0
            for i, answer in enumerate(answers):
                if self.check_answer(answer, self.test.questions[i]):
                    grade += 1
            self.grades[student] = grade
    
    def check_answer(self, answer, question):
        return answer == question.correct_answer
    
    def manually_grade_test(self, student, grade):
        self.grades[student] = grade
        
    def display_test_results(self, student):
        print(f"Test Results for Student {student}:")
        print(f"Grade: {self.grades[student]}")
        for i, answer in enumerate(self.student_answers[student]):
            print(f"Question {i+1}: {answer}")
        print()
