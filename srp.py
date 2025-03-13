class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def create(self):
        """Створює користувача"""
        print(f"Створено користувача: ID={self.user_id}, Ім'я={self.name}, Email={self.email}")

    def update(self, name=None, email=None):
        """Оновлює дані користувача"""
        if name:
            self.name = name
        if email:
            self.email = email
        print(f"Оновлено: Ім'я={self.name}, Email={self.email}")

    def delete(self):
        """Видаляє користувача"""
        print(f"Видалено користувача з ID={self.user_id}")

# Використання
user = User(1, "Олег", "oleg@example.com")
user.create()
user.update(email="oleg.new@example.com")
user.delete()