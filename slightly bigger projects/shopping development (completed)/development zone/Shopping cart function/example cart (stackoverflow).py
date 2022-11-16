
class ShoppingCart:

    def __init__(self):
        self.data = {}
    
    def add(self):
        i = input("What would you like to add to your cart? ")
        self.data[i] = input("Quantity: ")

    def clear(self):
        if input("Clear your list? [y/n] ").lower().startswith("y"):
            self.data = {}
            print("Your list has been cleared.")
        else:
            print("Action abandoned.")

    def delete(self):
        print("Still working on that, use 'clear' for now please.")

    def menu_loop(self):
        while True:
            i = input(
                "Make your shopping list. "
                "Please type (Show/Add/Delete/Clear/Quit). "
            ).lower()
            if i == 's':
                cart.show()
            try:
                getattr(self, i)()
            except AttributeError:
                print(
                    'Oops! Something went wrong. '
                    'Please type "(Show/Add/Delete/Clear/Quit)"'
                )
    def show(self):
        print(f'{self.data}')

cart = ShoppingCart()
cart.add()
cart.menu_loop()