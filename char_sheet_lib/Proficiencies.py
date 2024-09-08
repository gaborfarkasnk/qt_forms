from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QLabel

class Proficiencies(QGroupBox):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)
        self.setTitle("Proficiencies")
