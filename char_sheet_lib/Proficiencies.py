from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class Proficiencies(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)
        label = QLabel("Player proficiencies section")
        main_layout.addWidget(label)