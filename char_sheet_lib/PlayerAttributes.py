from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class PlayerAttributes(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)
        label = QLabel("Player attributes section")
        main_layout.addWidget(label)