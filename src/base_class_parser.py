from abc import ABC
from abc import abstractmethod


class ParserAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        """Абстрактный метод получения вакансий"""
        pass
