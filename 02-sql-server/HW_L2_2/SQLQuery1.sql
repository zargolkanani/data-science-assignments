--1: 
-- Cities with avg tran amount higher than overall avg

SELECT 
	m.CITYNAME, --city name
	COUNT(*) AS TotalTransationCount, --number of tran
	AVG(t.AMOUNT) AS AvgTransaction --avg tran amount

FROM tb_transactions t
JOIN tb_merchants m
	ON t.TERMINALNO = m.TERMINAL_NO
GROUP BY m.CITYNAME
--compare city avg with total avg
HAVING AVG(AMOUNT) > (
	SELECT AVG(AMOUNT) 
	FROM tb_transactions
)
ORDER BY AvgTransaction DESC