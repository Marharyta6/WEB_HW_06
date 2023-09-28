SELECT s.fullname as student, g.grades AS grades, gr.name AS group_name, d.name AS discipline
FROM grades g 
LEFT JOIN disciplines d ON d.id  = g.disciplines_id
LEFT JOIN students s ON s.id = g.students_id 
LEFT JOIN groups gr ON gr.id = s.group_id 
WHERE gr.id = 3 AND d.id = 2
ORDER BY g.grades DESC  
;

