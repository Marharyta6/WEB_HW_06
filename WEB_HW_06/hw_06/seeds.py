from datetime import datetime, date, timedelta
from faker import Faker

from random import randint
import sqlite3


disciplines = ["Вища математика",
               "Теорія ймовірності",
               "Ділова українська мова",
               "Історія України",
               "Програмування",
               "Філософія",
               "Англійська мова",
               "ООП"
            ]
groups = ["Ф2","ОП3","ЕП3","ТТ2","АТ2"]
NUMBER_TEACHERS = 6
NUMBER_STUDENT = 50

fake = Faker()

connect = sqlite3.connect("homework6.db")
cur = connect.cursor()

def seed_teachers():
    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers(fullname) VALUES (?);"
    cur.executemany(sql, zip(teachers,))

def seed_groups():
    sql = "INSERT INTO groups(name) VALUES (?);"
    cur.executemany(sql, zip(groups,))

def seed_disciplines():
    sql = "INSERT INTO disciplines(name, teacher_id) VALUES (?, ?);"
    cur.executemany(sql, zip(disciplines, iter(randint(1, NUMBER_TEACHERS) for _ in range(len(disciplines)))))

def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENT)]
    sql = "INSERT INTO students(fullname, group_id) VALUES (?, ?);"
    cur.executemany(sql, zip(students, iter(randint(1, len(groups)) for _ in range(len(students)))))

def seed_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-15", "%Y-%m-%d")
    sql = "INSERT INTO grades(disciplines_id, students_id, grades, date_of) VALUES (?, ?, ?, ?);"

    def get_list_date(start: date, end: date):
        result = []
        current_date = start
        while current_date <= end:
            if current_date.isoweekday()<6:
                result.append(current_date)
            current_date += timedelta(1)
        return result
    list_dates = get_list_date(start_date, end_date)

    grades = []
    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_students = [randint(1,NUMBER_STUDENT) for _ in range(5)]
        for student in random_students:
            grades.append((random_discipline, student, randint(1, 12), day.date()))
    cur.executemany(sql, grades)


if __name__== '__main__':
    try:
        seed_teachers()
        seed_disciplines()
        seed_groups()
        seed_students()
        seed_grades()
        connect.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        connect.close()

   