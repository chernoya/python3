#pp size enhancer 1.0 

import sys
import time

var = 1
dialogue_startengine = "Starting infinity engine 1 . . . 2 . . . 3 . . . ENGINE STARTED!"

def engine_start():
    for i in dialogue_startengine:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.2)
        
pp_size = float(input("What is your pp size? "))
choice = str(input("Would you like to increase your pp size? YES [y] NO [n] "))
while var==1:
    
    if choice in ['y', 'Y']:
        var = 0
        choice_1 = str(input("By how much? INFINITY [x] Nothing [n] "))
        
        if choice_1 in ['x', 'X']:
            engine_start()
            
            while True:             
                pp_size = pp_size + 1
                print("Your pp is now %s inches long" %pp_size)
        
        elif choice_1 in ['n', 'N']:
            print("Alright")
                    
        else:
            print("I didn't understand that")
    
    elif choice in ['n', 'N']:
        print("Ok")
        var = 0
    
    else:
        print("I didn't understand that")


#END