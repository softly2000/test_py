import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QDialog, QLineEdit, QComboBox


class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Создание метки с текстом "Добро пожаловать"
        welcome_label = QLabel("Добро пожаловать", self)
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("font-size: 20px; font-weight: bold;")

        # Создание двух зеленых кнопок
        student_button = QPushButton("Я Студент", self)
        student_button.setStyleSheet(" background-color: #3CB371; color: white; height: 30px; width: 120px; border-radius: 20px; font-size: 10px;")
        teacher_button = QPushButton("Я Преподователь", self)
        teacher_button.setStyleSheet(" background-color: #3CB371; color: white; height: 30px; width: 120px; border-radius: 20px; font-size: 10px;")

        # Создание главного вертикального макета
        main_layout = QVBoxLayout(self)
        main_layout.addStretch(1)
        main_layout.addWidget(welcome_label, alignment=Qt.AlignCenter)
        main_layout.addStretch(1)

        # Создание горизонтального макета для кнопок
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(student_button)
        button_layout.addStretch(1)
        button_layout.addWidget(teacher_button)
        button_layout.addStretch(1)

        # Добавление горизонтального макета в главный макет
        main_layout.addLayout(button_layout)

        # Установка шрифта для метки и кнопок
        font = QFont()
        font.setPointSize(18)
        welcome_label.setFont(font)
        student_button.setFont(font)
        teacher_button.setFont(font)

        # Установка размеров окна
        self.resize(300, 400)
        self.setWindowTitle("Добро пожаловать")
        self.show()

        # Добавление обработчика событий для кнопки "Я Студент"
        student_button.clicked.connect(self.show_student_login_window)

        teacher_button.clicked.connect(self.show_teacher_login_window)

    def show_student_login_window(self):
        # Создание нового окна входа для студента
        student_login_window = StudentLoginWindow()
        student_login_window.exec_()
    
    def show_teacher_login_window(self):
        # Создание нового окна входа для студента
        teacher_login_window = TeacherLoginWindow()
        teacher_login_window.exec_()

class TeacherLoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Создание метки с заголовком окна
        title_label = QLabel("Вход для студента", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Создание поля ввода для логина и пароля
        group_label = QLabel("Группа:", self)
        self.group_combo = QComboBox(self)
        self.group_combo.addItem("ИУ5-12")
        self.group_combo.addItem("ИУ5-22")
        self.group_combo.addItem("ИУ5-32")
        self.group_combo.addItem("ИТ-22")

        login_label = QLabel("Логин:", self)
        self.login_input = QLineEdit(self)

        password_label = QLabel("Пароль:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        # Создание кнопок "Войти" и "Отмена"
        login_button = QPushButton("Войти", self)
        login_button.setStyleSheet("background-color: #3CB371; color: white; height: 30px; width: 120px; border-radius: 20px; font-size: 10px;")

        cancel_button = QPushButton("Отмена", self)
        cancel_button.setStyleSheet("background-color: #CD5C5C; color: white; height: 30px; width: 120px; border-radius: 20px; font-size: 10px;")

        # Создание главного вертикального макета
        main_layout = QVBoxLayout(self)
        main_layout.addStretch(1)
        main_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        main_layout.addStretch(1)

        # Создание макета для поля ввода группы
        group_layout = QHBoxLayout()
        group_layout.addWidget(group_label)
        group_layout.addWidget(self.group_combo)
        main_layout.addLayout(group_layout)

        # Создание макета для поля ввода логина
        login_layout = QHBoxLayout()
        login_layout.addWidget(login_label)
        login_layout.addWidget(self.login_input)
        main_layout.addLayout(login_layout)

        # Создание макета для поля ввода пароля
        password_layout = QHBoxLayout()
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        main_layout.addLayout(password_layout)

        # Создание макета для кнопок
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(login_button)
        button_layout.addWidget(cancel_button)
        button_layout.addStretch(1)
        main_layout.addLayout(button_layout)

        # Установка размеров окна
        self.resize(300, 200)
        self.setWindowTitle("Вход для студента")
        self.show()

        # Добавление обработчиков событий для кнопок
        login_button.clicked.connect(self.student_login)
        cancel_button.clicked.connect(self.close)

    def student_login(self):
        # Получение введенных значений из полей ввода
        group = self.group_combo.currentText()
        login = self.login_input.text()
        password = self.password_input.text()

        # TODO: Здесь должна быть проверка введенных данных и переход на другое окно, если логин и пароль верны
        print(f"Group: {group}, Login: {login}, Password: {password}")


class StudentLoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Создание метки с заголовком окна
        title_label = QLabel("Вход для студента", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Создание поля ввода для логина и пароля
        group_label = QLabel("Группа:", self)
        self.group_combo = QComboBox(self)
        self.group_combo.addItem("ИУ5-12")
        self.group_combo.addItem("ИУ5-22")
        self.group_combo.addItem("ИУ5-32")
        self.group_combo.addItem("ИТ-22")

        login_label = QLabel("Логин:", self)
        self.login_input = QLineEdit(self)

        password_label = QLabel("Пароль:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        # Создание кнопок "Войти" и "Отмена"
        login_button = QPushButton("Войти", self)
        login_button.setStyleSheet("background-color: #3CB371; color: white; height: 30px; width: 120px; border-radius: 20px; font-size: 10px;")

        cancel_button = QPushButton("Отмена", self)
        cancel_button.setStyleSheet("background-color: #CD5C5C; color: white; height: 30px; width: 120px; border-radius: 20px; font-size: 10px;")

        # Создание главного вертикального макета
        main_layout = QVBoxLayout(self)
        main_layout.addStretch(1)
        main_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        main_layout.addStretch(1)

        # Создание макета для поля ввода группы
        group_layout = QHBoxLayout()
        group_layout.addWidget(group_label)
        group_layout.addWidget(self.group_combo)
        main_layout.addLayout(group_layout)

        # Создание макета для поля ввода логина
        login_layout = QHBoxLayout()
        login_layout.addWidget(login_label)
        login_layout.addWidget(self.login_input)
        main_layout.addLayout(login_layout)

        # Создание макета для поля ввода пароля
        password_layout = QHBoxLayout()
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        main_layout.addLayout(password_layout)

        # Создание макета для кнопок
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(login_button)
        button_layout.addWidget(cancel_button)
        button_layout.addStretch(1)
        main_layout.addLayout(button_layout)

        # Установка размеров окна
        self.resize(300, 200)
        self.setWindowTitle("Вход для студента")
        self.show()

        # Добавление обработчиков событий для кнопок
        login_button.clicked.connect(self.student_login)
        cancel_button.clicked.connect(self.close)

    def student_login(self):
        # Получение введенных значений из полей ввода
        group = self.group_combo.currentText()
        login = self.login_input.text()
        password = self.password_input.text()

        # TODO: Здесь должна быть проверка введенных данных и переход на другое окно, если логин и пароль верны
        print(f"Group: {group}, Login: {login}, Password: {password}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WelcomeWindow() 
    window.show()
    sys.exit(app.exec_())
