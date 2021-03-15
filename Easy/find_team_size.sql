# Write your MySQL query statement below
SELECT employee_id, team_size
FROM Employee E
         JOIN (
    SELECT team_id, COUNT(*) AS team_size
    FROM Employee
    GROUP BY team_id
) E1
              ON E.team_id = E1.team_id;


# Using window function, we use aggregate function COUNT over a partition (basically group the table)
# by team_id and COUNT all tuples in each partition of the table based on partitioning over team_id
# to avoid an unnecessary join, since we can't select employee_id if we GROUP BY team_id.
SELECT employee_id, COUNT(employee_id) OVER (PARTITION BY team_id) as team_size
FROM Employee;
