

cost_of_tiling = 0
area_of_walls = 0
revised_area = 0

tileprice = ['Null', 19.50, 25.95, 35.75, 12.50, 11.00, 52.95, 65.00, 58.98, 85.00, 62.75]

tiledesc_code_price = [['Code:', 1, 2, 3, 4, 5, 6,], ['Tile Description:', 'Small black granite', 'Small grey marble', 'Small powder blue', 'Medium sunset yellow', 'Medium berry red', 'Medium glitter purple', 'Large oak wood effect', 'Large black granite', 'Large bamboo effect', 'Extra-large white marble'], ['Price:', 19.50, 25.95, 35.75, 12.50, 11.00, 52.95, 65.00, 58.98, 85.00, 62.75]]

# TASK 1

for x, y, z in zip(*tiledesc_code_price):
    print(x, y, z)

while True:
    number_of_walls = int(input("Enter the number of walls you would like to tile: "))   #TASK 2
    if number_of_walls>4:
        print("Error max number of walls in a room are 4")
    else: 
        break

if number_of_walls==1:
    while True:
        length1 = int(input("what is the length of the wall?  "))
        if length1==0 or length1<0:
            print("Error, please enter a valid measurement")
        else: 
            break
    while True: 
        width1 = int(input("What is the Width of the wall?  "))
        if width1==0 or width1<0:
            print("Error, please enter a valid measurement")
        else:
            break
if number_of_walls==2:
    while True:
        length1 = int(input("what is the length of the wall?  "))
        if length1==0 or length1<0:
            print("Error, please enter a valid measurement")
        else: 
            break
    while True:
        length2 = int(input("what is the length of the second wall?  "))
        if length2==0 or length2<0:
            print("Error, please enter a valid measurement")
        else: 
            break
    while True: 
        width1 = int(input("What is the Width of the wall?  "))
        if width1==0 or width1<0:
            print("Error, please enter a valid measurement")
        else:
            break
    while True: 
        width2 = int(input("What is the Width of the second wall?  "))
        if width2==0 or width2<0:
            print("Error, please enter a valid measurement")
        else:
            break
if number_of_walls==3:
    while True:
        length1 = int(input("what is the length of the wall?  "))
        if length1==0 or length1<0:
            print("Error, please enter a valid measurement")
        else: 
            break
    while True:
        length2 = int(input("what is the length of the second wall?  "))
        if length2==0 or length2<0:
            print("Error, please enter a valid measurement")
        else: 
            break
    while True:
        length3 = int(input("what is the length of the third wall?  "))
        if length3==0 or length3<0:
            print("Error, please enter a valid measurement")
        else: 
            break
    while True: 
        width1 = int(input("What is the Width of the wall?  "))
        if width1==0 or width1<0:
            print("Error, please enter a valid measurement")
        else:
            break
    while True: 
        width2 = int(input("What is the Width of the second wall?  "))
        if width2==0 or width2<0:
            print("Error, please enter a valid measurement")
        else:
            break
    while True: 
        width3 = int(input("What is the Width of the third wall?  "))
        if width3==0 or width3<0:
            print("Error, please enter a valid measurement")
        else:
            break
if number_of_walls==4:
    while True:
        length1 = int(input("what is the length of the wall?  "))
        if length1==0 or length1<0:
            print("Error, please enter a valid measurement")
        else: 
            break
    while True:
        length2 = int(input("what is the length of the second wall?  "))
        if length2==0 or length2<0:
            print("Error, please enter a valid measurement")
        else: 
            break
    while True:
        length3 = int(input("what is the length of the third wall?  "))
        if length3==0 or length3<0:
            print("Error, please enter a valid measurement")
        else: 
            break
    while True:
        length4 = int(input("what is the length of the fourth wall?  "))
        if length4==0 or length4<0:
            print("Error, please enter a valid measurement")
        else: 
            break
    while True: 
        width1 = int(input("What is the Width of the wall?  "))
        if width1==0 or width1<0:
            print("Error, please enter a valid measurement")
        else:
            break
    while True: 
        width2 = int(input("What is the Width of the second wall?  "))
        if width2==0 or width2<0:
            print("Error, please enter a valid measurement")
        else:
            break
    while True: 
        width3 = int(input("What is the Width of the third wall?  "))
        if width3==0 or width3<0:
            print("Error, please enter a valid measurement")
        else:
            break
    while True: 
        width4 = int(input("What is the Width of the fourth wall?  "))
        if width4==0 or width4<0:
            print("Error, please enter a valid measurement")
        else:
            break
    
tilecode = int(input("Enter the code of the tile you prefer from (1 to 6):  "))
wastage = int(input("Enter the percentage of wasted tiles: "))

if number_of_walls==1:
    area_of_walls = (length1 * width1)
if number_of_walls==2:
    area_of_walls = (length1 * width1) + (length2 * width2) 
if number_of_walls==3:
    area_of_walls = (length1 * width1) + (length2 * width2) + (length3 * width3)
if number_of_walls==4:
    area_of_walls = (length1 * width1) + (length2 * width2) + (length3 * width3) + (length4 * width4)

waste_area = area_of_walls * (wastage/100)  #TASK 3
revised_area = area_of_walls - waste_area
cost_of_tiling = tileprice[tilecode] * revised_area 
numberofboxes = cost_of_tiling/tileprice[tilecode]  
estimate_no_of_boxes = round(numberofboxes) 
estimate_cost = round(cost_of_tiling)

print("The total area to tile is: ")
print(area_of_walls)
print("The total cost of tiling will be:")
print(estimate_cost)
print("The number of boxes of tiles per square meter required will be: ")
print(estimate_no_of_boxes)



