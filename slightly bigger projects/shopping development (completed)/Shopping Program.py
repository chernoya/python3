import time
import sys

#Aisles & Aisle products

aisles = ['Bakery [0]', 'Hygiene & Self-care [1]', 'Deserts & Candy [2]', 'Toys [3]', 'Furniture [4]']

bakery = ['Chocolate cake [0]', 'Strawberry cake [1]', 'Mango muffin [2]', 'Coffee bun [3]']    #0 - 3
bakery_price = [50, 45, 15, 4]

hygiene_selfcare = ['Shampoo [0]', 'Toothpaste [1]', 'Deodrant [2]']                            #0 - 2
hygiene_price = [12, 5, 10]

deserts_candy = ['Lollipop [0]', 'Mentos [1]', 'M&Ms [2]', 'Marshmellos [3]']                   #0 - 3
deserts_price = [1, 3, 4, 9]

toys = ['race cars [0]', 'train set [1]', 'legos [2]', 'airplane [3]', 'doll [4]']              #0 - 4
toys_price = [5, 12, 15, 20, 16]

furniture = ['Sofa [0]', 'Armchair [1]', 'bed [2]', 'coffee table [3]', 'desk [4]']             #0 - 4
furniture_price = [150, 90, 200, 120, 100]

end_dialogue = "Closing down mall. . . \n"
end_dialogue2 = "Counting profits. . . . . \n"
end_dialogue3 = "Shutting down app . . . \n"
end_dialoge4 = "Done! \n"

#Classes and methods of shopping

class shopping_cart():
    def __init__(self):
        self.item = []
        self.item_price = []
        
    def add_item(self):
        self.item.append(j[i])          #list_var[position 0 1 2. . .]
        self.item_price.append(k[i])    #list_var[position 0 1 2. . .]
        print("Added To Cart!")
    
    def show(self):
        print("Items: ", self.item)
        print("Price: ", self.item_price)
        self.current_total = sum(self.item_price)
        print("Estimated total: ", self.current_total)

    def remove(self):
        del self.item[z]         #item position 
        del self.item_price[z]   #item position
    
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

class end():
    def end_speech(self):
        for l in end_dialogue:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.1)
        for m in end_dialogue2:
            sys.stdout.write(m)
            sys.stdout.flush()
            time.sleep(0.1)
        for n in end_dialogue3:
            sys.stdout.write(n)
            sys.stdout.flush()
            time.sleep(0.1)
        for o in end_dialoge4:
            sys.stdout.write(o)
            sys.stdout.flush()
            time.sleep(0.1)


continue_shopping = True
remove_items = True 
cart = shopping_cart()
ending = end()

#START

print("==================================== W E L C O M E ========================================")


