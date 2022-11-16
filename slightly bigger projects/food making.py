#recipe app 1.0

import time 
import sys 

#Variables

choice1 = 0
choice3 = 0
choice3 = 0
choice5 = 0
choice6 = 0
choice7 = 0
choice8 = 0
choice9 = 0
choice10 = 0
choice11 = 0
choice12 = 0

loopender = 0
loopender2 = 0
loopender3 = 0
loopender4 = 0
loopender5 = 0
loopender6 = 0
loopender7 = 0

dialogue1 = ("Nom nom nom . . . \n")  #eating food
dialogue2 = ("Delicious! \n")  #eating food
dialogue3 = ("You threw away your food \n") #throwaway food
dialogue4 = ("You fed a homeless and hungry animal \n") #donating food

dialogue5 = ("Gulp...Gulp...Gulp \n") #drinking
dialogue6 = ("Refreshing! \n") #drinking
dialogue7 = ("You threw away your drink! \n") #throaway drink
dialogue8 = ("You watered a plant with your drink ಠ_ಠ \n") #donating drink

dialogue9 =  ("Plucking mangos from a mango tree. . . . \n") #milkshake 
dialogue10 = ("Stealing milk from a cow. . . .  \n") #milkshake
dialogue11 = ("Robbing sugar canes of their sugar. . . \n") #milkshake
dialogue12 = ("Shipping ice from Antarctica for 5$ (╯°□°）╯︵ ┻━┻ \n") #milkshake

dialogue13 = ("Robbing a hen of it's eggs ╭∩╮（︶︿︶）╭∩╮ \n") #egg
dialogue14 = ("Getting oil from Putin ( ͡° ͜ʖ ͡°) \n") #egg
dialogue15 = ("Colonising india to get spices...\n") #egg

dialogue16 = ("Placing a frying pan on the stove...\n") #making egg
dialogue17 = ("Adjusting the heat...\n") #making egg
dialogue18 = ("Drizzling oil into the pan...\n") #making egg
dialogue19 = ("Cracking an egg...\n") #making egg
dialogue20 = ("Egg fries...\n") #making egg
dialogue21 = ("Flipping egg on it's other side...\n") #making egg
dialogue22 = ("Sprinkling salt, pepper and chili flakes on egg...\n") #making egg
dialogue23 = ("Egg is done! \n") #making egg

dialogue24 = ("Sliciing mangos into cube size pieces...\n")
dialogue25 = ("Filling Juicer with Milk . . . \n")
dialogue26 = ("Adding sugar to the juicer . . . \n")
dialogue27 = ("Dropping in the mango pieces . . . \n")
dialogue28 = ("Adding ice cubes . . . \n")
dialogue29 = ("Closing the lid of the juicer . . . \n")
dialogue30 = ("Zrrrrrrrrrr . . . Zrrrrrrrrrr . . . \n")
dialogue31 = ("The milkshake is done! \n")

Food_list = ['Fried Egg [1]'] 
Beverage_list = ['Mango Milkshake [1]']

#General functions of making food

class food:
    def eating(self):
        for a in dialogue1:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.2)
        for b in dialogue2:
            sys.stdout.write(b)
            sys.stdout.flush()
            time.sleep(0.1)
    def throwaway(self):
        for c in dialogue3:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)
    def donate(self):
        for d in dialogue4:
            sys.stdout.write(d)
            sys.stdout.flush()
            time.sleep(0.1)        

class drink: 
    def drinking(self):
        for e in dialogue5:
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.1)
        for f in dialogue6:
            sys.stdout.write(f)
            sys.stdout.flush()
            time.sleep(0.1)
    def throwaway(self):
        for g in dialogue7:
            sys.stdout.write(g)
            sys.stdout.flush()
            time.sleep(0.1)
    def waterplants(self):
        for h in dialogue8:
            sys.stdout.write(h)
            sys.stdout.flush()
            time.sleep(0.1)

class mango_milkshake(drink):
    def collecting_ingredients(self):
        for i in dialogue9:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)
        for j in dialogue10:
            sys.stdout.write(j)
            sys.stdout.flush()
            time.sleep(0.1)
        for k in dialogue11:
            sys.stdout.write(k)
            sys.stdout.flush()
            time.sleep(0.1)
        for l in dialogue12:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.1)
    def making_milkshake(self):
        for x in dialogue24:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.1)
        for y in dialogue25:
            sys.stdout.write(y)
            sys.stdout.flush()
            time.sleep(0.1)
        for z in dialogue26:
            sys.stdout.write(z)
            sys.stdout.flush()
            time.sleep(0.1)
        for aa in dialogue27:
            sys.stdout.write(aa)
            sys.stdout.flush()
            time.sleep(0.1)
        for ab in dialogue28:
            sys.stdout.write(ab)
            sys.stdout.flush()
            time.sleep(0.1)
        for ac in dialogue29:
            sys.stdout.write(ac)
            sys.stdout.flush()
            time.sleep(0.1)
        for ad in dialogue30:
            sys.stdout.write(ad)
            sys.stdout.flush()
            time.sleep(0.1)
        for ae in dialogue31:
            sys.stdout.write(ae)
            sys.stdout.flush()
            time.sleep(0.1)

