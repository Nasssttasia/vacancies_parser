
class Vacancies:

    def __init__(self, title, url, salary_from, salary_to, requirement):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement

    def __str__(self):
        return f'{self.title}, {self.salary_to}'


    def __lt__(self, other):
        return self.salary_from < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

        '''валидировать данные, которыми инициализируются его атрибуты.?????'''



'''  def attributes_from_data_sj(self):
        title = self.get_vacancies_api['objects'][0]['profession']
        url = self.get_vacancies_api['objects'][0]['link']
        salary_from = self.get_vacancies_api['objects'][0]['payment_from']
        salary_to = self.get_vacancies_api['objects'][0]['payment_to']
        requirement = self.get_vacancies_api['objects'][0]['candidat']
'''
