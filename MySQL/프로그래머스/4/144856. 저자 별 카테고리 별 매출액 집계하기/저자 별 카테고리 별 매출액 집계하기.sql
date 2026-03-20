SELECT b.author_id, a.author_name, b.category, SUM(s.sales * b.price) as TOTAL_SALES
FROM book b
JOIN author a ON b.author_id = a.author_id
JOIN book_sales s ON b.book_id = s.book_id
WHERE s.sales_date >= '2022-01-01' AND s.sales_date < '2022-02-01'
GROUP BY b.author_id, a.author_name, b.category
ORDER BY 1 ASC, 3 DESC;