while continue_shopping==True:
    print()
    print("==================================== A I S L E S ========================================")
    print(aisles)                
    print()                                                                       #AISLES 
    input1 = int(input("Choose Aisle [0, 1, 2. .] or Stop Shopping [5]? "))
    print()
    
    if input1==0:
        continue_aisle = True
        while continue_aisle==True:
            j = bakery
            k = bakery_price
            ("==================================== B A K E R Y ========================================")
            print(bakery)
            print()                                                                 #BAKERY
            input2 = input("Buy From This Aisle? y/n ")
            print()
            if input2=='y':
                i = int(input("Which Item [0, 1, 2. . .] or None [4] "))
                print()
                if i==4:
                    continue_aisle = False
                elif i==1 or 2 or 3:
                    cart.add_item() #
                    print()
                    input4 = (input("Are You Done Buying From This Aisle? y/n "))
                    print()
                    if input4=='y':
                        print()
                        continue_aisle = False
                    elif input4=='n':
                        print()
                    else: 
                        print("Incorrect Input")
                        print()
                else:
                    print("Incorrect Input")
                    print()
            elif input2=='n':
                continue_aisle = False     
            else: 
                print("Incorrect Input")
                print()
    
    elif input1==1:
        continue_aisle = True
        while continue_aisle==True:
            j = hygiene_selfcare
            k = hygiene_price
            ("==================================== H Y G I E N E ========================================")
            print(hygiene_selfcare)  
            print()                                                         #HYGIENE 
            input2 = input("Buy From This Aisle? y/n ")
            print()
            if input2=='y':
                i = int(input("Which Item [0, 1, 2. . .] or None [4] "))
                print()
                if i==4:
                    continue_aisle = False
                elif i==0 or 1 or 2:
                    cart.add_item() #
                    print()
                    input4 = (input("Are You Done Buying From This Aisle? y/n "))
                    print()
                    if input4=='y':
                        print()
                        continue_aisle = False
                    elif input4=='n':
                        print()
                    else: 
                        print("Incorrect Input")
                        print()
                else:
                    print("Incorrect Input")
                    print()
            elif input2=='n':
                continue_aisle = False     
            else: 
                print("Incorrect Input")
                print()
        
    elif input1==2:
        continue_aisle = True
        while continue_aisle==True:
            j = deserts_candy
            k = deserts_price
            ("==================================== C A N D Y ========================================")
            print(deserts_candy) 
            print()                                                          #DESERTS AND CANDY
            input2 = input("Buy From This Aisle? y/n ")
            print()
            if input2=='y':
                i = int(input("Which Item [0, 1, 2. . .] or None [4] "))
                print()
                if i==4:
                    continue_aisle = False
                elif i==0 or 1 or 2 or 3:
                    cart.add_item()
                    print() #
                    input4 = (input("Are You Done Buying From This Aisle? y/n "))
                    print()
                    if input4=='y':
                        print()
                        continue_aisle = False
                    elif input4=='n':
                        print()
                    else:
                        print("Incorrect Input")
                        print()
                else:
                    print("Incorrect Input")
                    print()
            elif input2=='n':
                continue_aisle = False     
            else: 
                print("Incorrect Input")
                print()

    elif input1==3:
        continue_aisle = True
        while continue_aisle==True:
            j = toys
            k = toys_price
            ("==================================== T O Y S ========================================")
            print(toys)      
            print()                                                     #TOYS
            input2 = input("Buy From This Aisle? y/n ")
            print()
            if input2=='y':
                i = int(input("Which Item [0, 1, 2. . .] or None [5] "))
                print()
                if i==5:
                    continue_aisle = False
                elif i==0 or 1 or 2 or 3 or 4:
                    cart.add_item()
                    print() #
                    input4 = (input("Are You Done Buying From This Aisle? y/n "))
                    print()
                    if input4=='y':
                        print()
                        continue_aisle = False
                    elif input4=='n':
                        print()
                    else: 
                        print("Incorrect Input")
                        print()
                else:
                    print("Incorrect Input")
                    print()
            elif input2=='n':
                continue_aisle = False     
            else: 
                print("Incorrect Input")
                print()
    
    elif input1==4:
        continue_aisle = True
        while continue_aisle==True:
            j = furniture
            k = furniture_price
            ("==================================== F U R N I T U R E ========================================")
            print(furniture)      
            print()                                                     #Furniture
            input2 = input("Buy From This Aisle? y/n ")
            print()
            if input2=='y':
                i = int(input("Which Item [0, 1, 2. . .] or None [5] "))
                print()
                if i==5:
                    continue_aisle = False
                elif i==0 or 1 or 2 or 3 or 4:
                    cart.add_item()
                    print() #
                    input4 = (input("Are You Done Buying From This Aisle? y/n "))
                    print()
                    if input4=='y':
                        print()
                        continue_aisle = False
                    elif input4=='n':
                        print()
                    else:
                        print("Incorrect Input")
                        print()
                else:
                    print("Incorrect Input")
                    print()
            elif input2=='n':
                continue_aisle = False     
            else: 
                print("Incorrect Input")
                print()
    
    elif input1==5: 
        continue_shopping = False
        ("============================================================================")
        input5 = int(input("Review Cart [1] or Proceed To Checkout [2]? "))
        print()
        if input5==1:
            cart.show() 
            print() #              
            input6 = int(input("Remove Items From Cart [1] or Proceed To Checkout [2]? "))
            print()
            if input6==1:
                while remove_items==True: 
                    number_of_items = int(input("How many items would you like to remove?: "))
                    print()
                    for x in range(0, (number_of_items)):
                        cart.show()
                        print() #
                        z = int(input("Removal No " + str((x + 1)) +":" + " Enter their positional number from 0, 1, 2. . .: "))
                        print()
                        cart.remove()
                        print() #
                        cart.show()
                        print() #
                    
                    input7 = int(input("Remove items from cart [1] or Checkout [2]? "))
                    print()
                    if input7==1:
                        print("Alright")
                        print()
                    elif input7==2:
                        remove_items = False
                        cart.show()
                        print() #
                        input10 = int(input("Buy [1] or Abandon Shopping [2]? "))
                        print()
                        if input10==1:
                            cart.checkout()
                            print() #
                            break
                        elif input10==2:
                            cart.abandon()
                            print() #
                            break
                        else: 
                            print("Incorrect Input")
                            print()
                    else: 
                        print("Incorrect Input")
                        print()
            elif input6==2:
                cart.show()
                print() #
                input9 = int(input("Buy [1] or Abandon Shopping [2]? "))
                print()
                if input9==1:
                    cart.checkout()
                    print() #
                    break
                elif input9==2:
                    cart.abandon()
                    print() #
                    break
                else: 
                    print("Incorrect Input")
                    print()
            else:
                print("Incorrect Input")
                print()
        if input5==2:
            cart.show()
            print() #
            input8 = int(input("Buy [1] or Abandon Shopping [2]? "))
            print()
            if input8==1:
                cart.checkout()
                print() #
                break
            elif input8==2:
                cart.abandon()
                print() #
                break
            else: 
                print("Incorrect Input")
                print()
    
    else: 
        print("Incorrect Input")
        print()

ending.end_speech()

print(" ")
print("====================================================================")
print("Program by scein")
print("©️ Copyright 1969")
print("====================================================================")
print(" ")

#END