class fried_egg(food):
    def collecting_ingredients(self):
        for m in dialogue13:
            sys.stdout.write(m)
            sys.stdout.flush()
            time.sleep(0.1)
        for n in dialogue14:
            sys.stdout.write(n)
            sys.stdout.flush()
            time.sleep(0.1)
        for o in dialogue15:
            sys.stdout.write(o)
            sys.stdout.flush()
            time.sleep(0.1)
    def making_food(self):
        for p in dialogue16:
            sys.stdout.write(p)
            sys.stdout.flush()
            time.sleep(0.1)
        for q in dialogue17:
            sys.stdout.write(q)
            sys.stdout.flush()
            time.sleep(0.1)
        for r in dialogue18:
            sys.stdout.write(r)
            sys.stdout.flush()
            time.sleep(0.1)
        for s in dialogue19:
            sys.stdout.write(s)
            sys.stdout.flush()
            time.sleep(0.1)
        for t in dialogue20:
            sys.stdout.write(t)
            sys.stdout.flush()
            time.sleep(0.1)
        for u in dialogue21:
            sys.stdout.write(u)
            sys.stdout.flush()
            time.sleep(0.1)
        for v in dialogue22:
            sys.stdout.write(v)
            sys.stdout.flush()
            time.sleep(0.1)
        for w in dialogue23:
            sys.stdout.write(w)
            sys.stdout.flush()
            time.sleep(0.1)

cooked_egg = fried_egg()
milkshake_mango = mango_milkshake()        

#Welcome screen

#START

print("Welcome to the Food making / Recipe Prgram! What would you like to do today?")
while loopender==0:
    print("Make food [F] or Make a Beverage [B]")
    choice1 = input()
    if choice1=='F':
        loopender = 1
        while loopender4==0:
            print("What would food you like to make? ")
            print(Food_list)
            choice3 = int(input())
            if choice3==1:
                loopender4 = 1
                print("Collecting ingredients...")
                cooked_egg.collecting_ingredients()
                choice5 = input("Ingredients have been collected! Would you like to cook your food? [Y] for Yes, [N] for No  ")
                if choice5=='Y':
                    cooked_egg.making_food()
                    choice7 = input("Would you like to Eat your food? [Y] or [N]  ")
                    if choice7=='Y':
                        cooked_egg.eating()
                    elif choice7=='N':
                        choice8 = input("Then what would you like to do with it? Donate [D] or Throwaway [T]  ")
                        if choice8=='D':
                            cooked_egg.donate()
                        elif choice8=='T':
                            cooked_egg.throwaway()
                        else:
                            print("Choose a valid option you fucking twat")
                    else:
                        print("Please pick a valid option")
                elif choice5=='N':
                    print("Okay!")
                    break
                else:
                    print("Error! Wrong input")
            else:
                print("Please choose from one of the available options!")
    elif choice1=='B':
        loopender = 1
        while loopender5==0:
            print("What would beverage you like to brew?")
            print(Beverage_list)
            choice4 = int(input())
            if choice4==1:
                loopender5 = 1
                print("Collecting ingredients...")
                milkshake_mango.collecting_ingredients()
                choice6 = input("Ingredients have been collected! Would you like to brew your desired refreshmen? [Y] for Yes, [N] for No  ")
                if choice6=='Y':
                    milkshake_mango.making_milkshake()
                    choice9 = input("Would you like to drink your freshly made beverage? [N] or [Y]  ")
                    if choice9=='Y':
                        milkshake_mango.drinking()
                    elif choice9=='N':
                        choice10 = input("What would you like to do with it then? Donate [D] or throwaway [T]  ")
                        if choice10=='D':
                            milkshake_mango.waterplants()
                        elif choice10=='T':
                            milkshake_mango.throwaway()
                        else:
                            print("Choose a valid option for fucks sake blyat suka")
                    else:
                        print("Error! Wrong input")
                elif choice6=='N':
                    print("okay!")
                    break
                else:
                    print("Error! Wrong input")
            else:
                print("Please pick from one of the available options")
    else:
        print("Wrong input!")
#END


    






