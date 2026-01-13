import json

from src.base_class_saver import Saver


class JSONSaver(Saver):
    """Класс работы с JSON"""

    def __init__(self, filename: str = "hh_vacancies.json") -> None:
        self.__filename = filename

    def save_vacancies(self, vacancies: list) -> None:
        """Принимает список объектов Vacancy и сохраняет их в JSON"""
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump([v.to_dict() for v in vacancies], f, ensure_ascii=False, indent=4)

    def search_by_keyword(self, keyword: str) -> list[dict]:
        """Поиск в сохраненном файле по ключевому слову в названии"""
        with open(self.__filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        return [v for v in data if keyword.lower() in v["title"].lower()]
