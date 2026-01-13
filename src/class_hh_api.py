import requests

from src.base_class_parser import ParserAPI


class HeadHunterAPI(ParserAPI):
    """Класс для работы с HeadHunter"""

    def __init__(self) -> None:
        self.__url: str = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params: dict = {"text": "", "page": 0, "per_page": 100}
        self.vacancies: list = []

    def load_vacancies(self, keyword: str) -> None:
        """Загрузка вакансий"""
        self.__params["text"] = keyword
        self.vacancies = []  # Очищаем список перед новым поиском
        self.__params["page"] = 0  # Сбрасываем счетчик страниц

        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)

            if response.status_code == 200:
                data = response.json()
                vacancies = data.get("items", [])
                if not vacancies:  # Если вакансии закончились раньше 20 страницы
                    break
                self.vacancies.extend(vacancies)
                self.__params["page"] += 1
            else:
                print(f"Ошибка при загрузке страницы {self.__params['page']}")
                break
