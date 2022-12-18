import datetime
import os.path

from faker import Faker


def load_style(qss_style_name: str) -> str:
    """
    Чтение и загрузка стиля из файла qss

    :param qss_style_name: название файла qss
    :return: стиль
    """

    with open(os.path.join(os.path.dirname(__file__), "QSS", "style", qss_style_name), "r") as file:
        style = file.read()

    return style


def get_random_person_name(count: int = 20) -> list:
    """
    Получение случайного списка имён

    :param count: длина списка
    :return: список с именами
    """

    fake = Faker('ru_RU')

    return [fake.name() for _ in range(count)]


def get_random_address(count: int = 20) -> list:
    """
    Получение случайного списка адресов

    :param count: длина списка
    :return: список с именами
    """

    fake = Faker('ru_RU')

    return [fake.address() for _ in range(count)]


def get_person():
    fake = Faker('ru_RU')


    return {'name': fake.first_name(),
            'surname': fake.last_name(),
            'login': '@' + fake.user_name(),
            'password': fake.password(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'register_time': datetime.datetime.now()}


if __name__ == '__main__':
    print(get_person())
