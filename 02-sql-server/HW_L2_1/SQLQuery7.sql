-- 7) Esfand total amount for terminals completely inactive (no transactions) in Bahman
SELECT TERMINALNO, SUM(AMOUNT) AS TOTAL_AMOUNT
FROM tb_transactions
WHERE TRANDATE BETWEEN '1401-12-01' AND '1401-12-30' -- Esfand
AND TERMINALNO NOT IN (
	-- Exclude any terminal that had even a single transaction record in Bahman
	SELECT DISTINCT TERMINALNO
	FROM tb_transactions
	WHERE TRANDATE BETWEEN '1401-11-01' AND '1401-11-30' -- Bahman
	AND TERMINALNO IS NOT NULL
)
GROUP BY TERMINALNO
ORDER BY TOTAL_AMOUNT ASC;
