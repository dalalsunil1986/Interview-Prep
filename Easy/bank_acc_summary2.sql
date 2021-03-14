# group all transactions by acc, get balance and join on account, filter for balances above 10k per q. prompt.
SELECT name AS Name, T.BALANCE
FROM Users U
         JOIN (
    SELECT account, SUM(amount) as BALANCE
    FROM Transactions
    GROUP BY account
) T ON U.account = T.account
WHERE T.BALANCE > 10000;