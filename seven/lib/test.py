class Test:
    def __init__(self):
        self.questions = {}
        
    def add_question(self):
        question = input("Введите вопрос: ")
        answer_choices = input("Введите варианты ответа через запятую: ")
        correct_answer = input("Введите правильный ответ: ")
        answer_choices = answer_choices.split(",")
        if correct_answer not in answer_choices:
            return "Ошибка: правильный ответ отсутствует в списке вариантов ответа"
        self.questions[question] = {"answer_choices": answer_choices, "correct_answer": correct_answer}
        return "Вопрос успешно добавлен"
        
    def remove_question(self):
        question = input("Введите вопрос, который нужно удалить: ")
        if question in self.questions:
            del self.questions[question]
            return "Вопрос успешно удален"
        else:
            return "Ошибка: вопрос не найден"
        
    def update_question(self):
        question = input("Введите вопрос, который нужно обновить: ")
        if question in self.questions:
            answer_choices = input("Введите новые варианты ответа через запятую: ")
            correct_answer = input("Введите новый правильный ответ: ")
            answer_choices = answer_choices.split(",")
            if correct_answer not in answer_choices:
                return "Ошибка: правильный ответ отсутствует в списке вариантов ответа"
            self.questions[question] = {"answer_choices": answer_choices, "correct_answer": correct_answer}
            return "Вопрос успешно обновлен"
        else:
            return "Ошибка: вопрос не найден"
