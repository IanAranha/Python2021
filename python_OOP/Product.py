# The owner of a store wants a program to track products. Create a product class
# to fill the following requirements.
#
# Product Class:
# Attributes:
#
# Price
# Item Name
# Weight
# Brand
# Status: default "for sale"
# Methods:
#
# Sell: changes status to "sold"
#
# Add tax: takes tax as a decimal amount as a parameter and returns the price of
# the item including sales tax
#
# Return Item: takes reason_for_return as a parameter and changes status
# accordingly. If the item is being returned because it is defective, change
# status to "defective" and change price to 0. If it is being returned in the box,
# like new, mark it "for sale". If the box has been opened, set the status to
# "used" and apply a 20% discount.  (use "defective", "like_new", or "opened" as
# three possible value for reason_for_return).
#
# Display Info: show all product details.
#
# Every method that doesn't have to return something should return self so
# methods can be chained.

class Product:
    # Attributes:
    def __init__(self, price, item_name, quantity, brand):
        self.price = price
        self.item_name = item_name
        self.quantity = quantity
        self.brand = brand
        self.status = "for sale"
        self.tax_rate = 0.10
        self.total_price = self.add_tax(self.tax_rate)

    #Methods:
    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax_rate):
        self.total_price = self.price + (self.price * tax_rate)
        return self.total_price

    def return_item(self, reason_for_return):
        self.reason_for_return = reason_for_return
        if self.reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        elif self.reason_for_return == "like_new":
            self.status = "for sale"
        elif self.reason_for_return == "opened":
            self.status = "opened"
            self.price = self.price - (self.price * 0.2)
        return self

    def display_info(self):
        print(f"Brand: {self.brand} \nItem name: {self.item_name} \nQuantity: {self.quantity} \nPretax price: ${self.price} \nTotal Sales Price: ${self.total_price} \nStatus: {self.status}")
        return self

item1=Product(12.99, "Dryer Sheets", "240 count", "Bounce")

print("\nSale info:")
item1.display_info()
print("Item being returned:")
item1.return_item("defective")
item1.display_info()
