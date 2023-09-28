SELECT d.name AS discipline, s.fullname AS student
FROM grades g 
LEFT JOIN disciplines d ON d.id  = g.disciplines_id
LEFT JOIN students s  ON s.id = g.students_id  
WHERE s.id = 23
GROUP BY d.id  
;

