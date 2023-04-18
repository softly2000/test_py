class TestTaker:
    def __init__(self, student, test_bank, grader, report):
        self.student = student
        self.test_bank = test_bank
        self.grader = grader
        self.report = report
        self.test_session = None
        self.test_results = None

    def start_test(self):
        self.test_session = TestSession()
        print("Welcome to the test!")
        self.student_name = input("Please enter your name: ")
        self.test_session.load_test(self.test_bank)
        self.display_question()

    def display_question(self):
        current_question = self.test_session.get_current_question()
        print("Question: ", current_question.question_text)
        print("Options: ")
        for i, option in enumerate(current_question.options):
            print(f"{i+1}. {option}")
        self.get_student_answer()

    def get_student_answer(self):
        student_answer = input("Enter your answer (1-4): ")
        if student_answer.isdigit() and int(student_answer) in range(1, 5):
            current_question = self.test_session.get_current_question()
            self.grader.check_answer(current_question, int(student_answer))
            self.test_session.save_student_answer(int(student_answer))
            self.check_remaining_questions()
        else:
            print("Error: Please enter a valid option (1-4).")
            self.get_student_answer()

    def check_remaining_questions(self):
        if self.test_session.has_remaining_questions():
            self.display_question()
        else:
            self.generate_test_report()

    def generate_test_report(self):
        self.test_results = TestResults(self.student_name, self.test_session.get_student_answers(),
                                        self.grader.get_score(), self.test_session.get_total_questions())
        self.report.generate_report(self.test_results)
        print("Test completed. Thank you!")

    def run_test(self):
        self.start_test()
