import random

#moduł standardowy biblioteki
rand_num= random.randint(0,2)
if rand_num == 0:
    computerMove ="kamień"
elif rand_num == 1:
    computerMove="nożyce"
else:
    computerMove ="papier"

print(computerMove)

print( "Witaj w grze nożyce,kamień, papier !")
print( "..........Komputer losuje")
player1 = input("Twoja kolej, co wybierasz: ")
print("Sprawdzam.....")

if computerMove == player1:
    print("Remis, komputer wylosował " + computerMove)
elif computerMove == "kamień" and player1 == "nożyce":
     print("Komputer Wygrywa, komputer wylosował " + computerMove)
elif computerMove == "papier" and player1 == "kamień":
     print("Wygrałeś, komputer wylosował " + computerMove)
elif player1 == "nożyce"   and computerMove == "papier"  :
     print("Wygrałeś, komputer wylosował: " + computerMove)
elif player1 == "kamień"   and computerMove == "nożyce"  :
          print("Wygrałeś, komputer wylosował: " + computerMove)
else:
     print("Komputer Wygrał...wylosowano: " + computerMove)

