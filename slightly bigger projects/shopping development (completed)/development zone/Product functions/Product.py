#Shopping something something
#ALPHA 1.5
#

import random as random

fragrances = ['Smells like daisies! ¯\_(ツ)_/¯', 'Smells like roses ლ(ಠ益ಠ)ლ', 'Smells like ice (▀̿Ĺ̯▀̿ ̿)', 'Smells like Lavenders ╮ (. ❛ ᴗ ❛.) ╭']

class product():
    def __init__(self, code, name, price, expiry):
        self.code = code 
        self.name = name 
        self.price = price
        self.expiry = expiry
    
    def check_for_expiry(self):
        print(f'The expiry date for {self.name} is {self.expiry}')

class shampoos(product):
    def smell_fragrance(self):
        print(f'{self.name} ' + random.choice(list(fragrances)))

class shopping_cart(product):
    def __init__(self):
        self.cart = []
    def add(self):
        self.cart.append[[self.name, self.price, self.expiry]]