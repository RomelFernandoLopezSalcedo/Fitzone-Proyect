from PySide6.QtWidgets import QApplication
from src.ui.login_view import LoginView
import sys

app = QApplication(sys.argv)

window = LoginView()
window.show()

sys.exit(app.exec())
