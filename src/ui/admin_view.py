from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit


class AdminView(QWidget):
    def __init__(self, auth):
        super().__init__()
        self.auth = auth

        self.setWindowTitle("Panel Admin - CRUD Usuarios")

        layout = QVBoxLayout()

        self.label = QLabel("👑 Panel Administrador")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nombre")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")

        self.role_input = QLineEdit()
        self.role_input.setPlaceholderText("Rol (admin/user/security)")

        self.create_button = QPushButton("Crear Usuario")
        self.create_button.clicked.connect(self.create_user)

        self.list_button = QPushButton("Listar Usuarios")
        self.list_button.clicked.connect(self.list_users)

        self.update_button = QPushButton("Actualizar Nombre")
        self.update_button.clicked.connect(self.update_user)

        self.delete_button = QPushButton("Eliminar Usuario")
        self.delete_button.clicked.connect(self.delete_user)

        self.result = QLabel("")

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.close)

        layout.addWidget(self.label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.role_input)

        layout.addWidget(self.create_button)
        layout.addWidget(self.list_button)
        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)

        layout.addWidget(self.result)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def create_user(self):
        name = self.name_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        role = self.role_input.text()

        self.auth.create_user(name, email, password, role)
        self.result.setText("✅ Usuario creado")

    def list_users(self):
        users = self.auth.get_users()
        text = "\n".join([f"{u.get_name()} - {u.get_email()} - {u.get_role()}" for u in users])
        self.result.setText(text)

    def update_user(self):
        email = self.email_input.text()
        new_name = self.name_input.text()

        self.auth.update_user(email, new_name)
        self.result.setText("✏ Usuario actualizado")

    def delete_user(self):
        email = self.email_input.text()

        self.auth.delete_user(email)
        self.result.setText("🗑 Usuario eliminado")
