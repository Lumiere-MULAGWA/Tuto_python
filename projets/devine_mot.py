import random

nombre_mystere = random.randint(1,10)

def devine():
    essaie = 0
    while essaie <=3:

        nombre_user = int(input("entrer votre nombre: "))
        if nombre_mystere == nombre_user:
            print("vous avez reussi a trouver le bon nombre ")
            break
        else:
            
            if nombre_user < nombre_mystere:
                print("le nombre est plus grand ")
                print(f"il vous reste {3 -essaie}")
            else :
                print("le nombre est plus petit")
                print(f"il vous reste {3 -essaie}")
        essaie += 1
def demande():
    print("voulez vous recommencer ? (o/n) ")
    choix = input(">>> ")
    if choix != "o":
        print("Bye bye ")
    else:
        devine()
devine()



