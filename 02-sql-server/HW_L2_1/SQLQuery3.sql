
-- 3) Bahman transactions for terminals that had >200K in Dey
SELECT *
FROM tb_transactions
WHERE TRANDATE BETWEEN '1401-11-01' AND '1401-11-30' -- Bahman 
-- AND AMOUNT > 0 -- (optional: exclude zero amounts)
AND TERMINALNO IN (
	SELECT TERMINALNO
	FROM tb_transactions
	WHERE TRANDATE BETWEEN '1401-10-01' AND '1401-10-30' -- Dey 
	AND  AMOUNT > 200000
)
ORDER BY TRANDATE