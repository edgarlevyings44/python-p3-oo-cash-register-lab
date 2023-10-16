#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.prices = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.quantity = quantity
        for i in range(self.quantity):
            self.prices.append(price)
            self.price = price 
            self.title = title
            self.total += price
            self.items.append(title)
            
        return self.items   
            

    def apply_discount(self):
        if self.discount > 0:
            self.total = (100 - self.discount) / 100 * self.total
            print("After the discount, the total comes to $800.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
       if self.items:
           last_price = self.prices.pop()
           self.total -= last_price
       else:
           self.total = 0.0

       return self.total   

cash_register = CashRegister()
cash_register.add_item("eggs", 0.80,2)
cash_register.add_item("milk", 1.20,3)
cash_register.apply_discount()

