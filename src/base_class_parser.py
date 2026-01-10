from abc import ABC, abstractmethod


class ParserAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def load_vacancies(self, keyword: str):
        """Абстрактный метод получения вакансий"""
        pass
