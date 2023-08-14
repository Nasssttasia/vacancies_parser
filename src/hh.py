import json

from src.abc.abc_job_api import JobApi
from requests import get


class GetInfoHH(JobApi):
    _url = 'https://api.hh.ru/vacancies/'

    def __init__(self):
        pass

    def __str__(self):
        return 'HeadHunter.ru'

    def get_vacancies_api(self, **kwargs):
        params = {}
        for key, value in kwargs.items():
            params[key] = value

        response = get(self._url, params=params)

        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            return data_dict
        else:
            print(response.status_code)
            return None

