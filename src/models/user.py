class User:
    def __init__(self, name, email, password, role):
        self._name = name
        self._email = email
        self._password = password
        self._role = role

    # GETTERS
    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_role(self):
        return self._role

    # SETTERS
    def set_name(self, name):
        self._name = name

    def set_password(self, password):
        self._password = password
