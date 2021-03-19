# simple using subquery.
SELECT customer_id, COUNT(*) as count_no_trans
FROM Visits V
WHERE V.visit_id NOT IN (
    SELECT visit_id
    FROM Transactions
)
GROUP BY customer_id;


# avoids subquery, quicker execution using left join.
SELECT customer_id, COUNT(*) as count_no_trans
FROM Visits V
         LEFT OUTER JOIN Transactions T
                         ON V.visit_id = T.visit_id
WHERE T.transaction_id IS NULL
GROUP BY V.customer_id;