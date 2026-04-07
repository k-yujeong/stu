SELECT DISTINCT d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
FROM developers d 
JOIN skillcodes s
ON (d.skill_code & s.code) != 0
WHERE s.category LIKE 'F%'
ORDER BY 1 ASC;