SELECT c.login, COUNT(o.id) AS orders_in_delivery
FROM "Couriers" c
JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login
ORDER BY orders_in_delivery DESC;
