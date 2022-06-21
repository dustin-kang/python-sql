-- 262. Trips and Users

SELECT
    Trips.Request_at AS Day
    ROUND(SUM(IF(status != 'complete', 1, 0)) / count(*), 2) AS 'Cancellation Rate'
FROM
    Trips, Users
WHERE
    Trips.Client_Id = Users.Users_id AND
    Users.Banned = "No" AND
    Trips.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY
    Trips.Request_at