#!/usr/bin/python
# execution : $python XP_day3.py

import random
# fichier affichage (game.py)
# fichier logique jeu (rock-paper-scissors.py )

if __name__ == "__main__":
    # Exo1
    class Game() :
        def __init__(self) :
            pass
        #def __init__(self, fn, ln, age, job='developer', salary=15000) :
        #    self.first_name = fn


        #utilisez la validation des données et la boucle
        def get_user_item(self, question):
            s=''
            while len(s)==0 or s.lower()!='r' or s.lower()!='p' or s.lower()!='s': #Continuez à demander jusqu'à ce que l'utilisateur ait sélectionné l'un des éléments
                s=input(question)#Demandez à l'utilisateur de sélectionner un élément (pierre/papier/ciseaux)
                if s.lower()!='r' or s.lower()!='p' or s.lower()!='s':
                    print("fournir une autre reponse conforme cette fois")
            return s.lower()# Renvoie l'élément à la fin de la fonction

        # Sélectionnez au hasard le jeu pierre/papier/ciseaux pour l'ordinateur.
        #Renvoyer l'élément à la fin de la fonction. Utilisez la fonction Python random.choice()
        def get_computer_item(self):
            s=random.choice("rock", "paper","scissors")
            return s
        # récup user_choice
        # condition => quel choix est le + fort
        def get_game_result(self, user_item, computer_item):
            return # resultat
        # appel get_user_item() pour avoir get_user_item: userchoice= self.get_user_item()
        # appel get_computer_item() pour avoir computer_choice: computer_choice=
        # affiche result
        # return win ou loss ou draw (égalité)
        def play(self):
            return

    jeu=Game()
    print(jeu.get_user_item("rock(r)/paper(p)/scissors(s)? ") )
    print(jeu.get_computer_item() )

    print()
#EOF
