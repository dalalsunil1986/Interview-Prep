# Write your MySQL query statement below

# we just need the information for each product id i.e., W, L, H to calculate volume and once we group by warehouse
# we simply want to calculate volume for each product_id and sum volume for each product_id within each group to get
# the total volume ALL products take up for each warehouse.
SELECT name AS warehouse_name, SUM(units * (Width * Length * Height)) as volume
FROM Warehouse W
         JOIN Products P
              ON W.product_id = P.product_id
GROUP BY name;