import random
import csv
from datetime import datetime, timedelta

# Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Order class
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_order_total(self):
        return sum(product.price for product in self.products)

# Customer class
class Customer:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.orders = []

    def create_order(self, order_id):
        new_order = Order(order_id)
        self.orders.append(new_order)
        return new_order

# Store class
class Store:
    def __init__(self, store_id):
        self.store_id = store_id
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_all_orders(self):
        orders = []
        for customer in self.customers:
            for order in customer.orders:
                orders.append(order)
        return orders

# Corporation class
class Corporation:
    def __init__(self):
        self.stores = []

    def add_store(self, store):
        self.stores.append(store)

    def generate_sales_report(self, filename="sales_data.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time", "StoreID", "CustomerID", "OrderID", "Product Name", "Price"])

            for store in self.stores:
                for customer in store.customers:
                    for order in customer.orders:
                        order_time = datetime.now() - timedelta(days=random.randint(0, 365))
                        date_str = order_time.strftime('%Y-%m-%d')
                        time_str = order_time.strftime('%H:%M:%S')
                        for product in order.products:
                            writer.writerow([date_str, time_str, store.store_id, customer.customer_id, order.order_id, product.name, product.price])

# Helper functions to create sample data
def generate_sample_data():
    # Sample product list
    product_names = ["Laptop", "Headphones", "Keyboard", "Mouse", "Monitor"]
    products = [Product(name, random.uniform(50, 1000)) for name in product_names]

    # Create Corporation
    corp = Corporation()

    # Create 5 Stores
    for i in range(5):
        store = Store(store_id=f"Store_{i+1}")
        
        # Create 10 customers per store
        for j in range(10):
            customer = Customer(customer_id=f"Customer_{j+1}")
            
            # Create 5 orders per customer
            for k in range(5):
                order = customer.create_order(order_id=f"Order_{i+1}_{j+1}_{k+1}")
                
                # Add 3 random products per order
                for _ in range(3):
                    order.add_product(random.choice(products))
            
            store.add_customer(customer)
        
        corp.add_store(store)
    
    return corp

# Create sample data and generate report
corporation = generate_sample_data()
corporation.generate_sales_report("sales_data.csv")
