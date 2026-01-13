import pytest

from src.class_hh_api import HeadHunterAPI


# Имитируем объект ответа от requests
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


@pytest.fixture
def hh_api():
    """Создает экземпляр API для каждого теста"""
    return HeadHunterAPI()


def test_load_vacancies_success(hh_api, monkeypatch):
    """Тест успешной загрузки (имитируем, что данные есть только на первой странице)"""

    # Данные для первой страницы
    mock_data_page_1 = {
        "items": [
            {"name": "Python Developer", "salary": {"from": 100000}},
            {"name": "Django Developer", "salary": None},
        ]
    }
    # Данные для второй страницы (пусто), чтобы цикл while прервался
    mock_data_empty = {"items": []}

    # Счётчик вызовов
    calls = []

    def mock_get(*args, **kwargs):
        calls.append(1)
        # Если это первый вызов — даем данные, если второй и далее — пустой список
        if len(calls) == 1:
            return MockResponse(mock_data_page_1, 200)
        return MockResponse(mock_data_empty, 200)

    monkeypatch.setattr("requests.get", mock_get)

    hh_api.load_vacancies("Python")

    assert len(hh_api.vacancies) == 2
    assert hh_api.vacancies[0]["name"] == "Python Developer"
    assert hh_api.vacancies[1]["name"] == "Django Developer"


def test_load_vacancies_server_error(hh_api, monkeypatch):
    """Тест поведения при ошибке сервера (500)"""

    def mock_get(*args, **kwargs):
        return MockResponse({}, 500)

    monkeypatch.setattr("requests.get", mock_get)

    hh_api.load_vacancies("Python")

    assert hh_api.vacancies == []
