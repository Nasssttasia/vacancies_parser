# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.data import InfoToJson
from src.hh import GetInfoHH
from src.superjob import GetInfoSJ
from src.vacancies import Vacancies

hh_api = GetInfoHH()
# superjob_api = GetInfoSJ()

# Получение вакансий с разных платформ
hh_vacancies = hh_api.get_vacancies_api("Python")
hh_vacancies = hh_api.get_formated_data(hh_vacancies)
json_saver = InfoToJson("Python")
json_saver.add_vacancies(hh_vacancies)

while True:
    user_input = input('''
    1 - вывести все
    2- отсортировать по max зп
    exit выход ''')
    if user_input == '1':
        vacancies = json_saver.get_vacancies()
    if user_input == '2':
        vacancies = json_saver.sorted_vacancies()
    if user_input == 'exit':
        break
    for vacancy in vacancies:
        print(vacancy)

exit()
superjob_vacancies = superjob_api.get_vacancies_api("Python")

# Создание экземпляра класса для работы с вакансиями
vacancy = Vacancies("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
json_saver = InfoToJson()
json_saver.add_vacancies(vacancy)
json_saver.get_vacancies("100 000-150 000 руб.")
json_saver.del_vacancies(vacancy)

# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter", "SuperJob"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
 