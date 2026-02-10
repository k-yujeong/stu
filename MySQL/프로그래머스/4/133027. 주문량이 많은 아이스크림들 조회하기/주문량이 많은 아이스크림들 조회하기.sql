SELECT f.flavor AS FLAVOR 
FROM first_half f
join (
    SELECT flavor, SUM(j.total_order) AS july_order
    FROM july j
    GROUP BY flavor
     )

j ON f.flavor = j.flavor
ORDER BY (f.TOTAL_ORDER + j.july_order) DESC
LIMIT 3;