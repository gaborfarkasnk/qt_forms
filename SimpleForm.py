from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout
import sys


#subclass QWidget to define our window
# 
class Myform(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration form")
        self.resize(800, 0)

# create layouts for our widgets
        main_layout = QVBoxLayout(self)

        name_layout= QHBoxLayout()
        main_layout.addLayout(name_layout)

        email_layout = QHBoxLayout()
        main_layout.addLayout(email_layout)

        address_layout = QHBoxLayout()
        main_layout.addLayout(address_layout)

# create visible widgets like labels, buttons, etc

        name_lbl = QLabel("Name:")
        name_field = QLineEdit()
        address_lbl = QLabel("Address:")
        address_field = QLineEdit()
        email_lbl = QLabel("e-mail:")
        email_field = QLineEdit()
        button = QPushButton("Save")

# add them to layouts
        name_layout.addWidget(name_lbl)
        name_layout.addWidget(name_field)
        address_layout.addWidget(address_lbl)
        address_layout.addWidget(address_field)
        email_layout.addWidget(email_lbl)
        email_layout.addWidget(email_field)
        main_layout.addWidget(button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Myform()
    win.show()
    app.exec()
