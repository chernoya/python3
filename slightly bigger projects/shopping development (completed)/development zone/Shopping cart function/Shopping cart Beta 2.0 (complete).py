
class shopping_cart():
    def __init__(self):
        self.item = []
        self.item_price = []
        
    def add_item(self):
        j = int(input("Which item to add? "))
        self.item.append(None)          #list_var[position 0 1 2. . .]
        self.item_price.append(None)    #list_var[position 0 1 2. . .]
        print("Added!")
    
    def show(self):
        print("Items: ", self.item)
        print("Price: ", self.item_price)
        self.current_total = sum(self.item_price)
        print("Estimated total: ", self.current_total)

    def remove(self):
        z = int(input("which ones to remove "))
        del self.item[None]         #item position 
        del self.item_price[None]   #item position
    
    def checkout(self):
        self.total_price = sum(self.item_price)
        print()
        print("=====================R E C E I P T========================")
        print("Item: ", self.item)
        print("Price: ", self.item_price)
        print("Subtotal: ", self.total_price)
        print("==========================================================")
        print()
        print("  THANK YOU FOR SHOPPING WITH US! PLEASE COME AGAIN SOON  ")
        print()
        print()

    def abandon(self):
        self.item = []
        self.item_price = []
        print("You abandoned your shopping. . .")



    
