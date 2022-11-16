#testing grounds

class cart():
    def __init__(self):
        self.stuff = []
    
    def add_to_cart(self):
        self.stuff().append[1] 
    
    def remove_from_cart(self):
        print(f'{self.stuff}')
        choice5 = int(input("how many items do you want to remove? "))
        for a in range(1, (choice5 + 1)):
            print(f'{self.stuff}')
            print("Removal number: ", a)
            i = int(input("Which item do you want to delete? Items are arranged from 0, 1, 2 and so on...  "))
            del self.stuff[i]
    
    def empty_cart(self):
        self.stuff = []

    def display_cart(self):
        print(f'{self.stuff}')

cart1 = cart()
cart1.add_to_cart()
cart1.display_cart()
