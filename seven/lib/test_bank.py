class TestBank:
    def __init__(self):
        self.tests = []
    
    def add_test(self, test):
        """
        Добавляет новый тест в список тестов
        :param test: экземпляр класса Test
        :return: True, если тест успешно добавлен, иначе False
        """
        if isinstance(test, Test):
            self.tests.append(test)
            return True
        return False
    
    def remove_test(self, test):
        """
        Удаляет тест из списка тестов
        :param test: экземпляр класса Test
        :return: True, если тест успешно удален, иначе False
        """
        if test in self.tests:
            self.tests.remove(test)
            return True
        print("Тест не найден.")
        return False
    
    def update_test(self, test, **kwargs):
        """
        Обновляет информацию о тесте
        :param test: экземпляр класса Test
        :param kwargs: словарь с новыми значениями атрибутов теста
        :return: True, если информация о тесте успешно обновлена, иначе False
        """
        if test in self.tests:
            for key, value in kwargs.items():
                setattr(test, key, value)
            return True
        print("Тест не найден.")
        return False
