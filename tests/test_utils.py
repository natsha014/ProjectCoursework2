import pytest

from src.class_vacancy import Vacancy
from src.utils import filter_vacancies
from src.utils import get_top_vacancies
from src.utils import get_vacancies_by_salary
from src.utils import sort_vacancies


@pytest.fixture
def sample_vacancies():
    """Создает список тестовых вакансий с разными параметрами"""
    return [
        Vacancy("Python Dev", "http://1", 100000, 150000, "Разработка на Python и Django"),
        Vacancy("Java Dev", "http://2", 200000, 250000, "Опыт работы со Spring"),
        Vacancy("Frontend Dev", "http://3", 50000, 0, "Знание React и JavaScript"),
    ]


def test_filter_vacancies(sample_vacancies):
    """Тест фильтрации по ключевым словам в описании"""
    # Ищем вакансии, где в описании есть 'Django'
    filtered = filter_vacancies(sample_vacancies, ["Django"])
    assert len(filtered) == 1
    assert filtered[0].title == "Python Dev"

    # Ищем вакансии, где есть 'React' или 'Django'
    filtered_multi = filter_vacancies(sample_vacancies, ["Django", "React"])
    assert len(filtered_multi) == 2

    # Если слов нет, должен вернуться исходный список
    assert len(filter_vacancies(sample_vacancies, [])) == 3


def test_get_vacancies_by_salary(sample_vacancies):
    """Тест фильтрации по диапазону зарплат"""
    # Вакансии в диапазоне 80000 - 160000
    ranged = get_vacancies_by_salary(sample_vacancies, "80000-160000")
    assert len(ranged) == 1
    assert ranged[0].title == "Python Dev"

    # Проверка вакансии с salary_to = 0
    ranged_no_to = get_vacancies_by_salary(sample_vacancies, "40000-80000")
    assert any(v.title == "Frontend Dev" for v in ranged_no_to)

    # Некорректный формат строки
    assert len(get_vacancies_by_salary(sample_vacancies, "сто тыщ")) == 3


def test_sort_vacancies(sample_vacancies):
    """Тест сортировки (должна быть от большего к меньшему по salary_from)"""
    sorted_v = sort_vacancies(sample_vacancies)
    assert sorted_v[0].salary_from == 200000  # Java
    assert sorted_v[1].salary_from == 100000  # Python
    assert sorted_v[2].salary_from == 50000  # Frontend


def test_get_top_vacancies(sample_vacancies):
    """Тест получения топ N вакансий"""
    top_2 = get_top_vacancies(sample_vacancies, 2)
    assert len(top_2) == 2
    assert top_2[0].title == "Python Dev"
