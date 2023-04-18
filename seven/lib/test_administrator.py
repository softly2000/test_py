class TestAdministrator:
    def __init__(self, test_storage):
        self.test_storage = test_storage

    def create_test(self, test_name, test_date, test_time):
        # Создание нового теста с заданными параметрами
        new_test = {
            'test_name': test_name,
            'test_date': test_date,
            'test_time': test_time,
            'questions': []
        }

        # Добавление теста в хранилище тестов
        self.test_storage.append(new_test)

        # Возвращение созданного теста
        return new_test

    def add_question(self, test_name, question):
        # Поиск теста по названию
        test = self._find_test_by_name(test_name)

        if test is not None:
            # Добавление вопроса в указанный тест
            test['questions'].append(question)
            return "Success: Question added to test."
        else:
            return "Error: Test not found."

    def remove_question(self, test_name, question):
        # Поиск теста по названию
        test = self._find_test_by_name(test_name)

        if test is not None:
            # Проверка, есть ли указанный вопрос в тесте
            if question in test['questions']:
                # Удаление вопроса из теста
                test['questions'].remove(question)
                return "Success: Question removed from test."
            else:
                return "Error: Question not found in test."
        else:
            return "Error: Test not found."

    def update_question(self, test_name, question, new_answers, new_correct_answer):
        # Поиск теста по названию
        test = self._find_test_by_name(test_name)

        if test is not None:
            # Проверка, есть ли указанный вопрос в тесте
            for q in test['questions']:
                if q['question'] == question:
                    # Обновление информации о вопросе
                    q['answers'] = new_answers
                    q['correct_answer'] = new_correct_answer
                    return "Success: Question updated."
            return "Error: Question not found in test."
        else:
            return "Error: Test not found."

    def assign_test_to_group(self, test_name, group):
        # Поиск теста по названию
        test = self._find_test_by_name(test_name)

        if test is not None:
            # Назначение теста указанной группе
            test['group'] = group
            return "Success: Test assigned to group."
        else:
            return "Error: Test not found."

    def assign_test_to_student(self, test_name, student):
        # Поиск теста по названию
        test = self._find_test_by_name(test_name)

        if test is not None:
            # Назначение теста указанному студенту
            test['student'] = student
            return "Success: Test assigned to student."
        else:
            return "Error: Test not found."

    def change_test_date(self, test_name, new_date, new_time):
        # Поиск теста по названию
        test = self._find_test_by_name(test_name)

        if test is not None:
            # Проверка, что новая дата и время теста не конфликтуют с другими запланированными событиями
            if self._is_valid_datetime(new_date, new_time):
            # Изменение даты и времени теста в хранилище информации
                test['test_date'] = new_date
                test['test_time'] = new_time
                return "Error: Invalid date or time."
            else:
                return "Error: Invalid date or time."
        else:
            return "Error: Test not found."
    def delete_test(self, test_name):
        # Поиск теста по названию
        test = self._find_test_by_name(test_name)

        if test is not None:
            # Проверка, что тест был назначен и еще не прошел
            if 'group' in test or 'student' in test:
                return "Error: Test cannot be deleted. It has been assigned to a group or a student."
            else:
                # Удаление информации о тесте из хранилища
                self.test_storage.remove(test)
                return "Success: Test deleted."
        else:
            return "Error: Test not found."

    def _find_test_by_name(self, test_name):
        # Вспомогательный метод для поиска теста по названию
        for test in self.test_storage:
            if test['test_name'] == test_name:
                return test
        return None

    def _is_valid_datetime(self, date, time):
        # Вспомогательный метод для проверки корректности даты и времени
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            datetime.datetime.strptime(time, '%H:%M')
            return True
        except ValueError:
            return False
 