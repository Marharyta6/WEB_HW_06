SELECT ROUND(AVG(g.grades),2) AS average_grade
FROM grades g 
ORDER BY average_grade DESC;