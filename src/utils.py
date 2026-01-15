from src.class_vacancy import Vacancy


def filter_vacancies(vacancies: list, filter_words: list) -> list:
    """Фильтрация вакансий по ключевым словам в описании"""
    if not filter_words:
        return vacancies

    result = []
    for v in vacancies:
        description = (v.description or "").lower()
        if any(word.lower() in description for word in filter_words):
            result.append(v)
    return result


def get_vacancies_by_salary(vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
    """Фильтрация по диапазону зарплат (формат '100000 - 150000')"""
    if not salary_range or "-" not in salary_range:
        return vacancies

    try:
        range_min, range_max = map(int, salary_range.split("-"))
        return [
            v for v in vacancies if (v.salary_from >= range_min and (v.salary_to <= range_max or v.salary_to == 0))
        ]
    except ValueError:
        print("Некорректный формат диапазона зарплат. Используется полный список.")
        return vacancies


def sort_vacancies(vacancies: list) -> list:
    """
    Сортировка вакансий.
    Использует магический метод __lt__, определенный в классе Vacancy.
    """
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: list, top_n: int) -> list:
    """Возвращает N лучших вакансий"""
    return vacancies[:top_n]


def print_vacancies(vacancies: list) -> None:
    """Вывод вакансий пользователю"""
    if not vacancies:
        print("Вакансии по вашим критериям не найдены.")
        return

    for i, v in enumerate(vacancies, 1):
        salary = f"{v.salary_from} - {v.salary_to}" if v.salary_to else f"от {v.salary_from}"
        print(f"{i}. {v.title} | Зарплата: {salary} |\n Описание: {v.description} |\n Ссылка: {v.url}")
