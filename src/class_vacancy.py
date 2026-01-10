class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ('title', 'url', 'salary_from', 'salary_to', 'description')

    def __init__(self, title, url, salary_from, salary_to, description):
        self.title = title
        self.url = url
        self.salary_from = salary_from or 0
        self.salary_to = salary_to or 0
        self.description = description

    def to_dict(self):
        """Превращает объект в словарь для сохранения в JSON"""
        return {
            "title": self.title,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description
        }

    @classmethod
    def cast_to_object_list(cls, json_data):
        """Преобразует список данных из API в список объектов Vacancy"""
        vacancies = []
        for item in json_data:
            salary = item.get('salary')
            vacancies.append(cls(
                title=item.get('name'),
                url=item.get('alternate_url'),
                salary_from=salary.get('from') if salary else 0,
                salary_to=salary.get('to') if salary else 0,
                description=item.get('snippet', {}).get('responsibility')
            ))
        return vacancies
