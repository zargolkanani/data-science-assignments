
-- 4) Top 5 Esfand transactions (non-zero) for terminals in "آذربايجان شرقي"
SELECT TOP (5) *
FROM tb_transactions
WHERE AMOUNT != 0 -- Exclude zero amounts
AND TRANDATE BETWEEN '1401-12-01' AND '1401-12-30' --Esfand
AND TERMINALNO IN (
	SELECT TERMINAL_NO
	FROM tb_merchants
	WHERE PROVINCENAME LIKE 'آذربايجان شرقي' 
)
ORDER BY AMOUNT ASC