from sqlalchemy import create_engine, Column, Integer, String, Date, Sequence
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import text
from datetime import date, datetime
import json

# Читання конфігурації
with open('config.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']

# Підключення до БД
db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/itstep"
engine = create_engine(db_url)
Base = declarative_base()

# Модель таблиці People
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(20))
    surname = Column(String(20))
    city = Column(String(20))
    country = Column(String(20))
    date_dr = Column(Date)

    def __repr__(self):
        return (f"id = {self.id}, name = {self.name}, surname = {self.surname}, "
                f"city = {self.city}, country = {self.country}, date_dr = {self.date_dr}")

# Створення таблиці, якщо ще не існує
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Команда 1 — додати людину
def command1():
    print('1 - Додати нову людину')
    name = input("Ім'я: ")
    surname = input("Прізвище: ")
    city = input("Місто: ")
    country = input("Країна: ")
    date_str = input("Дата народження (РРРР-ММ-ДД): ")
    try:
        date_dr = datetime.strptime(date_str, '%Y-%m-%d').date()
        person = People(name=name, surname=surname, city=city, country=country, date_dr=date_dr)
        session.add(person)
        session.commit()
        print("Людину додано.")
    except ValueError:
        print("Неправильний формат дати.")

# Команда 2 — люди, ім’я яких починається на літеру
def command2():
    liter = input('Введіть першу літеру імені: ')
    query_sql = text("SELECT * FROM people WHERE name ILIKE :letter")
    result = session.execute(query_sql, {'letter': f'{liter}%'})
    for row in result.fetchall():
        print(row)

# Команда 3 — люди, що народились після певної дати
def command3():
    date_str = input('Введіть дату (РРРР-ММ-ДД): ')
    try:
        date_user = datetime.strptime(date_str, '%Y-%m-%d').date()
        query_sql = text("SELECT * FROM people WHERE date_dr > :date")
        result = session.execute(query_sql, {'date': date_user})
        for row in result.fetchall():
            print(row)
    except ValueError:
        print("Неправильний формат дати.")

# Команда 4 — кількість людей у країні
def command4():
    country_user = input('Введіть країну: ')
    query_sql = text("SELECT COUNT(*) FROM people WHERE country = :country")
    result = session.execute(query_sql, {'country': country_user})
    count = result.scalar()
    print(f"Кількість людей у країні {country_user}: {count}")

# Основний цикл
while True:
    print('''
1 - Додати нову людину
2 - Вивести людей, ім’я яких починається на певну літеру
3 - Вивести людей, які народились після певної дати
4 - Вивести скільки людей живе у певній країні
0 - Вихід
''')
    command = input('Введіть номер команди: ')
    if command == '1':
        command1()
    elif command == '2':
        command2()
    elif command == '3':
        command3()
    elif command == '4':
        command4()
    elif command == '0':
        break
    else:
        print("Невірна команда. Спробуйте ще.")
