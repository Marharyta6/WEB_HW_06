import sqlite3


def execute_query_6(sql: str) -> list:
    with sqlite3.connect('homework6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.fullname AS student, g.name AS group_name
FROM students s  
LEFT JOIN groups g ON g.id  = s.group_id  
WHERE g.id = 3
GROUP BY s.fullname 
;
"""

if __name__== '__main__':
    try:
        print(execute_query_6(sql))
    except sqlite3.Error as error:
        print(error)

