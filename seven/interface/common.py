from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

from student import StudentForm
from teacher import TeacherForm


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Установить заголовок и размеры формы
        self.setWindowTitle('My Form')
        self.setGeometry(50, 50, 400, 400)

        # Создать макет вертикального выравнивания
        layout = QVBoxLayout()

        # Добавить метку в макет
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('Hello World!')
        self.label.setFont(QFont('Arial', 10))
        self.label.setStyleSheet('color: black;')
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # Добавить кнопки в макет
        self.button1 = QPushButton('Я студент', self)
        self.button1.setStyleSheet('background-color: #1E90FF; color: white;')
        self.button1.clicked.connect(self.open_student_form)
        layout.addWidget(self.button1, alignment=Qt.AlignCenter)

        self.button2 = QPushButton('Я преподаватель', self)
        self.button2.setStyleSheet('background-color: #1E90FF; color: white;')
        self.button2.clicked.connect(self.open_teacher_form)
        layout.addWidget(self.button2, alignment=Qt.AlignCenter)

        # Установить макет для формы
        self.setLayout(layout)

    def open_student_form(self):
        self.student_form = StudentForm()
        self.student_form.show()

    def open_teacher_form(self):
        self.teacher_form = TeacherForm()
        self.teacher_form.show()


if __name__ == '__main__':
    app = QApplication([])
    form = MainForm()
    form.show()
    app.exec_()

















