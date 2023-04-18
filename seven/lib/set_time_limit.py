class SetTimeLimit:
    def __init__(self):
        self.time_limit = 0  # инициализация временного ограничения на 0

    def set_time_limit(self):
        """
        Установка временного ограничения на прохождение теста
        :return: статус выполнения метода (True - успешно, False - неуспешно)
        """
        try:
            self.time_limit = int(input("Введите временное ограничение на прохождение теста (в минутах): "))
            # преобразование введенного значения в целое число
            if self.time_limit <= 0:
                # проверка на положительность числа
                print("Ошибка: время должно быть положительным числом")
                return False
        except ValueError:
            # обработка исключения неправильного формата введенного значения
            print("Ошибка: введите целое положительное число")
            return False
        else:
            # если введенное значение корректно, выводим подтверждение и устанавливаем ограничение
            print(f"Временное ограничение на прохождение теста установлено: {self.time_limit} мин.")
            # запись результатов в лог
            with open('log.txt', 'a') as f:
                f.write(f"Установлено временное ограничение: {self.time_limit} мин.\n")
            return True
