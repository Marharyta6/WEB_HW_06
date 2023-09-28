import sqlite3


def execute_query_3(sql: str) -> list:
    with sqlite3.connect('homework6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT d.name, gr.name, ROUND(AVG(g.grades),2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.students_id
JOIN disciplines d ON d.id = g.disciplines_id
JOIN [groups] gr ON gr.id = s.group_id 
WHERE d.id = 2
GROUP BY gr.name, d.name 
ORDER BY average_grade DESC;
"""

if __name__== '__main__':
    try:
        print(execute_query_3(sql))
    except sqlite3.Error as error:
        print(error)

