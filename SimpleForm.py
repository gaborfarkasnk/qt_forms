from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout
            ,QSlider,                   
                               )
import sys, json, os


#subclass QWidget to define our window
# 
class Myform(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration form")
        self.resize(800, 0)

# create layouts for our widgets
        main_layout = QVBoxLayout(self)

        button1_layout = QVBoxLayout(self)
        main_layout.addLayout(button1_layout)

        name_layout= QHBoxLayout()
        main_layout.addLayout(name_layout)

        email_layout = QHBoxLayout()
        main_layout.addLayout(email_layout)

        address_layout = QHBoxLayout()
        main_layout.addLayout(address_layout)

# create visible widgets like labels, buttons, etc

        name_lbl = QLabel("Name:")
        name_lbl.setMinimumWidth(120)
        self.name_field = QLineEdit()
        address_lbl = QLabel("Address:")
        address_lbl.setMinimumWidth(120)
        self.address_field = QLineEdit()
        email_lbl = QLabel("e-mail:")
        email_lbl.setMinimumWidth(120)
        self.email_field = QLineEdit()
        button1 = QPushButton("Save1")
        button_save = QPushButton("Save2")
        slider = QSlider()
        
# add them to layouts
        button1_layout.addWidget(button1)
        name_layout.addWidget(name_lbl)
        name_layout.addWidget(self.name_field)
        address_layout.addWidget(address_lbl)
        address_layout.addWidget(self.address_field)
        email_layout.addWidget(email_lbl)
        email_layout.addWidget(self.email_field)
        main_layout.addWidget(button_save)
        main_layout.addWidget(slider)
        
#connect signals
        button_save.clicked.connect( self.handle_button_clicked )

#try to load user data
        self.load_data()

    def load_data(self):
        if os.path.exists("user_data.json"):
            with open("user_data.json") as f:
                user_data = json.load(f)
                self.name_field.setText(user_data["name"])
                self.address_field.setText(user_data["address"])
                self.email_field.setText(user_data["email"])

#button click method
    def handle_button_clicked(self):
        #print(f"Name: {self.name_field.text()}")
        #print(f"address: {self.address_field.text()}")
        #print(f"email: {self.email_field.text()}")
        user_data = {
            "name": self.name_field.text(),
            "address": self.address_field.text(),
            "email": self.email_field.text(),
        }

        with open("used_data.json", "w") as f:
            json.dump(user_data, f)


#clear all field
        self.name_field.clear()
        self.address_field.clear()
        self.email_field.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Myform()
    win.show()
    app.exec()
