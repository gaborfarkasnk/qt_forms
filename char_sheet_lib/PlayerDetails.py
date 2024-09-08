from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit

class PlayerDetails(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setTitle("Player Details")
        self.setMaximumHeight(100)


        main_layout = QHBoxLayout(self)

        self.player_name = QLineEdit()
        self.player_name.setPlaceholderText("Player Name")
        main_layout.addWidget(self.player_name)

        player_data_layout = QVBoxLayout()
        main_layout.addLayout(player_data_layout)

        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        player_data_layout.addLayout(h_layout1)
        player_data_layout.addLayout(h_layout2)

        self.race_field = QLineEdit()
        self.race_field.setPlaceholderText("Race")

        self.age_field = QLineEdit()
        self.age_field.setPlaceholderText("Age")

        h_layout1.addWidget(self.race_field)
        h_layout1.addWidget(self.age_field)

        self.background_field = QLineEdit()
        self.background_field.setPlaceholderText("Background")

        self.eyes_field = QLineEdit()
        self.eyes_field.setPlaceholderText("Eyes")

        h_layout2.addWidget(self.background_field)
        h_layout2.addWidget(self.eyes_field)
