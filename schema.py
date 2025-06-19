"""
schema.py
Contains database schema definition used for prompting the LLM,
including both a natural language description and a structured list of tables and columns.
"""


SCHEMA_DEF = """
Database Schema Description:

Table: customers
- customer_id (INTEGER, PRIMARY KEY): Unique identifier for each customer.
- registration_date (DATE): The date when the customer registered.
- city (TEXT): City where the customer resides.
- gender (TEXT): Gender of the customer ('Male', 'Female', etc.)

Table: orders
- order_id (INTEGER, PRIMARY KEY): Unique order identifier.
- customer_id (INTEGER, FOREIGN KEY → customers.customer_id): ID of the customer who placed the order.
- order_date (DATE): Date on which the order was placed.
- total_amount (NUMERIC): Total amount of the order.
- status (TEXT): Status of the order ('Delivered', 'Cancelled', etc.)

Table: order_items
- item_id (INTEGER, PRIMARY KEY): Unique identifier for each item in an order.
- order_id (INTEGER, FOREIGN KEY → orders.order_id): The order to which this item belongs.
- product_name (TEXT): Name of the product purchased.
- quantity (INTEGER): Quantity of the product.
- unit_price (NUMERIC): Price per unit of the product.
"""

