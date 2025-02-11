#!/usr/bin/python
# execution : $>python daily_challenge_day3.py

if __name__ == "__main__":
    # Challenge#1 in French !
    # Créez une classe appelée Farm. Comment doit-elle être implémentée ?
    class Farm:
        # La classe Farm a-t-elle besoin d'une __init__méthode ? Si oui, quels paramètres doit-elle accepter ?
        def __init__(self, Farm_name):
            self.animals=[] # ajout pour get_animal_types()
            self.name=Farm_name
            print(f"{self.name}'s farm\n")

        # De combien de méthodes la Farm a-t-elle besoin ? => 2 (avant le bonus !)
        # Avez-vous remarqué quelque chose d'intéressant dans la façon dont nous appelons la add_animal?
        # Quels paramètres cette fonction doit-elle avoir ? Combien de… ?
        def add_animal(self, new_animal, qte=2):
            if new_animal not in self.animals:
                self.animals.append(new_animal) # ajout pour get_animal_types()
            # Bonus : alignez soigneusement le texte en colonnes comme dans l'exemple ci-dessus. Utilisez le formatage de chaîne.
            print(f"{new_animal} : {qte}")
            return

        def get_info(self):
            return "\n\tE-I-E-I-0!"

        def get_animal_types(self): # Ajoutez une méthode
            # cette méthode doit renvoyer une liste triée de tous les types d'animaux (noms)
            return sorted([v for v in self.animals])

        def get_short_info(self): # Ajoutez une méthode
            # Cette méthode doit renvoyer : « La ferme McDonald's possède des vaches, des chèvres et des moutons. ».
            # La méthode doit appeler get_animal_types() pour obtenir une liste des animaux
            msg="La ferme McDonald's possede des"
            for v in self.get_animal_types():
                msg += " "+v+"s" # il faut ajouter un « s » à la fin du mot
            print(msg+'.')
            return

    # Testez votre code et assurez-vous d'obtenir les mêmes résultats que l'exemple ci-dessus.
    macdonald=Farm("McDonald")

    macdonald.add_animal('cow',5)
    macdonald.add_animal('sheep')
    macdonald.add_animal('sheep')
    macdonald.add_animal('goat', 12)
    print(macdonald.get_info() )

    print(macdonald.get_animal_types() ) # la liste devrait être : ['cow', 'goat', 'sheep'].
    macdonald.get_short_info()
    print()

#EOF
