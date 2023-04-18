from PyQt5 import QtWidgets

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Форма входа")
        layout = QtWidgets.QVBoxLayout()

        group_label = QtWidgets.QLabel("Выберите группу:")
        self.group_combobox = QtWidgets.QComboBox()
        self.group_combobox.addItems(["Группа 1", "Группа 2", "Группа 3"])
        layout.addWidget(group_label)
        layout.addWidget(self.group_combobox)

        last_name_label = QtWidgets.QLabel("Фамилия:")
        self.last_name_edit = QtWidgets.QLineEdit()
        layout.addWidget(last_name_label)
        layout.addWidget(self.last_name_edit)

        first_name_label = QtWidgets.QLabel("Имя:")
        self.first_name_edit = QtWidgets.QLineEdit()
        layout.addWidget(first_name_label)
        layout.addWidget(self.first_name_edit)

        button = QtWidgets.QPushButton("Продолжить")
        button.clicked.connect(self.login)
        layout.addWidget(button)

        self.setLayout(layout)

    def login(self):
        group = self.group_combobox.currentText()
        last_name = self.last_name_edit.text()
        first_name = self.first_name_edit.text()

        # здесь можно проверить данные, например, по базе данных
        print("Вход выполнен! Группа: {}, Фамилия: {}, Имя: {}".format(group, last_name, first_name))

        # закрываем текущее окно и открываем новое
        self.close()
        self.next_window = NextWindow()
        self.next_window.show()

class NextWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Другое окно")
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Вы в другом окне")
        layout.addWidget(label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    login_window = LoginWindow()
    login_window.show()
    app.exec_()










import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

from student import StudentForm
from teacher import TeacherForm

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        # Настройка формы
        self.setWindowTitle('My Form')
        self.setGeometry(100, 100, 600, 700)

        # Создание метки с текстом
        self.label = QLabel(self)
        self.label.setGeometry(150, 100, 300, 500)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('Hello World!')
        self.label.setFont(QFont('Arial', 24))
        self.label.setStyleSheet('color: black;')

        # Создание кнопки "Я студент"
        self.button1 = QPushButton('Я студент', self)
        self.button1.setGeometry(180, 650, 120, 40)
        self.button1.setStyleSheet('background-color: #009688; color: white; border-radius: 20px; font-size: 18px;')
        self.button1.clicked.connect(self.open_student_form)

        # Создание кнопки "Я преподаватель"
        self.button2 = QPushButton('Я преподаватель', self)
        self.button2.setGeometry(360, 650, 150, 40)
        self.button2.setStyleSheet('background-color: #FF5722; color: white; border-radius: 20px; font-size: 18px;')
        self.button2.clicked.connect(self.open_teacher_form)
   
    def open_student_form(self):
        self.student_form = StudentForm()
        self.student_form.show()
        QApplication.instance().exec_()

    def open_teacher_form(self):
        self.teacher_form = TeacherForm()
        self.teacher_form.show()
        QApplication.instance().exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_form = MyForm()
    my_form.show()
    sys.exit(app.exec_())
