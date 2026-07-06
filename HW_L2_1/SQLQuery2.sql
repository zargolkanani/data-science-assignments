
-- 2) Merchants with "تکمیل مدارک" status
SELECT SHOPNAME, PROVINCENAME, CITYNAME, TERMINAL_NO
FROM tb_merchants
WHERE WORKFLOWCAPTION = 'تکمیل مدارک'
