import sqlite3


def execute_query_2(sql: str) -> list:
    with sqlite3.connect('homework6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT d.name, s.fullname, ROUND(AVG(g.grades),2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.students_id
JOIN disciplines d ON d.id = g.disciplines_id
WHERE d.id = 5
GROUP BY s.fullname 
ORDER BY average_grade DESC 
LIMIT 1;
"""

if __name__== '__main__':
    try:
        print(execute_query_2(sql))
    except sqlite3.Error as error:
        print(error)

