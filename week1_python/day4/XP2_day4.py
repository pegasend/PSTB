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
    class Family():
        def __init__(self, last_name:str, **kwargs):
            self.last_name=last_name
            self.members=[]
            for member in kwargs.items():# [dict{}]
                self.members.append(member)

        # Implémentez les méthodes suivantes :
        # born: ajoute un enfant à la liste des membres (utilisez **kwargs),
        # n'oubliez pas d'imprimer un message félicitant la famille.
        def born(self, **kwargs):#{key:value}
            l_name=[]
            for person in self.members:
                l_name.append(person['name'])

            if kwargs['name'] not in l_name:# ajout si n'existe pas deja
                self.members.append(
                    {'name':kwargs['name'],'age':kwargs['age'],'gender':kwargs['gender'],'is_child':kwargs['is_child']}
                )# append => list
                print("felicitation a la famille pour le nouveau jeune arrivant")#imprimer un message félicitant la famille
            else:
                print(f"cette personne {kwargs['name']} existe deja !")
            #print(self.members)
            return
        # is_18: prend le nom d'un membre de la famille comme paramètre et renvoie True s'il a plus de 18 ans et False sinon
        def is_18(self, nom):
            for person in self.members:
                #print(person)
                if person['name']==nom:
                    if person['age']>18:# renvoie True s'il a plus de 18 ans
                        return True
                    else:
                        return False
            print(f"{nom} n'existe pas dans la famille {self.last_name}")
            return

        # family_presentation:une méthode qui imprime le nom de famille et tous les détails des membres
        def family_presentation(self):
            print(f"\nVoici le detail de la famille {self.last_name}:")
            for member in self.members:# le nom de famille
                for detail in member.keys():
                    print(f"\t{detail}:{member[detail]}") # tous les détails des membres
                print()
            return

    # Créez une instance de la classe Family, avec le nom de famille de votre choix et les membres ci-dessous.
    # Appelez ensuite toutes les méthodes que vous avez créées au point 2.
    # exemple:
    #     [{'name':'Michael','age':35,'gender':'Male','is_child':False},
    #     {'name':'Sarah','age':32,'gender':'Female','is_child':False}]
    # init
    famille=Family("name_family",)
    famille.born(name='toto', age=0, gender='Male', is_child=True)# vient de naitre => age=0
    famille.born(name='Michael', age=35, gender='Male', is_child=True)
    famille.born(name='Sarah', age=32, gender='Female', is_child=False)

    assert famille.is_18("Sarah")==True

    famille.family_presentation()
    # Exo5
    print("\nExo5")
    class TheIncredibles(Family):
        def __init__(self, last_name:str,**kwargs):
            super().__init__(last_name, **kwargs)# init de la classe mere
            #self.members=[]
            #for member in kwargs.items():# [dict{}]
            #    self.members.append(member)
            #print("***", self.members)

        # cette méthode doit afficher la puissance d'un membre uniquement s'il a plus de 18 ans.
        # Sinon, déclenchez une exception (recherchez les exceptions) indiquant qu'il n'a pas plus de 18 ans.
        def use_power(self, nom):
            for person in self.members:
                print(person)
                if person['name']==nom:
                    if super().is_18(nom):# afficher la puissance s'il a plus de 18 ans
                        print()
                        #print(f"la puissance de {nom} est:", person[super().power])
                    else:
                        # déclenchez une exception
                        print("il n'a pas plus de 18 ans")
            #print(f"{nom} n'existe pas dans la famille {super().last_name}")
            return

        # Ajoutez une méthode appelée incredible_presentation qui :
        def incredible_presentation(self):
            print("*Voici notre puissante famille **")
            # utilisez la fonction super() pour appeler la family_presentation()
            super().family_presentation()# Imprime le nom de famille et tous les détails des membres
            return

    # Créez une instance de la classe Indestructibles, avec le nom de famille « Indestructibles »
    f_TheIncredibles=TheIncredibles("name_Incredible")
    #Créez des membres de cet même instance
    f_TheIncredibles.born(name='Michael', age=35, gender='Male', is_child=True, power='fly',incredible_name='MikeFly')
    f_TheIncredibles.born(name='Sarah', age=32, gender='Female', is_child=False, power='read minds',incredible_name='SuperWoman')

    f_TheIncredibles.use_power("Sarah")
    print()
    # Appelez la incredible_presentation
    f_TheIncredibles.incredible_presentation()

    # Utilisez la fct born() héritée de la Family pour ajouter Baby Jack avec la puissance suivante : « Unknown Power ».
    f_TheIncredibles.born(name='Baby Jack', age=45, gender='Male', is_child=False, power='Unknown Power',incredible_name='MikeFly')

    # Appelez à nouveau incredible_presentation()
    f_TheIncredibles.incredible_presentation()
    print()
#EOF
