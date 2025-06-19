RETRIEVED_CONTEXT = """
Examples:
- "Count new customers who joined last month." → 
  SELECT COUNT(*) FROM customers WHERE registration_date >= DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH), '%Y-%m-01') AND registration_date < DATE_FORMAT(CURDATE(), '%Y-%m-01');

- "What is the male to female customer ratio?" →
  SELECT COUNT(CASE WHEN gender = 'Male' THEN 1 END) / NULLIF(COUNT(CASE WHEN gender = 'Female' THEN 1 END), 0) AS male_female_ratio FROM customers;

- "Show total sales for each month in 2023." →
  SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(total_amount) AS total_sales FROM orders WHERE YEAR(order_date) = 2023 GROUP BY month ORDER BY month;

- "Find orders placed by customers in Mumbai." →
  SELECT o.* FROM orders o JOIN customers c ON o.customer_id = c.customer_id WHERE c.city = 'Mumbai';

- "Which products are most frequently purchased together?" →
  SELECT oi1.product_name AS product_1, oi2.product_name AS product_2, COUNT(*) AS frequency
  FROM order_items oi1
  JOIN order_items oi2 ON oi1.order_id = oi2.order_id AND oi1.product_name < oi2.product_name
  GROUP BY product_1, product_2
  ORDER BY frequency DESC
  LIMIT 10;

- "List total quantity sold for each product." →
  SELECT product_name, SUM(quantity) AS total_quantity FROM order_items GROUP BY product_name ORDER BY total_quantity DESC;

- "Get total sales last quarter." →
  SELECT SUM(total_amount) AS total_sales
  FROM orders
  WHERE QUARTER(order_date) = QUARTER(DATE_SUB(CURDATE(), INTERVAL 1 QUARTER)) 
    AND YEAR(order_date) = YEAR(DATE_SUB(CURDATE(), INTERVAL 1 QUARTER));
"""
