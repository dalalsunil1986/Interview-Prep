# use left join since we need to return travelers that went 0 distance. Simply get distance for each user_id with JOIN,
# then group by user_id and sum all distances in group.
SELECT name, IFNULL(SUM(distance), 0) as travelled_distance
FROM Users U
         LEFT JOIN Rides R
                   ON U.id = R.user_id
GROUP BY u.id
# break ties by name
ORDER BY travelled_distance DESC, name ASC;