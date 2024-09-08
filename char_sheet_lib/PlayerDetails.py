from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class PlayerDetails(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)
        label = QLabel("Player details section")
        main_layout.addWidget(label)