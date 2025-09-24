-- 1. Flag high-value transactions (example threshold)
SELECT * FROM transactions WHERE amount > 100000;

-- 2. Customers with multiple accounts
SELECT user_id, COUNT(account_id) as cnt
FROM accounts
GROUP BY user_id
HAVING COUNT(account_id) > 1;

-- 3. Inactive accounts for > 1 year (MySQL syntax example)
SELECT account_id, last_transaction_date
FROM accounts
WHERE last_transaction_date < DATE_SUB(CURDATE(), INTERVAL 1 YEAR);
