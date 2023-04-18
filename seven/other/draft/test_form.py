import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # устанавливаем размеры окна и заголовок
        self.setGeometry(100, 100, 400, 700)
        self.setWindowTitle('Добро пожаловать')
        
        # создаем блок
        self.block = QWidget(self)
        self.block.setGeometry(0, 0, 400, 700)
        self.block.setStyleSheet('background-color: white; border: 1px solid black')
        
        # создаем текст "Добро пожаловать"
        self.label = QLabel('Добро пожаловать', self.block)
        #"""self.label.setAlignment(0x0082)"""
        self.label.setStyleSheet('font-size: 18px;')
        self.label.setGeometry(0, 50, 400, 50)
        
        # создаем кнопки "Я студент" и "Я преподаватель"
        self.student_button = QPushButton('Я студент', self.block)
        self.student_button.setStyleSheet('border-radius: 5px; width: 120px; height: 15px')
        self.student_button.setGeometry(140, 200, 120, 15)
       # self.student_button.clicked.connect(self.show_student_window)
        
        self.teacher_button = QPushButton('Я преподаватель', self.block)
        self.teacher_button.setStyleSheet('border-radius: 5px; width: 120px; height: 15px')
        self.teacher_button.setGeometry(140, 240, 120, 15)
        self.teacher_button.clicked.connect(self.show_teacher_window)
        
        # создаем вертикальный layout и добавляем в него кнопки
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.student_button)
        vbox.addWidget(self.teacher_button)
        vbox.addStretch(1)
        
        # создаем горизонтальный layout, добавляем в него вертикальный layout и устанавливаем его на блок
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        self.block.setLayout(hbox)
    
    def show_teacher_window(self):
        teacher_window = TeacherWindow()
        teacher_window.show()
        self.hide()
       



class TeacherWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем виджеты для формы
        self.label = QLabel('Добро пожаловать', self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button_login = QPushButton('Вход', self)
        self.button_register = QPushButton('Регистрация', self)
        self.label_login = QLabel('Вход для студентов', self)

        # Устанавливаем стиль для виджетов
        self.setStyleSheet("""
            QWidget {
                background-color: #CCCCCC;
            }
            QLabel {
                font-size: 24px;
            }
            QPushButton {
                width: 120px;
                height: 20px;
            }
            #label_login {
                font-size: 10px;
            }
        """)

        # Создаем горизонтальный слой для кнопок
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_login)
        button_layout.addWidget(self.button_register)

        # Создаем вертикальный слой для всех виджетов
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addWidget(self.label)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.label_login, alignment=QtCore.Qt.AlignCenter)
        main_layout.addStretch()

        # Устанавливаем слой для формы и задаем размеры
        self.setLayout(main_layout)
        self.setGeometry(100, 100, 400, 700)
        self.setWindowTitle('Моя форма')

    def show_teacher_window(self):
        teacher_window = TeacherWindow()
        teacher_window.show()
        self.hide()


   
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
