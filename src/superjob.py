from src.abc.abc_job_api import JobApi


from requests import *
import json


class SuperJob(JobApi):
    """Класс, наследующийся от абстрактного класса,
    для работы с платформой SuperJob,
    и класса, для работы с файлом, содержащем вакансии superjob.ru"""

    __API_KEY = "v3.r.137703650.ac1aff3f3bfda03167f07eded22af755c6160e5e.65877cca7d7f0899800a132a5b5e96082aad9dfb"
    _api_link = "https://api.superjob.ru/2.0/vacancies"

    def __init__(self):
        pass
        # filename = "superjob.json"
        # super().__init__(filename)

    def __str__(self):
        return "superjob.ru"

    def get_vacancies_api(self, **kwargs):
        """
        :param kwargs:
        town - город ("Москва")
        keyword - Поисковый запрос
        count - Количество вакансий для вывода
        """
        params = {}
        headers = {
            'X-Api-App-Id': self.__API_KEY
        }

        for key, value in kwargs.items():
            params[key] = value

        response = get(self._api_link, headers=headers, params=params)
        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            return data_dict
        else:
            print("Ошибка при выполнении запроса.")
            return []

    def get_search_vacancies(self, search_data, n=10):
        return self.get_vacancies_api(keyword=search_data, count=n)

    def get_region_vacancies(self, region, n=10):
        return self.get_vacancies_api(town=region, count=n)

