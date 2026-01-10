def filter_vacancies(vacancies, filter_words):
    """Фильтрация вакансий по ключевым словам в описании"""
    if not filter_words:
        return vacancies

    result = []
    for v in vacancies:
        # Проверяем описание (snippet), если оно есть
        description = (v.description or "").lower()
        if any(word.lower() in description for word in filter_words):
            result.append(v)
    return result


def get_vacancies_by_salary(vacancies, salary_range):
    """Фильтрация по диапазону зарплат (формат '100000 - 150000')"""
    if not salary_range or '-' not in salary_range:
        return vacancies

    try:
        range_min, range_max = map(int, salary_range.split('-'))
        return [
            v for v in vacancies
            if (v.salary_from >= range_min and (v.salary_to <= range_max or v.salary_to == 0))
        ]
    except ValueError:
        print("Некорректный формат диапазона зарплат. Используется полный список.")
        return vacancies


def sort_vacancies(vacancies):
    """Сортировка вакансий по зарплате (от большего к меньшему)"""
    return sorted(vacancies, key=lambda x: x.salary_from, reverse=True)


def get_top_vacancies(vacancies, top_n):
    """Возвращает N лучших вакансий"""
    return vacancies[:top_n]


def print_vacancies(vacancies):
    """Вывод вакансий пользователю"""
    if not vacancies:
        print("Вакансии по вашим критериям не найдены.")
        return

    for i, v in enumerate(vacancies, 1):
        salary = f"{v.salary_from} - {v.salary_to}" if v.salary_to else f"от {v.salary_from}"
        print(f"{i}. {v.title} | Зарплата: {salary} | Ссылка: {v.url}")
