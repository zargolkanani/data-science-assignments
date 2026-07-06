
-- 1) Transactions > 100K between 25 Dey and 24 Bahman (exclude NULL amounts)
SELECT *
FROM tb_transactions
WHERE AMOUNT IS NOT NULL
AND AMOUNT > 100000 
AND TRANDATE BETWEEN '1401-10-25' AND '1401-11-24' -- Date range: 25 Dey to 24 Bahman
ORDER BY TRANDATE
