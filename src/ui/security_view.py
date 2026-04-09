from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class SecurityView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Panel Seguridad")

        layout = QVBoxLayout()

        self.label = QLabel("Panel de monitoreo de accesos")

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.close)

        layout.addWidget(self.label)
        layout.addWidget(self.back_button)

        self.setLayout(layout)
