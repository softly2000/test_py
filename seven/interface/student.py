from PyQt5 import QtCore, QtGui, QtWidgets

class StudentForm(QtWidgets.QWidget):
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
"""
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    login_window = LoginWindow()
    login_window.show()
    app.exec_()"""
