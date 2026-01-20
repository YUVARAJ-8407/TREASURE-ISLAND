def game_over():
    print("Your guess is wrong😭")
    print("You are not qualified to the next round")
    print("GAME OVER")
def guess_correct():
    print("Your guess is exact🙌")
    print("You are qualified to the next round")

print("Welcome to TREASURE ISLAND😊")
print("Your mission is to find the treasure")
while True:
    choice=input("Choose: 'LEFT' or 'RIGHT'").upper()
    if choice=="LEFT":
        guess_correct()
        choice = input("Choose: 'SWIM' or 'WAIT'").upper()
        if choice == "WAIT":
            guess_correct()
            choice = input("Choose which door: 'RED','BLUE','GREEN'").upper()
            if choice == "GREEN":
                print("Your guess is exact🙌")
                print("You WIN")
            elif choice == "BLUE" or choice == "RED":
                game_over()
                break
            else:
                print("You typed an invalid choice😑")
        elif choice == "SWIM":
            game_over()
            break
        else:
            print("You typed an invalid choice😑")
    elif choice=="RIGHT":
        game_over()
        break
    else:
        print("You typed an invalid choice😑")

    while True:
        now = input("Do you want to restart: 'YES' or 'NO'").upper()
        if now == "YES":
            break
        elif now == "NO":
            print("Thanks for playing")
            exit()
        else:
            print("You typed an invalid choice; Please type: 'YES' or 'NO'")
