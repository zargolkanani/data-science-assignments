--5:
-- Tran statistics for terminals in Dey 1401
 SELECT	
		m.TERMINAL_NO, --terminal num
		m.SHOPNAME, --shop name
		COUNT(t.TERMINALNO) AS TotalTransactions, --total tran
		SUM( --purchase tran (00)
			CASE 
				WHEN TRANTYPE = 0 THEN 1
				ELSE 0
			END
		) AS BuyTransaction,
		SUM( --balance inquiry tran (31)
			CASE 
				WHEN TRANTYPE = 31 THEN 1
				ELSE 0
			END
		) AS BalanceTransaction,
		SUM( --charge purchase tran (50)
			CASE
				WHEN TRANTYPE = 50 THEN 1
				ELSE 0
			END
		) AS ChargeTransaction,
		SUM(t.AMOUNT) AS TotalAmount --total AMOUNT
FROM tb_merchants m
LEFT JOIN tb_transactions t -- To show terminals even without tran
	ON t.TERMINALNO = m.TERMINAL_NO
WHERE t.TRANDATE BETWEEN '1401-10-01' AND '1401-10-30' --filter : Dey 1401
GROUP BY m.TERMINAL_NO, m.SHOPNAME
ORDER BY TotalAmount DESC

