--2:
--Inactive stores: stores with no tran or total tran amount = 0  
SELECT  
	m.TERMINAL_NO, --terminal num
	m.SHOPNAME --shop name
FROM tb_merchants m
LEFT JOIN tb_transactions t  -- To show terminals even without tran
	ON t.TERMINALNO = m.TERMINAL_NO
GROUP BY m.TERMINAL_NO, m.SHOPNAME
HAVING COUNT(t.AMOUNT) = 0 --no tran
	   OR
	   SUM (t.AMOUNT) = 0 --total amount is 0
ORDER BY m.TERMINAL_NO
