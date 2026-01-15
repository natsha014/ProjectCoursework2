from src.class_vacancy import Vacancy


def test_vacancy_init():
    """Тест инициализации и очистки HTML-тегов"""
    v = Vacancy(
        title="<highlighttext>Python</highlighttext> Developer",
        url="hh.ru",
        salary_from=100000,
        salary_to="200000",
        description="Опыт в <b>Django</b>",
    )
    assert v.title == "Python Developer"
    assert v.description == "Опыт в Django"
    assert v.salary_to == 200000
    assert v.url == "URL не указан"


def test_vacancy_invalid_data():
    """Тест валидации некорректных данных"""
    v = Vacancy(None, 123, -500, "abc", [])
    assert v.title == "Нет данных"
    assert v.url == "URL не указан"
    assert v.salary_from == 0
    assert v.salary_to == 0
    assert v.description == "Нет данных"


def test_vacancy_comparison():
    """Тест магического метода __lt__ (сравнение по зарплате)"""
    v1 = Vacancy("Dev1", "http", 100, 0, "")
    v2 = Vacancy("Dev2", "http", 200, 0, "")

    assert v1 < v2
    assert v2 > v1
    assert not (v1 == v2)


def test_cast_to_object_list():
    """Тест преобразования списка словарей в список объектов"""
    data = [
        {
            "name": "Python",
            "alternate_url": "http://hh.ru",
            "salary": {"from": 50000, "to": 100000},
            "snippet": {"responsibility": "Писать код"},
        }
    ]
    vacancies = Vacancy.cast_to_object_list(data)
    assert len(vacancies) == 1
    assert isinstance(vacancies[0], Vacancy)
    assert vacancies[0].salary_from == 50000


def test_to_dict():
    """Тест преобразования объекта в словарь"""
    v = Vacancy("Python", "http", 50, 100, "Desc")
    d = v.to_dict()
    assert d["title"] == "Python"
    assert d["salary_from"] == 50
    assert isinstance(d, dict)
