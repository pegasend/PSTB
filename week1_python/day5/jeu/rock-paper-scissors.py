#!/usr/bin/python

# execution : $python rock-paper-scissors.py
# fichier pour l'affichage menu(rock-paper-scissors.py): fonctions pour afficher menu principal, gérer la saisie utilisateur et afficher résumé jeu avant de quitter


import game # importer la class Game du fichier game.py
# ./classes/game.py
#from classes import game #le fichier game.py dans le dossier classes (./classes/game.py)

# ou
#import classes.game # importer la class Game dans (./classes/game.py) le dossier classes où se trouve le fichier game.py



# fonctions pour afficher le menu principal,
def get_user_menu_choice():
    print("\n\tMenu: ?")
    s=''
    while len(s)==0 or (s!='g' and s!='x'): # Affichage répété du menu
        s=input("\t(g) Play a new (g)ame\n\tor\n\t(x) Show scores and e(x)it: ").lower()# et afficher le résumé du jeu
    return s# renvoyer le choix.

# afficher les résultats des parties jouées.
def print_results(results):# dico des parties jouées => all_results
    #Il devrait afficher ces résultats de manière conviviale
    print("\n\tall Games Results:")
    print(f"\tyou won {results['win']} times\n\tyou lost {results['loss']} times\n\tyou drew {results['draw']} times")
    # et remercier l'utilisateur d'avoir joué.
    print("\n\tthank you for playing!")

    #=> boucler?

if __name__ == "__main__":
    #créer un dictionnaire qui va sauvegarder mes resultats
    all_results={"win" : 0, "loss" : 0, "draw": 0} #init

    # print(get_user_menu_choice() ) # pour tester

    # Affichage répété du menu, jusqu'à ce que l'utilisateur saisisse la valeur pour quitter le programme :
    # « x » ou « g », selon votre choix.
    s_choix_menu=get_user_menu_choice()
    #print("while:",s)
    while s_choix_menu=='g':# tant que "g" : DANS LA BOUCLE WHILE => gérer la saisie de l'utilisateur
        # Lorsque l'utilisateur choisit de jouer à un jeu :
        # Créez un nouvel Game objet (voir ci-dessous) et appelez sa play()fonction, en recevant le résultat du jeu qui est renvoyé.
        # Récupérez l'objet de l'utilisateur (pierre/papier/ciseaux) et mémorisez-le
        jjeu=game.Game() # import game du fichier game.py où la class Game() est définie
        # jjeu=game.Game()
        #jjeu=classes.game.Game()

        # play() appelée depuis l'extérieur de la classe (c'est-à-dire depuis rock-paper-scissors.py )
        # Souvenez-vous des résultats de chaque partie jouée.
        all_results[jjeu.play()] += 1# j'utilise la string 'win' ou 'loss' ou 'draw', comme une clef de mon dictionnaire

        s_choix_menu=get_user_menu_choice()# renvoi 'g' ou 'x'

    # Lorsque l'utilisateur choisit de quitter le programme,
    #  appelez la print_results() afin d'afficher un résumé de toutes les parties jouées.
    if s_choix_menu=='x':
        # avant de quitter.
        # Lorsque l'utilisateur choisit de quitter le programme, appelez la fonction print_results() afin d'afficher un résumé de toutes les parties jouées.
        print_results(all_results)#all_results={"win" : 0, "loss" : 0, "draw": 0}

    else:
        print("erreur de saisie")

#EOF
