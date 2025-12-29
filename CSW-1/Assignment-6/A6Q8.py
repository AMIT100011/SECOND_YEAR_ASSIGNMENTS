class Product:
    # Class variable
    total_products_sold = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Instance method to sell product
    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            Product.total_products_sold += amount
            print(f"{amount} {self.name}(s) sold.")
        else:
            print("Not enough stock available.")

    # Class method to get total products sold
    @classmethod
    def get_total_products_sold(cls):
        return cls.total_products_sold


# Create Product objects
p1 = Product("Laptop", 50000, 10)
p2 = Product("Mouse", 500, 20)

# Sell products
p1.sell_product(3)
p2.sell_product(5)

# Display remaining quantity
print("Remaining Laptops:", p1.quantity)
print("Remaining Mice:", p2.quantity)

# Display total products sold
print("Total Products Sold:", Product.get_total_products_sold())
