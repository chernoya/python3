#Take out trash robot 
# 9/5/2022 @ 12:05PM
#

import time
import sys

day = 0

dialogue1 = ("Taking out trash. . . ")
dialogue11 = ("Walking to trash can. . . ")
dialogue111 = (" . . .Done! ")
dialogue2 = ("There is no need to take out the trash today . . . ")

jaws = 0

def take_out_trash():
    for a in dialogue1:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.2)
    for b in dialogue11:
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.2)
    for c in dialogue111:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

def no_reason_to_take_out_trash():
    for d in dialogue2:
        sys.stdout.write(d)
        sys.stdout.flush()
        time.sleep(0.2)    
              
while True:
    print("What day is it today?  ")
    day = input()
    if day=='monday':
        (take_out_trash())
        break
    if day=='wednesday':
        (take_out_trash())
        break
    if day=='thursday':
        (take_out_trash())
        break
    if day=='saturday':
        (take_out_trash())
        break
    if day=='sunday':
        (no_reason_to_take_out_trash())
        break
    if day=='tuesday':
        (no_reason_to_take_out_trash())
        break
    if day=='friday':
        (no_reason_to_take_out_trash())
        break
    else: 
        print('Enter a valid day of the week in l o w e r  c a s e')

exit