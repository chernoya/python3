#task 1 


onewayticket = 25
Uptime = ["9:00", "11:00", "13:00", "15:00"]
Upseats = [480, 480, 480, 480]
Takenupseats = [0, 0, 0, 0]
Upmoney = [0, 0, 0, 0]

Downtime = ["10:00", "12:00", "14:00", "16:00"]
Downseats = [480, 480, 480, 480]
Takendownseats = [0, 0, 0, 0]
Downmoney = [0, 0, 0, 0]

Maxpassengertrain = [0, 0, 0, 0]
numofpassenger = 0 
uptrip = 0
downtrip = 0 
cost = 0
discounted_cost = 0
twowayticket = 0
total_passenger = 0
total_amount = 0

print("welcome to train journey!")
for i in range(0, 3):
        print("train num:", [i], "Train Up time:", Uptime[i], "Up seats:", Upseats[i], "Taken up seats:", Takenupseats[i])
        print("Total up money:", Upmoney[i])
        print("train num:", [i], "Train Down time:", Downtime[i], "Down seats:", Downseats[i], "Taken down seats:", Takendownseats[i])
        print("Total down money:", Downmoney[i])
#task 2 
choice1 = input("Want to buy tickets? Type true for yes and false for no: ")
while choice1=="true":
        numofpassenger = int(input("enter the number of passengers for the trip "))
        total_passenger = numofpassenger + total_passenger

        uptrip = int(input("enter train to journey up [0, 1, 2, 3]: "))
        Takenupseats[uptrip] = Takenupseats[uptrip] + numofpassenger
        Upseats[uptrip] = Upseats[uptrip] - numofpassenger

        downtrip = int(input("enter train journey down [0, 1, 2, 3]: "))
        Takendownseats[downtrip] = Takendownseats[downtrip] + numofpassenger
        Downseats[downtrip] = Downseats[downtrip] - numofpassenger

        cost = numofpassenger * onewayticket
        discounted_cost = cost - (onewayticket * (numofpassenger / 10))
        
        twowayticket = discounted_cost * 2
        Upmoney[uptrip] = Upmoney[uptrip] + discounted_cost
        Downmoney[downtrip] = Downmoney[downtrip] + discounted_cost

        total_amount = total_amount + Upmoney[uptrip] + Downmoney[downtrip]

        for i in range(0, 3):
                if Upseats[i]==0:
                        print(Uptime[i] + " train full, booking closed")
                else:
                        print(Uptime[i] + " seat available, booking open!")
                
                if Downseats[i]==0:
                        print(Downtime[i] + " train full, booking closed")
                else:
                        print(Downtime[i] + " seat available, booking open!")
        choice1 = input("do you want to buy more tickets? ")
#task 3
Maxtrainup = 0
Maxtraindown = 0
print("end of the day")
for i in range(0, 3): 
        if Takenupseats[i] > Maxpassengertrain[i]:
                Maxpassengertrain[i] = Takenupseats[i] + Maxpassengertrain[i]
                Maxtrainup = Uptime[i]
        elif Takendownseats[i] > Maxpassengertrain[i]:
                Maxpassengertrain[i] = Takendownseats[i] + Maxpassengertrain[i]
                Maxtraindown = Downtime[i]
print("total money earned today: ")
print(total_amount)
print("total passengers travelled today: ")
print(total_passenger)
print("Max train passengers upwards: ")
print(Maxtrainup)
print("Max train passengers downwards: ")
print(Maxtraindown)

#end






        




        
