from src.models.user import User


class AuthService:
    def __init__(self):
        self.users = []

    # CREATE
    def create_user(self, name, email, password, role):
        user = User(name, email, password, role)
        self.users.append(user)

    # READ
    def get_users(self):
        return self.users

    # UPDATE
    def update_user(self, email, new_name):
        for user in self.users:
            if user.get_email() == email:
                user.set_name(new_name)

    # DELETE
    def delete_user(self, email):
        self.users = [u for u in self.users if u.get_email() != email]

    # LOGIN
    def login(self, email, password):
        for user in self.users:
            if user.get_email() == email and user.get_password() == password:
                return user
        return None
