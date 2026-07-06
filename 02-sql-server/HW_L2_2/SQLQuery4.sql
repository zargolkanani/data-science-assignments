--4:
-- Calculate terminal fees for each month

 SELECT 
	TERMINALNO, --terminal num
	FORMAT(TRANDATE, 'yyyy-MM') AS TranMonth, --exteract year and month
	SUM ( --calculate total fee
		CASE
			WHEN TRANTYPE = 31 THEN 200 --balance inquiry
			WHEN TRANTYPE = 50 THEN 100 --charge purchase
			WHEN TRANTYPE = 0 --parchase less than 5000
				 AND AMOUNT < 5000 
				 THEN 25
			WHEN TRANTYPE = 0 AND --parchase BETWEEN 5000 AND 25000
				 AMOUNT BETWEEN 5000 AND 25000 
				 THEN (AMOUNT * 0.01)
			WHEN TRANTYPE = 0 --parchase more than 25000
				 AND AMOUNT > 25000 
				 THEN 260
			
			ELSE 0
		END
		) AS TotalFee
 FROM tb_transactions
 GROUP BY TERMINALNO,
		  FORMAT(TRANDATE, 'yyyy-MM')

 