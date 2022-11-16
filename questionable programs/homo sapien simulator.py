
import time
import sys

class human():
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def suicide(self):
        a = (f"{self.name} climbed the stairs of a tall building . . .    \n")
        b = (f"{self.name} stood at the edge of the tall building . . .  \n")
        c = (f'{self.name} took a deep breath and jumped off building . . .  \n')
        d = (f"{self.name} died at the age of {self.age} of suicide . . .(╥﹏╥)   \n")
        
        for w in a:
            sys.stdout.write(w)
            sys.stdout.flush()
            time.sleep(0.1)
        for x in b:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.1)
        for y in c:
            sys.stdout.write(y)
            sys.stdout.flush()
            time.sleep(0.1)
        for z in d:
            sys.stdout.write(z)
            sys.stdout.flush()
            time.sleep(0.1)
            
hooman_name = str(input("Enter a human name: "))
hooman_age = float(input("Enter %s's age: " %hooman_name))
homo_sapien = human(hooman_name, hooman_age)

choice = str(input("What would you want your human to do? Suicide [S] or Nothing [X] "))
if choice in ['S', 's']:
    homo_sapien.suicide()
    respect = str(input("Press F to pay respects "))
    if respect in ['f', 'F']:
        print("You payed your respects")
    else:
        print("You didn't pay your respects (┛ಠДಠ)┛彡┻━┻ ")
elif choice in ['X', 'x']:
    print(". . .")
else: 
    print("Error! wrong input")




