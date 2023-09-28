import sqlite3


def execute_query_4(sql: str) -> list:
    with sqlite3.connect('homework6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(g.grades),2) AS average_grade
FROM grades g 
ORDER BY average_grade DESC;
"""

if __name__== '__main__':
    try:
        print(execute_query_4(sql))
    except sqlite3.Error as error:
        print(error)

