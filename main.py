from src.class_hh_api import HeadHunterAPI
from src.class_vacancy import Vacancy
from src.json_class import JSONSaver
from src.utils import filter_vacancies
from src.utils import get_top_vacancies
from src.utils import get_vacancies_by_salary
from src.utils import print_vacancies
from src.utils import sort_vacancies


def main() -> None:
    # 1. Сбор данных
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    print(f"Загрузка вакансий по запросу '{search_query}'...")
    hh_api.load_vacancies(search_query)

    # 2. Преобразование в объекты
    vacancies_list = Vacancy.cast_to_object_list(hh_api.vacancies)

    # 3. Ввод критериев пользователем
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации (через пробел): ").split()
    salary_range = input("Введите диапазон зарплат (например, 50000-150000): ")

    # 4. Обработка
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # 5. Вывод и сохранение
    print("\nРезультаты поиска:")
    print_vacancies(top_vacancies)

    saver = JSONSaver("data/hh_vacancies.json")
    saver.save_vacancies(top_vacancies)


if __name__ == "__main__":
    main()
