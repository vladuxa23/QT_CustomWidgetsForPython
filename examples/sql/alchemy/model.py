import json
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.elements import and_

from utils import get_person

engine = create_engine("sqlite:///example.db", echo=True, future=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Model = declarative_base(name='Model')
Model.query = db_session.query_property()


class User(Model):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True)
    name = Column('name', String(200))
    surname = Column('surname', String(200))
    login = Column('login', String(200))
    password = Column('password', String(200))
    email = Column('email', String(200))
    phone = Column('phone', String(200))
    register_time = Column('register_time', DateTime())

    def __init__(self, **params):
        self.name = params.get("name")
        self.surname = params.get("surname")
        self.login = params.get("login")
        self.password = params.get("password")
        self.email = params.get("email")
        self.phone = params.get("phone")
        self.register_time = params.get("register_time")

    def to_dict(self):
        return dict(name=self.name, surname=self.surname, login=self.login,
                    password=self.password, email=self.email, phone=self.phone,
                    register_time=self.register_time)

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, sort_keys=True, default=str)


def init_db() -> None:
    """
    Инициализация (создание БД)

    :return: None
    """

    Model.metadata.create_all(bind=engine)


def addUser() -> dict:
    """
    Добавление пользователя в БД

    :return: словарь с данными нового пользователя
    """

    user = User(**get_person())
    db_session.add(user)
    db_session.commit()

    return user.to_dict()


def getUser(name: str, surname: str) -> dict:
    """
    Получить данные о пользователе из БД

    :param name: имя пользователя
    :param surname: фамилия пользователя
    :return: словарь со всеми полями о пользователе
    """

    data = User.query.filter(and_(User.name == name, User.surname == surname))
    return data.one().to_dict()


def getUsers() -> list:
    """
    Получение всех пользователей из БД

    :return: список пользователей
    """

    return [x.to_dict() for x in User.query.all()]


def getNames() -> list:
    """
    Получение имен и фамилий пользователей

    :return:
    """

    data = [f"{x[0]} {x[1]}" for x in User.query.with_entities(User.name, User.surname).all()]
    return data


init_db()

if __name__ == '__main__':
    # print(getNames())
    print(getUser("Наина", "Сысоева"))
