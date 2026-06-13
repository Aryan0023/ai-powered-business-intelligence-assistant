

-- Total Profit

SELECT
ROUND(SUM(profit), 2) AS total_profit
FROM superstore;





-- Top 10 Customers By Profit

SELECT
customer_name,
ROUND(SUM(profit), 2) AS profit
FROM superstore
GROUP BY customer_name
ORDER BY profit DESC
LIMIT 10;






-- Profit By Category

SELECT
category,
ROUND(SUM(profit), 2) AS profit
FROM superstore
GROUP BY category
ORDER BY profit DESC;






-- Profit By Region

SELECT
region,
ROUND(SUM(profit), 2) AS profit
FROM superstore
GROUP BY region
ORDER BY profit DESC;






-- Monthly Profit

SELECT
DATE_TRUNC('month', order_date) AS month,
ROUND(SUM(profit), 2) AS profit
FROM superstore
GROUP BY month
ORDER BY month;






-- Average Profit Per Order

SELECT
ROUND(
SUM(profit) /
COUNT(DISTINCT order_id),
2
) AS average_profit_per_order
FROM superstore;

-- Most Frequently Ordered Products

SELECT
product_name,
SUM(quantity) AS total_quantity
FROM superstore
GROUP BY product_name
ORDER BY total_quantity DESC
LIMIT 10;