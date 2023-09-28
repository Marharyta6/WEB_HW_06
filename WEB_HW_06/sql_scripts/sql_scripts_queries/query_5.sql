SELECT t.fullname AS teacher, d.name AS discipline
FROM grades g 
LEFT JOIN disciplines d ON g.disciplines_id  = d.id 
LEFT JOIN teachers t ON d.teacher_id = t.id 
WHERE t.id = 5
GROUP BY d.id
;
