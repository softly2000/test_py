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
        self.show()

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

        # Создание выпадающего списка для выбора группы
        group_label = QLabel("Группа:", self)
        self.group_combo = QComboBox(self)
        self.group_combo.addItems(["Группа 1", "Группа 2", "Группа 3"])

        # Создание поля ввода для имени и фамилии
        name_label = QLabel("Фамилия и имя:", self)
        self.name_edit = QLineEdit(self)

        # Создание кнопки входа
        login_button = QPushButton("Войти", self)
        login_button.clicked.connect(self.login)

        # Создание вертикального макета для размещения элементов окна
        main_layout = QVBoxLayout(self)
        # Добавление элементов на окно
        main_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        main_layout.addWidget(group_label)
        main_layout.addWidget(self.group_combo)
        main_layout.addWidget(name_label)
        main_layout.addWidget(self.name_edit)
        main_layout.addWidget(login_button, alignment=Qt.AlignCenter)

        # Установка шрифта для меток и кнопки
        font = QFont()
        font.setPointSize(14)
        title_label.setFont(font)
        group_label.setFont(font)
        name_label.setFont(font)
        login_button.setFont(font)

        # Установка размеров окна
        self.resize(300, 200)
        self.setWindowTitle("Вход для студента")

    def login(self):
        # Получение выбранной группы и имени/фамилии из полей ввода
        group = self.group_combo.currentText()
        name = self.name_edit.text()

        # Вывод введенных данных в консоль
        print("Группа:", group)
        print("Фамилия и имя:", name)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec_())

        
   
