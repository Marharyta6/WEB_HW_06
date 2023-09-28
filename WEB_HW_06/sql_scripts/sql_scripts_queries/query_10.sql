SELECT d.name AS discipline, s.fullname AS student, t.fullname AS teacher
FROM grades g 
LEFT JOIN disciplines d ON d.id  = g.disciplines_id
LEFT JOIN students s  ON s.id = g.students_id
LEFT JOIN teachers t  ON t.id = d.teacher_id 
WHERE s.id = 23 AND t.id = 1
GROUP BY d.id  
;

