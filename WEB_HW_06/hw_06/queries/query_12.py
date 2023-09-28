import sqlite3


def execute_query_12(sql: str) -> list:
    with sqlite3.connect('homework6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.fullname AS student, gr.name AS group_name, d.name AS discipline, g.grades AS grades, g.date_of AS last_date
FROM grades g 
LEFT JOIN disciplines d ON d.id  = g.disciplines_id
LEFT JOIN students s  ON s.id = g.students_id
LEFT JOIN teachers t  ON t.id = d.teacher_id
LEFT JOIN groups gr ON gr.id =s.group_id 
WHERE gr.id = 2 AND d.id = 3
AND last_date = (
	SELECT MAX(date_of)
	FROM grades g
	LEFT JOIN students s ON s.id = g.students_id 
	WHERE s.group_id = 2 AND g.disciplines_id = 3
)  
ORDER BY grades DESC
;
"""

if __name__== '__main__':
    try:
        print(execute_query_12(sql))
    except sqlite3.Error as error:
        print(error)

