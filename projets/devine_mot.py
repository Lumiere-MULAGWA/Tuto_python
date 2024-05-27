import random
import os



def devine():
    nombre_mystere = random.randint(1,10)
    essaie = 0
    os.system("clear")
    print("+"*50)
    print("+\t Bienvenue dans le jeu devine mot  \t+")
    print("+"*50)
    while essaie <=3:

        nombre_user = int(input("\tentrer votre nombre: "))
        if nombre_mystere == nombre_user:
            print("\tvous avez reussi a trouver le bon nombre ")
            demande()
            break
        else:
            
            if nombre_user < nombre_mystere:
                print("\tle nombre est plus grand ")
                print(f"\til vous reste {3 -essaie}")
            else :
                print("\tle nombre est plus petit")
                print(f"\til vous reste {3 -essaie}")
                print("#"*50)
            essaie += 1
        if essaie== 4:
            demande()
        
def demande():
    print("-"*50)
    print("\tvoulez vous recommencer ? (o/n) ")
    choix = input("\t\t>>> ")
    if choix != "o":
        print("\t\tBye bye (^_^)")
    else:
        devine()
devine()



