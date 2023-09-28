import sqlite3


def drop_table_groups():
    with sqlite3.connect('homework6.db') as con:
        sql = """DROP TABLE IF EXISTS [groups];"""
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

def drop_table_students():
    with sqlite3.connect('homework6.db') as con:
        sql = """DROP TABLE IF EXISTS students;"""
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
def drop_table_teachers():
    with sqlite3.connect('homework6.db') as con:
        sql = """DROP TABLE IF EXISTS teachers;"""
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
def drop_table_disciplines():
    with sqlite3.connect('homework6.db') as con:
        sql = """DROP TABLE IF EXISTS disciplines;"""
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
def drop_table_grades():
    with sqlite3.connect('homework6.db') as con:
        sql = """DROP TABLE IF EXISTS grades;"""
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
def create_table_groups():
    with sqlite3.connect('homework6.db') as con:
        sql = """CREATE TABLE [groups] (
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     name STRING UNIQUE
);"""
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

def create_table_students():
    with sqlite3.connect('homework6.db') as con:
        sql = """CREATE TABLE students (
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     fullname STRING,
     group_id REFERENCES [groups] (id)
);"""
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
def create_table_teachers():
    with sqlite3.connect('homework6.db') as con:
        sql = """CREATE TABLE teachers (
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     fullname STRING
);"""
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
def create_table_disciplines():
    with sqlite3.connect('homework6.db') as con:
        sql = """CREATE TABLE disciplines (
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     name STRING UNIQUE,
     teacher_id REFERENCES teachers (id)
);"""
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

def create_table_grades():
    with sqlite3.connect('homework6.db') as con:
        sql = """CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    grades INTEGER, 
    disciplines_id REFERENCES disciplines (id),
    students_id REFERENCES students (id),
    date_of DATE
);"""
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

if __name__== '__main__':
    try:
        drop_table_groups()
        drop_table_students()
        drop_table_teachers()
        drop_table_disciplines()
        drop_table_grades()
        create_table_groups()
        create_table_students()
        create_table_teachers()
        create_table_disciplines()
        create_table_grades()
    except sqlite3.Error as error:
        print(error)

