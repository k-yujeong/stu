SELECT e3.id
FROM ecoli_data e3
JOIN ecoli_data e2 on e3.parent_id = e2.id
JOIN ecoli_data e1 on e2.parent_id = e1.id
WHERE e1.parent_id IS NULL
ORDER BY e3.id ASC;