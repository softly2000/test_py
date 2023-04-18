class Grader:
    def __init__(self):
        pass

    def grade_test(self, student_answers, correct_answers):
        """
        Метод для проверки ответов студента на тест.

        :param student_answers: список ответов студента на тест
        :param correct_answers: список правильных ответов на тест
        :return: количество баллов за тест
        """
        total_points = 0
        for i in range(len(student_answers)):
            points = self.calculate_points(student_answers[i], correct_answers[i])
            total_points += points

        return total_points

    def check_answer(self, student_answer, correct_answer):
        """
        Метод для сравнения ответа студента с правильным ответом на вопрос.

        :param student_answer: ответ студента на вопрос
        :param correct_answer: правильный ответ на вопрос
        :return: True, если ответы совпадают, иначе - False
        """
        return student_answer == correct_answer

    def calculate_points(self, student_answer, correct_answer):
        """
        Метод для вычисления количества баллов за данную пару ответов на вопрос.

        :param student_answer: ответ студента на вопрос
        :param correct_answer: правильный ответ на вопрос
        :return: количество баллов за ответ на вопрос
        """
        if self.check_answer(student_answer, correct_answer):
            return 1
        else:
            return 0
