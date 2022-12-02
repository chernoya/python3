# SLAVE MARKET APP 1.0 
# DATE STARTED 9/4/2022 @ 12:50PM
# BY SCEIN


from datetime import datetime
import sys
import time

choice1 = 0
choice2 = 0
choice3 = 0 

dialogue1 = ("Alright you can afford a wide variety of slaves (｡◕‿◕｡) ")
dialogue2 = ("You are too poor to afford a slave (ﾉಥ益ಥ）ﾉ ┻━┻ . . .")
dialogue4 = ("You're too rich for us!")
dialogue5 = ("We do not sell any animals, please visit your nearest pet shop for further assistance!")
dialogue6 = ("Okay!")
receipt_message1 = ("Congratulations you've bought your first slave! ")
receipt_message2 = ("You didn't buy any slaves . . . . . . . .(ಥ益ಥ)")
main_receiptmsg = 0

money = 0 
money_left = 0

userinput1 = 0

class Slaves:
 
    def __init__(self, name, price, strength, intelligence):
        self.name = name
        self.price = price
        self.strength = strength
        self.intelligence = intelligence
 
    def __repr__(self):
        return  " \n " + self.name + ', ' + ' $'+ str(self.price) + ', ' + ' Strength: ' + str(self.strength) + ', ' + str(self.intelligence) +" IQ" + ' \n '
slaves = [
        Slaves('Osas', 650, 4.5, 105 ),
        Slaves('James', 500, 4, 113),
        Slaves('Abdul', 490, 4.2, 102)
        ]

sold_slaves = []

Osas = slaves[0]
Abdul = slaves[1]
James = slaves[2]


def SellSlave():
    while True:
        choice3 = int(input("Which slave would you like to buy? -> Osas [1], James [2], Abdul [3] or None [4] "))
        if choice3==1:
            sold_slaves.append(Slaves('Osas', 650, 4.5, 105 ))
            del slaves[0]
            money_left = money - 650
            main_receiptmsg = receipt_message1
            break
        if choice3==2:
            sold_slaves.append(Slaves('James', 530, 4, 113))
            del slaves[1]
            money_left = money - 530
            main_receiptmsg = receipt_message1
            break
        if choice3==3:
            sold_slaves.append(Slaves('Abdul', 510, 4.2, 102))
            del slaves[2]
            money_left = money - 510
            main_receiptmsg = receipt_message1
            break
        if choice3==4:
            print("Okay come again soon!")
            sold_slaves.append("None")
            money_left = money
            main_receiptmsg = receipt_message2
            break
        else:
            print("Choose a valid option ffs")
    
    print('                                                ')
    print('================================================')
    print(main_receiptmsg)
    print('================================================') 
    print('                                                ')
    print('================================================')
    print('               R E C E I P T                    ')
    print('                                                ')
    print("Slave Bought:                                   ")
    print(sold_slaves)
    print('                                                ')
    print("Money left:                                     ")
    print(money_left)
    print('                                                ')
    print('================================================')

def text1():
    for a in dialogue1:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.1)
def text2():
    for b in dialogue2:
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.1)
def text4():
    for d in dialogue4:
        sys.stdout.write(d)
        sys.stdout.flush()
        time.sleep(0.1)
def text5():
    for e in dialogue5:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)
def text6():
    for f in dialogue6:
        sys.stdout.write(f)
        sys.stdout.flush()
        time.sleep(0.1)

print("=====================================================================================")
print("   W  E  L  C  O  M  E     T  O     T  H  E     S  L  A  V  E     M  A  R  K  E  T")
print("=====================================================================================")

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("DATE AND TIME >>> ", dt_string)

while True:
    print("============================================================================")
    choice1 = input("What would you like to buy today? -> Slaves [1], Animals [2], Nothing [3] ")
    print("============================================================================")
    if choice1=='1':
        money = float(input("What is your budget? ->  "))
        if money<=1000 and money>=600:
            text1()
            while True:
                 print('                                                                          ')
                 print("What are you most interested in? Price [1], Strength [2], Intelligence [3]")
                 userinput1 = int(input())
                 if userinput1==1:
                     slaves.sort(key=lambda x: x.price)
                     print(slaves)
                     SellSlave()
                     break
                 elif userinput1==2:
                    slaves.sort(key=lambda x: (x.strength), reverse=True)
                    print(slaves)
                    SellSlave()
                    break
                 elif userinput1==3: 
                    slaves.sort(key=lambda x: (x.intelligence), reverse=True)
                    print(slaves)
                    SellSlave()
                    break
                 else: 
                    print("Kindly enter a valid option!")    
        elif money<600:
            text2()
        elif money>1000:
            text4()
        else: 
            print("Kindly enter a valid amount of money")
        break
    elif choice1=='2':
        text5()
        break
    elif choice1=='3':
        text6()
        break
    else:
        print("Kindly enter a valid option!")

#END
