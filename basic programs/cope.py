entry = str(input("how are you: "))
if entry=="bad":
    print("i hope you get better")
elif entry=="fine":
    two_entry = input("are you sure?: ")
    if two_entry=="no":
        print("i hope you get better")
    elif two_entry=="yes":
        print("good!")
    elif two_entry=="idk":
        third_entry = input("what's wrong?: ")
        if third_entry=="nothing":
            print("Ok")
        else:
            print("it's Ok, things change, you'll get better. I believe in you! ;) ")
    else:
        print("I didn't understand that :(")
elif entry=="wonderful":
    print("good!")
elif entry=="good":
    print("that's good!")
else:
    print("I didn't quite understand that..")
