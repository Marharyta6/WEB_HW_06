import sqlite3


def execute_query_11(sql: str) -> list:
    with sqlite3.connect('homework6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.fullname AS student, t.fullname AS teacher, ROUND(AVG(g.grades),2) AS average_grade
FROM grades g 
LEFT JOIN disciplines d ON d.id  = g.disciplines_id
LEFT JOIN students s  ON s.id = g.students_id
LEFT JOIN teachers t  ON t.id = d.teacher_id 
WHERE s.id = 35 AND t.id = 1
GROUP BY t.id  
ORDER BY average_grade DESC
;
"""

if __name__== '__main__':
    try:
        print(execute_query_11(sql))
    except sqlite3.Error as error:
        print(error)

