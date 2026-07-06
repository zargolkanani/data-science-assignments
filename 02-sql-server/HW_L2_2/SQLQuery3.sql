--3:
-- Compare total tran between Alborz and Khuzestan in Bahman 1401

SELECT 
	m.PROVINCENAME, --province name
	SUM(AMOUNT) AS TotalTransaction
FROM tb_transactions t
JOIN tb_merchants m
	ON t.TERMINALNO = m.TERMINAL_NO
WHERE (t.TRANDATE BETWEEN '1401-11-01' AND '1401-11-30' ) --date filter
	  AND m.PROVINCENAME IN ( N'البرز' , N'خوزستان') --selected provinces
GROUP BY m.PROVINCENAME

