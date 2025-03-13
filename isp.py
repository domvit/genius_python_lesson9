from abc import ABC, abstractmethod


# Інтерфейс для друку
class Printable(ABC):
    @abstractmethod
    def print_document(self):
        pass


# Інтерфейс для сканування
class Scannable(ABC):
    @abstractmethod
    def scan_document(self):
        pass


# Інтерфейс для копіювання
class Copyable(ABC):
    @abstractmethod
    def copy_document(self):
        pass


# Клас Принтер
class Printer(Printable):
    def print_document(self):
        print("Принтер: Друкую документ...")


# Клас Сканер
class Scanner(Scannable):
    def scan_document(self):
        print("Сканер: Сканую документ...")


# Клас Багатофункціональний пристрій
class MultiFunctionDevice(Printable, Scannable, Copyable):
    def print_document(self):
        print("БФП: Друкую документ...")

    def scan_document(self):
        print("БФП: Сканую документ...")

    def copy_document(self):
        print("БФП: Копіюю документ...")


# Використання
printer = Printer()
scanner = Scanner()
mfd = MultiFunctionDevice()

printer.print_document()
scanner.scan_document()
mfd.print_document()
mfd.scan_document()
mfd.copy_document()