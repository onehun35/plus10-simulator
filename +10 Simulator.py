import os, sys, random, time


def enhancing_animation():
    os.system("cls")
    print("Enhancing".center(100),end="")
    sys.stdout.flush()
    time.sleep(0.5)

    for i in range(3):
        os.system("cls")
        print(("Enhancing" + "." * (i + 1)).center(100))
        sys.stdout.flush()
        time.sleep(0.5)

    os.system("cls")

def success_message(e_state):
    print(f"Current Enhancement: +{e_state}".center(100))
    print()
    print("[Success!]".center(100))
    input(" " *50)

def downgrade_message(e_state):
    print(f"Current Enhancement: +{e_state}".center(100))
    print()
    print("[FAILED]".center(100))
    print()
    print("Your sword is Downgraded :(".center(100))
    input(" " *50)

def broken_message(e_state):
    print(f"Current Enhancement: +{e_state}".center(100))
    print()
    print("[FAILED]".center(100))
    print()
    print("Your sword is Broken :(".center(100))
    input(" " *50)

def shop (e_state,gold,bonus,protect):
    while True:
        os.system("cls")  

        print(f"Current Enhancement: +{e_state}")
        print(f"Gold: {gold} G")
        print()
        print("1.Buy\n2.Sell\n3.Exit")

        try:
            choice = int(input())

            if choice == 1:
                os.system("cls")

                print("1.Success +10 "+"%"+" coupon (300 G)\n2.Broken protect coupon (500 G)\n3.Exit")

                try:
                    buy = int(input())

                    if buy == 1:
                        if gold < 300:
                            os.system("cls")

                            print("You don't have enough gold!")
                            input()
                            continue
                        
                        else:
                            bonus += 1
                            gold -= 300

                            os.system("cls")

                            print("You buy a Success +10 "+"%"+" coupon!")
                            input()
                            continue

                    elif buy == 2:
                        if gold < 500:
                            os.system("cls")

                            print("You don't have enough gold!")
                            input()
                            continue
                        
                        else:
                            protect += 1
                            gold -= 500

                            os.system("cls")

                            print("You buy a protect coupon!")
                            input()
                            continue

                    elif buy == 3:
                        continue
                
                except:
                    os.system("cls") 
                    print("Invalid input!")
                    input()
                    continue

            elif choice == 2:

                if e_state == 0:
                    os.system("cls")  
                    print("You don't have anything to sell!")
                    continue

                gold += e_state*100

                os.system("cls")  

                print(f"You earn {e_state*100} G!")
                input()

                e_state = 0
                continue
                
            elif choice == 3:
                return e_state,gold,bonus,protect
            
            else:
                os.system("cls") 
                print("Invalid input!")
                input()
                continue

            
        except:   
            
            os.system("cls") 
            print("Invalid input!")
            input()
            continue



e_state = 0
gold = 0
bonus = 0
protect = 0
guaranteed = 0 


while True:
    os.system("cls")

    print("<Sword +10 simulator> - Challenge your limits!\n".center(100))
    print(f"Current Enhancement: +{e_state}")

    if e_state <= 5:
        print(f"Enhance possibility: {100 - 10*e_state} %")
    else:
        print("Enhance possibility: 50 %")

    print(f"Current gold: {gold} G")
    print(f"Coupon [Bonus: {bonus}, protect: {protect}]")
    
    try:
        choice = int(input("\n1.Enhance\n2.Shop\n3.Quit\n\nEnter your choice: "))
        if choice not in [1,2,3]:
            os.system("cls")
            print("Invalid input!".center(100))
            input()
            continue
        
    except:
        os.system("cls")
        print("Invalid input!".center(100))
        input()
        continue

   

    if choice == 1:

        if e_state < 6:

            success_rate = 100 - 10*e_state
            downgrade_rate = 10*e_state


            os.system("cls")
            pos = random.randint(1,100)
            
            print(f"Enhance possibility: {success_rate} %".center(100))

            if e_state > 0:
                print(f"Downgrade possibility: {downgrade_rate} %".center(100))
            
            print()
            print("1.Enhance 2.Use bonus Coupon 3.Exit".center(100))

            try:
                b_choice = int(input(" " *50))
                if b_choice not in [1,2,3]:
                    os.system("cls")
                    print("Invalid input!".center(100))
                    input()
                    continue
            except:
                os.system("cls")
                print("Invalid input!".center(100))
                input()
                continue

            if b_choice == 2:

                if e_state == 0:
                    os.system("cls")
                    print("Success posssibility is already 100"+"%!".center(100))
                    input()
                    continue
            
                if bonus == 0:
                    os.system("cls")
                    print("You don't have the coupon!".center(100))
                    input()
                    continue

                success_rate = 110 - 10*e_state
                downgrade_rate = 10*e_state - 10

                os.system("cls")
                print(f"Enhance possibility: {success_rate} %".center(100))
                print(f"Downgrade possibility: {downgrade_rate} %".center(100))
                print("Enter any button to enhance")
                input(" " *50)


            elif b_choice == 3:
                continue

            
            enhancing_animation()

            if pos <= (success_rate):
                e_state += 1

                success_message(e_state)

            else:
                if e_state > 0:
                    e_state -= 1

                downgrade_message(e_state)

        elif e_state >= 6:
            
            success_rate = 50
            broken_rate = (e_state - 5)*10
            downgrade_rate = (10 - e_state)*10

            os.system("cls")
            pos = random.randint(1,100)
            print(f"Enhance possibility: {success_rate} %".center(100))
            print(f"Broken possibility: {broken_rate} %".center(100))
            print(f"Downgrade possibility: {downgrade_rate} %".center(100))
            print()
            print("1.Enhance 2.Use bonus Coupon 3.Exit".center(100))
            
            try:
                b_choice = int(input(" " *50))
                if b_choice not in [1,2,3]:
                    os.system("cls")
                    print("Invalid input!".center(100))
                    input()
                    continue
            except:
                os.system("cls")
                print("Invalid input!".center(100))
                input()
                continue

            if b_choice == 2:

                if bonus == 0:
                    os.system("cls")
                    print("You don't have the coupon!".center(100))
                    input()
                    continue

                success_rate = 60
                broken_rate = (e_state - 5)*10 - 5
                downgrade_rate = (10 - e_state)*10 - 5

                os.system("cls")
                print(f"Enhance possibility: {success_rate} %".center(100))
                print(f"Broken possibility: {broken_rate} %".center(100))
                print(f"Downgrade possibility: {downgrade_rate} %".center(100))
                print("Enter any button to enhance")
                input(" " *50)


            elif b_choice == 3:
                continue

            enhancing_animation()

            if pos <= broken_rate:
                
                if protect > 0:
                    protect -= 1
                    os.system("cls") 
                    print("Your sword is protected by the coupon!")
                    continue

                e_state = 0 
                broken_message(e_state)
                

            elif pos <= success_rate and pos > broken_rate:
                e_state -= 1 
                downgrade_message(e_state)
                

            else:
                e_state += 1
                success_message(e_state)

            if e_state == 10:
                os.system("cls") 
                print("Congratulation! you win!".center(100))    

    elif choice == 2:
        e_state,gold,bonus,protect = shop (e_state,gold,bonus,protect)

    elif choice == 3:
        os.system("cls")
        print("See ya~!".center(100))
        exit()

    else:
        print("It's impossible!")
        continue