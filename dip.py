from abc import ABC, abstractmethod


# Абстракція для збереження даних
class DataStorage(ABC):
    @abstractmethod
    def save(self, data):
        pass


# Конкретна реалізація збереження у файл
class FileStorage(DataStorage):
    def save(self, data):
        print(f"Збережено у файл: {data}")


# Конкретна реалізація збереження у базу даних
class DatabaseStorage(DataStorage):
    def save(self, data):
        print(f"Збережено у базу даних: {data}")


# Клас User залежить від абстракції
class User:
    def __init__(self, user_id, name, storage: DataStorage):
        self.user_id = user_id
        self.name = name
        self.storage = storage  # Залежність від абстракції

    def save(self):
        self.storage.save(f"ID={self.user_id}, Ім'я={self.name}")


# Використання
file_storage = FileStorage()
db_storage = DatabaseStorage()

user1 = User(1, "Олег", file_storage)
user2 = User(2, "Анна", db_storage)

user1.save()  # Зберігає у файл
user2.save()  # Зберігає у базу даних