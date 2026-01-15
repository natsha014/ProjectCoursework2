import json
import os

import pytest

from src.class_vacancy import Vacancy
from src.json_class import JSONSaver  # Укажите ваш путь к файлу


@pytest.fixture
def temp_file(tmp_path):
    """Создает путь к временному файлу для тестов"""
    return str(tmp_path / "test_vacancies.json")


@pytest.fixture
def sample_vacancies():
    """Подготовка тестовых объектов Vacancy"""
    return [
        Vacancy("Python Developer", "hh.ru", 100000, 150000, "Описание 1"),
        Vacancy("Java Developer", "hh.ru", 200000, 250000, "Описание 2"),
    ]


def test_save_vacancies(temp_file, sample_vacancies):
    """Тест сохранения объектов в JSON-файл"""
    saver = JSONSaver(temp_file)
    saver.save_vacancies(sample_vacancies)

    # Проверяем, что файл действительно создался
    assert os.path.exists(temp_file)

    # Проверяем содержимое файла
    with open(temp_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 2
        assert data[0]["title"] == "Python Developer"
        assert data[0]["salary_from"] == 100000


def test_search_by_keyword(temp_file, sample_vacancies):
    """Тест поиска по ключевому слову в сохраненном файле"""
    saver = JSONSaver(temp_file)
    saver.save_vacancies(sample_vacancies)

    # Ищем вакансию со словом "Java"
    results = saver.search_by_keyword("Java")

    assert len(results) == 1
    assert results[0]["title"] == "Java Developer"

    # Ищем то, чего нет
    empty_results = saver.search_by_keyword("C++")
    assert len(empty_results) == 0


def test_search_in_empty_file(temp_file):
    """Тест поиска в пустом или несуществующем файле"""
    saver = JSONSaver(temp_file)

    with pytest.raises(FileNotFoundError):
        saver.search_by_keyword("Python")
