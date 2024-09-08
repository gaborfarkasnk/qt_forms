from PySide6.QtWidgets import QGroupBox, QLabel, QVBoxLayout

class PlayerAttributes(QGroupBox):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)
        self.setTitle("Player Attirubutes")
        self.setMaximumWidth(250)
