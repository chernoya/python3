
continue_shopping = True
remove_items = True 

#START

print("welcome screen")

#should be function? 
while continue_shopping==True:
    print("aisles [bread, self-care & hygiene etc]")
    input1 = int(input("Choose aisle [1] or stop shopping? [2] "))
    if input1==1:
        continue_aisle = True
        while continue_aisle==True:
            print("Aisle 1")
            input2 = int(input("Buy from this aisle [1] yes [2] No "))
            if input2==1:
                input3 = int(input("which item [1] [2] [3] [4] None "))
                if input3==1 or 2 or 3:
                    #cart.add_item() 
                    print("added to cart!")
                    input4 = int(input("Done buying from this aisle? [1] yes, [2] no "))
                    if input4==1:
                        print("okay")
                        continue_aisle = False
                    if input4==2:
                        print("")
                else:
                    print("error 1")
            elif input2==2:
                continue_aisle = False     
            else: 
                print("error 2")
    if input1==2: 
        continue_shopping = False
        input5 = int(input("review cart [1] or proceed to checkout [2] "))
        if input5==1:
            print("cart: Items, price, total cost")                
            input6 = int(input("remove items [1] or proceed to checkout [2] "))
            if input6==1:
                while remove_items==True: 
                    number_of_items = int(input("how many items to remove "))
                    for x in range(0, (number_of_items)):
                        print("cart: items, price, total cost")
                        code_to_remove = int(input("Removal: " + str((x + 1)) + " Enter their positional number from 0, 1, 2 and so on: "))
                        #cart.remove(code_to_remove)
                        print("cart: items, price, total cost")
                    
                    input7 = int(input("remove items [1], checkout [2] "))
                    if input7==1:
                        print("okay")
                    elif input7==2:
                        remove_items = False
                        print("Cart: items, price, total cost")
                        input10 = int(input("buy [1] or abandon shopping [2]? "))
                        if input10==1:
                            #cart.checkout()
                            #end
                            print("DONE HERES YOUR RECEIPT PLEASE COME AGAIN")
                            break
                        elif input10==2:
                            #cart.abandon()
                            #end
                            print("YOU ABANDONED YOUR SHOPPING")
                            break
                        else: 
                            print("error 7")
                    else: 
                        print("error 3")
            elif input6==2:
                print("Cart: items, price, total cost")
                input9 = int(input("buy [1] or abandon shopping [2]? "))
                if input9==1:
                    #cart.checkout()
                    #end
                    print("DONE HERES YOUR RECEIPT PLEASE COME AGAIN")
                    break
                elif input9==2:
                    #cart.abandon()
                    #end
                    print("YOU ABANDONED YOUR SHOPPING")
                    break
                else: 
                    print("error 4")
            else:
                print("error 5")
        if input5==2:
            print("Cart: items, price, total cost")
            input8 = int(input("buy [1] or abandon shopping [2]? "))
            if input8==1:
                #cart.checkout()
                #end
                print("DONE HERES YOUR RECEIPT PLEASE COME AGAIN")
                break
            elif input8==2:
                #cart.abandon()
                #end
                print("YOU ABANDONED YOUR SHOPPING")
                break
            else: 
                print("error 6")
#END