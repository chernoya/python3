import sys
import time

while True:
    input1 = str(input("Would you like the program to start? YES [y] / NO [n] "))
    if input1 in ['y','Y']:
        print("Starting the Bruteforce engine")
        break
    elif input1 in ['n' or 'N']:
        print("Closing program")
        break
    else:
        print("Error incorrect input")

print("Engine has started!")
input2 = input("Enter the name of the phone you would like to hack: ")

d1 = ("\n Cracking code . . .FAILED! \n")
d2 = ("\n Cracking pattern . . . . . . . SUCCESS!! \n")
d3 = ("\n Injecting virus . . . 1% . . . 38% . . . 78% . . . 99% . . SUCCESS! \n")
d4 = ("\n Deleting files . . . 4% . . . 18% . . . 38% . . . 60% . . . 88% . . . 96% . . . SUCCESS! \n")
d5 = ("\n Blocking access to the internet . . . 6% . . . 97% . . . SUCCESS! \n")
d6 = ("\n Stealing images and whatsapp messages . . . 54% . . . 99.9% SUCCESS! \n")
d7 = ("\n Hacking and taking control of Phone . . . 12% . . . 67.6% . . . SUCCESS! \n")
d8 = ("\n %s HAS BEEN HACKED! \n" %input2)

while True:
    for a in d1:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.07)
    for a in d2:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.07)
    for a in d3:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.07)
    for a in d4:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.07)
    for a in d5:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.07)
    for a in d6:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.07)
    for a in d7:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.07)
    for a in d8:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.07)                
    print("\n Closing the hacking program... Done!")
    break        
          

            