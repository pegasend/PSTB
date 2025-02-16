#!/usr/bin/python
# execution : $python game.py

import random
# fichier pour la logique du jeu (game.py): Classe Game(), déterminer le résultat du jeu et renvoyer le résultat.

# Exo1
class Game() :
    def __init__(self) :
        pass

    #utilisez la validation des données et la boucle
    def get_user_item(self, question):
        s_choix_user=''
        while len(s_choix_user)==0 or (s_choix_user!='r' and s_choix_user!='p' and s_choix_user!='s'):#Continuez à demander jusqu'à ce que le user ait sélectionné 1 des éléments
            s_choix_user=input(question).lower()#Demandez à l'utilisateur de sélectionner un élément (pierre/papier/ciseaux)
            if s_choix_user!='r' and s_choix_user!='p' and s_choix_user!='s':
                print("fournir une autre reponse conforme cette fois\n")# informer que ce n'est pas la bonne réponse
        return s_choix_user# Renvoie l'élément à la fin de la fonction

    # Sélectionnez au hasard le jeu pierre/papier/ciseaux pour l'ordinateur.
    #Renvoyer l'élément à la fin de la fonction. Utilisez la fonction Python random.choice()
    def get_computer_item(self):
        return random.choice(["rock", "paper","scissors"])[0]# Utilisez la fonction Python random.choice() pour le choix au hasard du computer

    # récup user_choice et computer_choice
    def get_game_result(self, user_item, computer_item):
        if user_item==computer_item:
            print(f"Egality, You selected ({user_item}). The computer selected ({computer_item}). You drew!")
            return 'draw' # Un match nul (égalité)

        else: # condition => quel choix est le + fort
            if (user_item=='s' and computer_item=='p') or (user_item=='p' and computer_item=='r') or (user_item=='r' and computer_item=='s'):
                print(f"It's different: You selected ({user_item}). The computer selected ({computer_item}). You win !")
                return 'win'# L'utilisateur a gagné

            elif (computer_item=='s' and user_item=='p') or (computer_item=='p' and user_item=='r') or (computer_item=='r' and user_item=='s'):
                print(f"It's different: You selected ({user_item}). The computer selected ({computer_item}). You lose")
                return 'loss' # L'ordinateur a gagné (l'utilisateur a perdu)
        #return => resultat# resultat win/loss/draw => {win: 2,loss: 4,draw: 3}, transmis à la fonction print_results() dans rock-paper-scissors.py

    def play(self):
        # 1.Récupérez l'objet de l'utilisateur (pierre/papier/ciseaux) et mémorisez-le
        # appel get_user_item() pour avoir get_user_item: userchoice= self.get_user_item()
        user_item = self.get_user_item("Select ? (r)ock, (p)aper, (s)cissors : ")
        #print("You chose:", user_item)

        # 2.Prenez un objet aléatoire pour l'ordinateur (pierre/papier/ciseaux) et mémorisez-le
        # appel get_computer_item() pour avoir computer_choice: computer_choice=
        computer_item=self.get_computer_item()
        #print("The computer chose:", computer_item)

        # 3.Déterminer les résultats du jeu en comparant l'objet de l'utilisateur et l'objet de l'ordinateur
        # affiche result
        game_result=self.get_game_result(user_item, computer_item)
        #print("Result:", game_result )

        return game_result # return 'win' ou 'loss' ou 'draw' (égalité)

if __name__ == "__main__": # que le main de game.py, donc pas executé dans rock-paper-scissors.py
    # L'utilisateur saisira son mouvement (pierre/papier/ciseaux),
    jeu=Game()
    user_item = jeu.get_user_item("Select ? (r)ock/(p)aper/(s)cissors : ")
    print("You chose:", user_item)
    # et l'ordinateur sélectionnera au hasard soit une pierre, une feuille ou des ciseaux.
    computer_item=jeu.get_computer_item()
    print("The computer chose:", computer_item)
    # Nous comparerons ensuite le mouvement de l'utilisateur avec celui de l'ordinateur et déterminerons les résultats du jeu :
    print("Result:", jeu.get_game_result(user_item, computer_item) )

    #print() le choix de l'utilisateur, le choix de l'ordinateur et le résultat.

    # décide de quitter le programme,
    # nous imprimerons un résumé des résultats de toutes les parties :
    #    combien de fois il a gagné, perdu ou fait match nul contre l'ordinateur.

    print()
#EOF
