import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QDialog, QLineEdit


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

        # Добавление обработчика событий для кнопки "Я Студент"
        student_button.clicked.connect(self.show_student_login_window)

    def show_student_login_window(self):
        # Создание нового окна входа для студента
        student_login_window = StudentLoginWindow()
        student_login_window.exec_()    


class StudentLoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Создание метки с заголовком окна
        title_label = QLabel("Вход для студента", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Создание поля ввода для логина и пароля
        username_label = QLabel("Логин:", self)
        self.username_edit = QLineEdit(self)
        password_label = QLabel("Пароль:", self)
        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.Password)
        login_button = QPushButton("Войти", self)
        login_button.clicked.connect(self.login)

        # Создание вертикального макета для размещения элементов окна
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        main_layout.addWidget(username_label)
        main_layout.addWidget(self.username_edit)
        main_layout.addWidget(password_label)
        main_layout.addWidget(self.password_edit)
        main_layout.addWidget(login_button)

        # Установка размеров окна
        self.resize(300, 200)
        self.setWindowTitle("Вход для студента")

    def login(self):
        # Обработчик события нажатия кнопки "Войти"
        # Здесь вы можете добавить свой код для проверки логина и пароля
        # Если логин и пароль верны, то можно закрыть окно входа для студента
        # self.accept()
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome_window = WelcomeWindow()
    sys.exit(app.exec_())

