class ManuallyGrader:
    def __init__(self):
        self.test = None
        self.grade_dict = {}

    def set_test(self, test):
        self.test = test

    def grade(self, question, answer):
        if question not in self.test.questions:
            return "Question not found"
        correct_answer = self.test.questions[question].correct_answer
        if answer == correct_answer:
            self.grade_dict[question] = 1
            return "Correct"
        else:
            self.grade_dict[question] = 0
            return "Incorrect"

    def get_grade(self):
        total_questions = len(self.test.questions)
        total_correct = sum(self.grade_dict.values())
        grade_percent = total_correct / total_questions * 100
        return f"Grade: {grade_percent}% ({total_correct}/{total_questions})"
