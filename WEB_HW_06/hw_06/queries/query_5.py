import sqlite3


def execute_query_5(sql: str) -> list:
    with sqlite3.connect('homework6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT t.fullname AS teacher, d.name AS discipline
FROM grades g 
LEFT JOIN disciplines d ON g.disciplines_id  = d.id 
LEFT JOIN teachers t ON d.teacher_id = t.id 
WHERE t.id = 5
GROUP BY d.id
;
"""

if __name__== '__main__':
    try:
        print(execute_query_5(sql))
    except sqlite3.Error as error:
        print(error)

