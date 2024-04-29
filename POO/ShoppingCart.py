from abc import ABC


class ShoppingCart(ABC):

    def __init__(self):self.items = []

    def add(self, product, quantity=1):
        self.items.append({'product': product, 'quantity': quantity})

    def remove(self, product):
        self.items = [item for item in self.items if item['product'] != product]

    def checkout(self):
        total_price = sum(item['product'].price * item['quantity'] for item in self.items)
        return total_price