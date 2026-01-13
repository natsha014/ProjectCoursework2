import re
from typing import Any
from typing import Self


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("title", "url", "salary_from", "salary_to", "description")

    def __init__(self, title: Any, url: Any, salary_from: Any, salary_to: Any, description: Any) -> None:
        self.title = self.__valid_clean_str(title)
        self.url = self.__validate_url(url)
        self.salary_from = self.__validate_int(salary_from)
        self.salary_to = self.__validate_int(salary_to)
        self.description = self.__valid_clean_str(description)

    def __valid_clean_str(self, value: Any) -> str:
        """Проверяет, что строка не пустая и является строкой и чистит от тегов"""
        if not value or not isinstance(value, str):
            return "Нет данных"

        return re.sub(r"<.*?>", "", value)

    def __validate_int(self, value: Any) -> int:
        """Проверяет корректность числовых данных и пытается преобразовать их"""
        try:
            # Пытаемся превратить входное значение в число
            if value is not None:
                num = int(float(value))  # Сначала во float (на случай "200.0"), затем в int
                return num if num > 0 else 0
        except (ValueError, TypeError):
            # Если это не число (например, "abc" или None), возвращаем 0
            return 0
        return 0

    def __validate_url(self, url: Any) -> str:
        """Базовая проверка ссылки"""
        if isinstance(url, str) and url.startswith("http"):
            return url
        return "URL не указан"

    def __lt__(self, other: Self) -> bool:
        """Магический метод для сравнения вакансий по зарплате"""
        return self.salary_from < other.salary_from

    @classmethod
    def cast_to_object_list(cls, json_data: list[dict]) -> list[Self]:
        """Преобразует список данных из API в список объектов Vacancy"""
        vacancies = []
        for item in json_data:
            salary = item.get("salary")
            vacancies.append(
                cls(
                    title=item.get("name"),
                    url=item.get("alternate_url"),
                    salary_from=salary.get("from") if salary else 0,
                    salary_to=salary.get("to") if salary else 0,
                    description=item.get("snippet", {}).get("responsibility"),
                )
            )
        return vacancies

    def to_dict(self) -> dict[str, Any]:
        """Превращает объект в словарь для сохранения в JSON"""
        return {
            "title": self.title,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description,
        }
