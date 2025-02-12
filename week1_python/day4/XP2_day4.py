#!/usr/bin/python


# $mkdir tools_pets, put the file XP_day3.py into ./tools_pets
# execution : $python XP2_day3.py

# importez classe Dog
from tools_pets import XP_day4
import random


if __name__ == "__main__":
    # Exo1
    print("Exo3")
    #instanciation
    #toutou1=XP_day4.Dog("snoupi", 5,15)

    # PetDog qui hérite de Dog
    class PetDog(XP_day4.Dog):
        def __init__(self, dog_name, dog_age, dog_weight, petdog_trained=False): # False par défaut
            super().__init__(dog_name, dog_age, dog_weight) # j'appelle le init de la classe mere (Dog)
            self.trained=petdog_trained # Ajoutez un attribut appelé trained

        # Ajoutez les méthodes
        # train: print la sortie de bark() et déclare le booléen 'trained' à True
        def train(self):
            print(f"{self.bark()}") # print la sortie de bark() de Dog(la mère)
            self.trained=True # déclare le booléen 'trained' à True
            return
        # prend un paramètre dont la valeur est quelques noms d'autres Dog (utilisez *args ).
        # La méthode doit afficher la chaîne suivante : « dog_names tous jouent ensemble ».
        def play(self, *args):
            print(f"{args} all play together")
            #print(f"({args[0]}, {args[1]}, {args[2]},...) all play together")
            return
        #imprimer l'une des phrases
        def do_a_trick(self):
            nb=random.randint(1,4) # une des 4 phrases au hasard
            phrase={1:f"{self.name} does a barrel roll",
                    2:f"{self.name} stands on his back legs",
                    3:f"{self.name} shakes your hand",
                    4:f"{self.name} plays dead",
            }
            if self.trained:
                print(phrase[nb]) # nb random
            else:
                print("dog is not trained")
            return

    petdog_newdog=PetDog("snoupi_fille", 1, 5) # self.trained=False par défaut
    petdog_newdog.play("dog1","dog2","dog3","dog4")
    petdog_newdog.do_a_trick() # self.trained=False par défaut

    print()
    petdog_newdog.train() # self.trained=True
    petdog_newdog.do_a_trick()

    # Exo4
    print("\nExo4")

    # Exo5
    print("\nExo5")

    print()
#EOF
