class Report:
    def __init__(self, tests):
        self.tests = tests
    
    def generate_report(self, student_id):
        if student_id not in self.tests:
            return "No test results found for student with ID {}".format(student_id)
        
        test = self.tests[student_id]
        report = "Test report for student with ID {}\n\n".format(student_id)
        
        for i, question in enumerate(test["questions"]):
            report += "Question {}: {}\n".format(i+1, question["text"])
            report += "Student answer: {}\n".format(question["student_answer"])
            report += "Correct answer: {}\n\n".format(question["correct_answer"])
        
        return report
    
    def generate_group_report(self, group_id):
        group_report = "Test report for group with ID {}\n\n".format(group_id)
        
        for student_id in self.tests:
            if self.tests[student_id]["group_id"] == group_id:
                student_report = self.generate_report(student_id)
                group_report += student_report
        
        if len(group_report) == len("Test report for group with ID {}\n\n".format(group_id)):
            return "No test results found for group with ID {}".format(group_id)
        
        return group_report
    
    def generate_summary_report(self):
        summary_report = "Summary test report\n\n"
        total_students = len(self.tests)
        total_scores = sum(test["score"] for test in self.tests.values())
        avg_score = round(total_scores/total_students, 2)
        good_scores = len([test for test in self.tests.values() if test["score"] >= 80])
        good_percent = round((good_scores/total_students)*100, 2)
        excellent_scores = len([test for test in self.tests.values() if test["score"] >= 90])
        excellent_percent = round((excellent_scores/total_students)*100, 2)
        
        summary_report += "Total students: {}\n".format(total_students)
        summary_report += "Average score: {}\n".format(avg_score)
        summary_report += "Number of students with score >= 80: {}, {}%\n".format(good_scores, good_percent)
        summary_report += "Number of students with score >= 90: {}, {}%\n".format(excellent_scores, excellent_percent)
        
        return summary_report
