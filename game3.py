import random
print("snake,water,gun")
game=["s","w","g"]


restart=True
while restart:
    computerscore=0
    yourscore=0
    for i in range(1,5):
        print("round",i)
        comp=(random.choice(game))
        you=(input("Choose any ome:snake(s),water(w),gun(g)="))

        print(f"computer choose {comp}")
        print(f"you choose {you}")

        if you == comp:
            print("This match is tie")

        elif you=='s' and comp=='w':
            print("you win this match")
            yourscore+=1
        elif you=='w' and comp=='s':
            print("computer win this match")
            computerscore+=1
        elif comp=='g' and you=='w':
            print("you win this match")
            yourscore+=1
        elif comp=='w' and you=='g':
            print("computer win this match")
            computerscore+=1

        elif you=='g' and comp=='s':
            print("you win this match")
            yourscore+=1
        elif comp=='g' and you=='s':
            print("computer win this match ")
        else:
            print("Choose a valid input")

        if i>=4:
            n = input("you want to continue game yes or no: ")
            if n=="no":
             restart=False
            break
if yourscore < computerscore:
          print(f" Sorry You lose the game  computer win the "f"game with {computerscore} score")
elif yourscore == computerscore:
        print( " Game is tie play again ")
else:
        print(f" You Win the game with {yourscore} score ")










