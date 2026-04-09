from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from src.services.auth_service import AuthService
from src.ui.admin_view import AdminView
from src.ui.user_view import UserView
from src.ui.security_view import SecurityView


class LoginView(QWidget):
    def __init__(self):
        super().__init__()

        self.auth = AuthService()

        # Usuarios de prueba
        self.auth.create_user("Romel", "romel@mail.com", "1234", "admin")
        self.auth.create_user("User", "user@mail.com", "1234", "user")
        self.auth.create_user("Seguridad", "seg@mail.com", "1234", "security")

        self.setWindowTitle("FitZone - Login")

        layout = QVBoxLayout()

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Correo")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Iniciar sesión")
        self.login_button.clicked.connect(self.login)

        self.message = QLabel("")

        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.message)

        self.setLayout(layout)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        user = self.auth.login(email, password)

        if user:
            role = user.get_role()

            if role == "admin":
                self.admin_view = AdminView(self.auth)
                self.admin_view.show()

            elif role == "user":
                self.user_view = UserView()
                self.user_view.show()

            elif role == "security":
                self.security_view = SecurityView()
                self.security_view.show()

            self.close()
        else:
            self.message.setText("❌ Error en login")
