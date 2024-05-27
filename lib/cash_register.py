#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.transactions = []

    def add_item(self, title, price, qty = 1):
        self.total += price * qty
        self.items.extend([title] * qty)
        self.transactions.append((price, qty))

    # def apply_discount(self):

    # def void_last_transaction(self):
