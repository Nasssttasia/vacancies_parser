import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class GetInfoAPI(ABC):

    @abstractmethod
    def get_info(self):
        pass


class GetInfoHH(GetInfoAPI):

    def get_info(self):
        url = 'https://api.hh.ru/vacancies/'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        return soup

"""
class GetInfoSJ(GetInfoAPI):

    def get_info(self):
        url = 'https://api.superjob.ru/2.0/vacancies/'
        # api_key =
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        return soup
"""
