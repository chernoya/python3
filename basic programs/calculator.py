#basic calculator 1.0

Number1 = 0
Number2 = 0
Number3 = 0
Number4 = 0
Number5 = 0
answer = 0

print("welcome to calculator basic!")
choice1 = input("What would you like to do? + - / *: ")

if choice1 == "+":
    calc1 = int(input("Okay, How many numbers would you like to add between 1 to 5): "))
    if calc1 == 1:
        print("you must pick more than one number")
    elif calc1 == 2:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        answer = Number1 + Number2
        print(answer)
    elif calc1 == 3:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        Number3 = int(input("Enter the third number: "))
        answer = Number1 + Number2 + Number3
        print(answer)
    elif calc1 == 4:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        Number3 = int(input("Enter the third number: "))
        Number4 = int(input("Enter the fourth number: "))
        answer = Number1 + Number2 + Number3 + Number4
        print(answer)
    elif calc1 == 5:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        Number3 = int(input("Enter the third number: "))
        Number4 = int(input("Enter the fourth number: "))
        Number5 = int(input("Enter the fifth number: "))
        answer = Number1 + Number2 + Number3 + Number4 + Number5
        print(answer)
    else:
        print("Wrong input! Try again")
#subtraction

elif choice1 == "-":
    calc1 = int(input("Okay, How many numbers would you like to minus between 1 to 5): "))
    if calc1 == 1:
        print("you must pick more than one number")
    elif calc1 == 2:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        answer = Number1 - Number2
        print(answer)
    elif calc1 == 3:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        Number3 = int(input("Enter the third number: "))
        answer = Number1 - Number2 - Number3
        print(answer)
    elif calc1 == 4:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        Number3 = int(input("Enter the third number: "))
        Number4 = int(input("Enter the fourth number: "))
        answer = Number1 - Number2 - Number3 - Number4
        print(answer)
    elif calc1 == 5:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        Number3 = int(input("Enter the third number: "))
        Number4 = int(input("Enter the fourth number: "))
        Number5 = int(input("Enter the fifth number: ")) 
        answer = Number1 - Number2 - Number3 - Number4 - Number5
        print(answer)
    else:
        print("Wrong input! Try again")

#division

elif choice1 == "/":
    calc1 = int(input("Okay, How many numbers would you like to divide between 1 to 5): "))
    if calc1 == 1:
        print("you must pick more than one number")
    elif calc1 == 2:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        answer = Number1 / Number2
        print(answer)
    elif calc1 == 3:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        Number3 = int(input("Enter the third number: "))
        answer = Number1 / Number2 / Number3
        print(answer)
    elif calc1 == 4:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        Number3 = int(input("Enter the third number: "))
        Number4 = int(input("Enter the fourth number: "))
        answer = Number1 / Number2 / Number3 / Number4
        print(answer)
    elif calc1 == 5:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        Number3 = int(input("Enter the third number: "))
        Number4 = int(input("Enter the fourth number: "))
        Number5 = int(input("Enter the fifth number: "))
        answer = Number1 / Number2 / Number3 / Number4 / Number5
        print(answer)
    else:
        print("Wrong input! Try again")

#multiplication

elif choice1 == "*":
    calc1 = int(input("Okay, How many numbers would you like to multiply between 1 to 5): "))
    if calc1 == 1:
        print("you must pick more than one number")
    elif calc1 == 2:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        answer = Number1 * Number2
        print(answer)
    elif calc1 == 3:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        Number3 = int(input("Enter the third number: "))
        answer = Number1 * Number2 * Number3
        print(answer)
    elif calc1 == 4:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        Number3 = int(input("Enter the third number: "))
        Number4 = int(input("Enter the fourth number: "))
        answer = Number1 * Number2 * Number3 * Number4
        print(answer)
    elif calc1 == 5:
        Number1 = int(input("Enter the first number: "))
        Number2 = int(input("Enter the second number: "))
        Number3 = int(input("Enter the third number: "))
        Number4 = int(input("Enter the fourth number: "))
        Number5 = int(input("Enter the fifth number: "))
        answer = Number1 * Number2 * Number3 * Number4 * Number5
        print(answer)
    else:
        print("Wrong input! Try again")
else:
    print("Wrong input! Please type the correct option")

#END






