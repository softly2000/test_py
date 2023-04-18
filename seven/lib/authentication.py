class Authentication:
    def __init__(self, db):
        self.db = db

    def login(self):
        # Проверка, не авторизован ли пользователь уже в системе
        if self.db.get_session():
            print("Вы уже авторизованы в системе.")
            return False

        # Запросить у пользователя логин и пароль
        username = input("Введите логин: ")
        password = input("Введите пароль: ")

        # Проверить корректность введенных данных
        if not self.db.check_user(username, password):
            print("Неверный логин или пароль.")
            return False

        # Создать сессию для пользователя и сохранить ее в базе данных
        self.db.create_session(username)
        print("Вы успешно авторизовались в системе.")
        return True

    def logout(self):
        # Проверить, авторизован ли пользователь в системе
        if not self.db.get_session():
            print("Вы не авторизованы в системе.")
            return False

        # Удалить сессию пользователя из базы данных
        self.db.delete_session()
        print("Вы успешно вышли из системы.")
        return True
