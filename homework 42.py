from sqlalchemy import create_engine, MetaData, insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import json

# Завантаження логіну та паролю з конфігураційного файлу
with open('config.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']

# Підключення до бази даних
db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/itstep2"
engine = create_engine(db_url)

metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


# Вибір таблиці
def get_table():
    print('Виберіть таблицю з бази:')
    for table_name in metadata.tables:
        print(f'\t{table_name}')
    return input('Ваша відповідь: ')


# Вставка рядка
def insert_row():
    table_name = get_table()
    table = metadata.tables[table_name]

    values = {}
    for column in table.columns:
        if column.name == 'id':
            continue
        value = input(f'{column.name} = ')
        values[column.name] = value

    try:
        session.execute(insert(table).values(values))
        session.commit()
        print("Рядок успішно додано.")
    except Exception as err:
        print(f"Помилка: {err}")


# Оновлення рядків
def update_row():
    table_name = get_table()
    table = metadata.tables[table_name]

    print("Введіть умову для оновлення (наприклад: id = 1):")
    condition = input("WHERE ")

    if not condition.strip():
        confirm = input("Ви справді хочете оновити УСІ рядки таблиці? (так/ні): ")
        if confirm.lower() != 'так':
            print("Операцію скасовано.")
            return

    updates = {}
    for column in table.columns:
        if column.name == 'id':
            continue
        value = input(f'Нове значення для {column.name} (або залиште порожнім): ')
        if value:
            updates[column.name] = value

    if not updates:
        print("Жодного значення не вказано для оновлення.")
        return

    set_clause = ", ".join([f"{col} = :{col}" for col in updates])
    query_str = f"UPDATE {table_name} SET {set_clause}"
    if condition.strip():
        query_str += f" WHERE {condition}"

    try:
        session.execute(text(query_str), updates)
        session.commit()
        print("Оновлення виконано.")
    except Exception as err:
        print(f"Помилка: {err}")


# Видалення рядків
def delete_rows():
    table_name = get_table()
    table = metadata.tables[table_name]

    print("Введіть умову для видалення (наприклад: id = 1):")
    condition = input("WHERE ")

    if not condition.strip():
        confirm = input("Ви справді хочете видалити УСІ рядки таблиці? (так/ні): ")
        if confirm.lower() != 'так':
            print("Операцію скасовано.")
            return

    query_str = f"DELETE FROM {table_name}"
    if condition.strip():
        query_str += f" WHERE {condition}"

    try:
        session.execute(text(query_str))
        session.commit()
        print("Видалення виконано.")
    except Exception as err:
        print(f"Помилка: {err}")


# Лікарі, які не у відпустці
def doctors_notvac():
    query = """
        SELECT DOCTORS.SURNAME, (DOCTORS.SALARY + DOCTORS.PREMIUM) AS ZP
        FROM DOCTORS
        JOIN Vacations ON Vacations.doctorid = DOCTORS.id 
        WHERE NOW() NOT BETWEEN Vacations.startdate AND Vacations.enddate
    """

    try:
        rows = session.execute(text(query)).fetchall()
        for row in rows:
            print(row)
    except Exception as err:
        print(f"Помилка: {err}")


# Показати відділення
def show_depart():
    query = "SELECT NAME FROM Departments"
    try:
        rows = session.execute(text(query)).fetchall()
        for row in rows:
            print(row)
    except Exception as err:
        print(f"Помилка: {err}")


# Палати у відділенні
def wards_depart():
    show_depart()
    depart_name = input("Введіть назву відділення: ")

    query = """
        SELECT WARDS.NAME
        FROM WARDS
        JOIN Departments ON Departments.id = WARDS.Departmentid
        WHERE Departments.NAME = :depart_name
    """

    try:
        rows = session.execute(text(query), {'depart_name': depart_name}).fetchall()
        for row in rows:
            print(row)
    except Exception as err:
        print(f"Помилка: {err}")


# Головне меню
while True:
    print("\nДії:")
    print("1 - Вставити рядок у таблицю")
    print("2 - Вивести прізвища та зарплати лікарів, які не у відпустці")
    print("3 - Вивести назви палат у певному відділенні")
    print("4 - Оновити рядки в таблиці")
    print("5 - Видалити рядки з таблиці")
    print("0 - Вихід")

    command = input('Введіть номер команди: ')

    if command == '1':
        insert_row()
    elif command == '2':
        doctors_notvac()
    elif command == '3':
        wards_depart()
    elif command == '4':
        update_row()
    elif command == '5':
        delete_rows()
    elif command == '0':
        print("Завершення роботи.")
        break
    else:
        print('Невірна команда')
