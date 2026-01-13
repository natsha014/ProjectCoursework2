from abc import ABC
from abc import abstractmethod


class Saver(ABC):
    """Абстрактный класс сохранения файлов"""

    @abstractmethod
    def save_vacancies(self, vacancies: list) -> None:
        """Абстрактный метод сохранения объектов"""
        pass
