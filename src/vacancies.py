
class Vacancies:

    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

        '''валидировать данные, которыми инициализируются его атрибуты.?????'''