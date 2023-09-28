SELECT d.name AS discipline, t.fullname AS teacher, ROUND(AVG(g.grades),2) AS average_grade
FROM grades g 
LEFT JOIN disciplines d ON d.id  = g.disciplines_id
LEFT JOIN teachers t  ON t.id = d.teacher_id 
WHERE t.id = 5
ORDER BY average_grade DESC  
;

