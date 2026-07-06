
-- 7) Esfand total amount for terminals inactive in Bahman (amount = 0)
SELECT TERMINALNO, SUM(AMOUNT) AS TOTAL_AMOUNT
FROM tb_transactions
WHERE TRANDATE BETWEEN '1401-12-01' AND '1401-12-30' --Esfand
AND TERMINALNO IN (
	SELECT TERMINALNO
	FROM tb_transactions
	WHERE TRANDATE BETWEEN '1401-11-01' AND '1401-11-30' --Bahman
	AND AMOUNT = 0 --Inactive terminals
)
GROUP BY TERMINALNO
ORDER BY SUM(AMOUNT) ASC 
