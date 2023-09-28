import sqlite3


def execute_query_10(sql: str) -> list:
    with sqlite3.connect('homework6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT d.name AS discipline, s.fullname AS student, t.fullname AS teacher
FROM grades g 
LEFT JOIN disciplines d ON d.id  = g.disciplines_id
LEFT JOIN students s  ON s.id = g.students_id
LEFT JOIN teachers t  ON t.id = d.teacher_id 
WHERE s.id = 23 AND t.id = 1
GROUP BY d.id  
;
"""

if __name__== '__main__':
    try:
        print(execute_query_10(sql))
    except sqlite3.Error as error:
        print(error)

