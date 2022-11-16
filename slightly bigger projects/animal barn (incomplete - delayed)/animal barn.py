#farm business program 0.1
#by scein

#START

quantity = 17

class cosmetics():
    def __init__(self, name, price, stock1):
        self.name = name
        self.price = price 
        self.quantity = stock1

class animals():
    def __init__(self, type, cost, stock):
        self.type = type
        self.cost = cost
        self.stock = stock
    
    def __repr__(self):
        return "\n " + str(self.type) + "   Price: " +"$"+ str(self.cost) + "   Stock: " + str(self.stock) + "\n "
    
    def stock_shortage(self):
        if self.stock<quantity:
            return " We're short on " + (quantity - self.stock) + " cows!"
Animals = [ 
    animals("Cow  ", 1000, 10),
    animals("Horse", 1250, 16),
    animals("Sheep", 850, 20)
]

cow = animals[0]
horse = animals[1]
sheep = animals[2]

print("What would you like to do?")
while True:
    choice = input(" \n Shop for Animals [A]  \n Animal Cosmetics [B]  \n End Shopping [C] \n --> ")
    if choice in ['A', 'a']:
        break
    elif choice in ['B', 'b']:
        break
    elif choice in ['C', 'c']:
        break
    else: 
        print("\nError! Type a proper answer")

print(Animals)
animals("Horse", 1250, 16).stock_shortage