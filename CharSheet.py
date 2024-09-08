from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout
            ,QSlider, QGroupBox                  
                               )
import sys, json, os
from char_sheet_lib.PlayerAttributes import PlayerAttributes
from char_sheet_lib.PlayerDetails import PlayerDetails
from char_sheet_lib.Proficiencies import Proficiencies


class CharSheet(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("D&D Character Sheet")
        self.showMaximized()

        main_layout = QVBoxLayout(self)
       
        player_details = PlayerDetails()
        main_layout.addWidget(player_details)

        h_layout = QHBoxLayout()
        main_layout.addLayout(h_layout)

        player_attributes = PlayerAttributes()
        h_layout.addWidget(player_attributes)

        proficiencies = Proficiencies()
        h_layout.addWidget(proficiencies)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CharSheet()
    win.show()
    app.exec()