SELECT s.fullname AS student, t.fullname AS teacher, ROUND(AVG(g.grades),2) AS average_grade
FROM grades g 
LEFT JOIN disciplines d ON d.id  = g.disciplines_id
LEFT JOIN students s  ON s.id = g.students_id
LEFT JOIN teachers t  ON t.id = d.teacher_id 
WHERE s.id = 35 AND t.id = 1
GROUP BY t.id  
ORDER BY average_grade DESC
;

