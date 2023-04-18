class StudentProgressTracker:
    def __init__(self, student_id, test_results, test_dates, group_name):
        self.student_id = student_id
        self.test_results = test_results
        self.test_dates = test_dates
        self.group_name = group_name
    
    def view_test_results(self):
        return self.test_results.get(self.student_id, None)
    
    def view_test_dates(self):
        return self.test_dates.get(self.student_id, None)
    
    def compare_results(self, group_manager):
        group = group_manager.get_group(self.group_name)
        if group is None:
            return None
        group_results = []
        for student_id in group.student_ids:
            results = self.test_results.get(student_id, None)
            if results is not None:
                group_results.append(results)
        return group_results
    
    def view_group_stats(self, group_manager):
        group = group_manager.get_group(self.group_name)
        if group is None:
            return None
        group_results = self.compare_results(group_manager)
        if not group_results:
            return None
        num_students = len(group_results)
        max_scores = [max(results) for results in group_results]
        min_scores = [min(results) for results in group_results]
        avg_scores = [sum(results)/len(results) for results in group_results]
        return {'num_students': num_students, 'max_scores': max_scores, 'min_scores': min_scores, 'avg_scores': avg_scores}
    
    def generate_student_report(self):
        results = self.test_results.get(self.student_id, None)
        dates = self.test_dates.get(self.student_id, None)
        if results is None or dates is None:
            return None
        report = f"Student ID: {self.student_id}\nTest Results: {results}\nTest Dates: {dates}"
        return report
