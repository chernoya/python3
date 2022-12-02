
#START

name = str(input("type a name: "))  #user input of whatever name / company 
name_list = name.split()            #splits the words into elements in a list

ignore_list = ['and', 'And', 'AND', 'the', 'The', 'THE', 'of', 'Of', 'OF', 'for', ' For', 'FOR', 'that', 'That', 'THAT'] 

#for loop which repeats itself for the number of words in the list and delete that match in ignore list
for word in name_list:          
    if word in ignore_list:
        name_list.remove(word)
    else:
        pass

# 1 variable that will be used later // 2 make a new list to store the first letter of each word in the list
x = 0                         
name_list_new = []

#for loop which repeats for every word in the list and stores the first letter of each word as a string in the new list
for letter in name_list: 
    name_list_new.append(' '.join(letter[x].split()))

#removes the [ ] brackets from string and capitalizes ever letter
monogram = (str((' '.join(str(y) for y in name_list_new))).upper()) 

#prints the output monogram/initial
print(monogram)

#END