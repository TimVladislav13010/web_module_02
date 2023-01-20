from abc import ABC, abstractmethod


class AddressBookInterface(ABC):
    @staticmethod
    @abstractmethod
    def show_contact(*args):
        """
        Абстрактний метод для виведення контактів на екран.
        """
        pass

    @staticmethod
    @abstractmethod
    def helps(*args):
        """
        Абстрактний метод для виведення інформації про доступні команди.
        """
        pass


class NoteInterface(ABC):
    @staticmethod
    @abstractmethod
    def show_notes(*args):
        """
        Абстрактний метод для виведення нотаток на екран.
        :param args:
        :return:
        """
        pass
