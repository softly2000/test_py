from PyQt5 import QtCore, QtGui, QtWidgets

class TeacherForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Определяем размеры формы
        self.setFixedSize(400, 550)

        # Создаем метку для текста
        self.label = QtWidgets.QLabel("Другой текст", self)
        self.label.setGeometry(0, 0, self.width(), self.height() - 60)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        # Создаем кнопку "Я студент"
        self.button_student = QtWidgets.QPushButton("Я студент", self)
        self.button_student.setGeometry(self.width() // 2 - 60, self.height() - 50, 120, 20)
        self.button_student.setStyleSheet("background-color: darkblue; color: white; font-weight: bold; font-size: 8px;")

        # Создаем кнопку "Я преподаватель"
        self.button_teacher = QtWidgets.QPushButton("Я преподаватель", self)
        self.button_teacher.setGeometry(self.width() // 2 - 60, self.height() - 25, 120, 20)
        self.button_teacher.setStyleSheet("background-color: darkblue; color: white; font-weight: bold; font-size: 8px;")

