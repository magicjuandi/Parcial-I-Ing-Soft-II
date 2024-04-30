from abc import ABC
import Payment
import User
import Product

class ShoppingCart(ABC):

    def __init__(self):self.items = []

    def add(self, product, quantity=1):
        self.items.append({'product': product, 'quantity': quantity})

    def remove(self, product):
        self.items = [item for item in self.items if item['product'] != product]

    def checkout(self,product : Product):
        total_price = product.price
        return total_price
    
    
