from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class UserView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Panel Usuario")

        layout = QVBoxLayout()

        self.label = QLabel("Bienvenido Usuario")

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.close)

        layout.addWidget(self.label)
        layout.addWidget(self.back_button)

        self.setLayout(layout)
