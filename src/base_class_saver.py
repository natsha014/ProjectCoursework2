from abc import ABC, abstractmethod


class Saver(ABC):
    """Абстрактный класс сохранения файлов"""

    @abstractmethod
    def save_vacancies(self, vacancies):
        """Абстрактный метод сохранения объектов"""
        pass
