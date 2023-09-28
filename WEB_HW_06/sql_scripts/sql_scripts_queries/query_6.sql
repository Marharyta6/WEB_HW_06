SELECT s.fullname AS student, g.name AS group_name
FROM students s  
LEFT JOIN groups g ON g.id  = s.group_id  
WHERE g.id = 3
GROUP BY s.fullname 
;
