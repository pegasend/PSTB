#!/usr/bin/python
# execution : $python XP_day3.py

if __name__ == "__main__":
    # Exo1
    class Cat:
        def __init__(self, cat_name, cat_age):
            self.name = cat_name
            self.age = cat_age

    #En dehors de la classe
    # créez une fonction qui trouve le chat le plus vieux et renvoie le chat.
    def plus_vieux(c1,c2,c3):
        c_max=max([int(c1.age),int(c2.age),int(c3.age)])
        for chat in [c1,c2,c3]:
            if chat.age==c_max:
                return chat
        return 0

    def print_name_age(self):
        print(f"le chat le plus age est {name} et a {age} ans")
        return

    print("Exo1")
    #Instanciez 3 Cat objets en utilisant le code fourni ci-dessus.
    mycat1=Cat('rominet1', 5)
    mycat2=Cat('rominet2', 10)
    mycat3=Cat('rominet3', 15)
    #print(mycat3.name, mycat3.age)

    #En dehors de la classe, créez une fonction qui trouve le chat le plus vieux et renvoie le chat associé
    chat_max=plus_vieux(mycat1, mycat2, mycat3)

    #Imprimez la chaîne suivante : « Le chat le plus âgé est <cat_name>, et a <cat_age>ans. ».
    # Utilisez la fonction précédemment créée
    print(f"le chat le plus age est ({chat_max.name}) et a {chat_max.age} ans")

    # Exo2
    print("\nExo2")
    # Créez une classe appelée Dog.
    class Dog:
        # créez une __init__méthode qui prend deux paramètres : name et height
        def __init__(self, dog_name, dog_height):
            self.name   = dog_name
            self.height = dog_height
        #bark qui imprime la chaîne « <dog_name> fait ouaf ! »
        def bark(self):
            print(f"({self.name}) fait wouaf!")
        #jump qui imprime la chaîne « <dog_name>saute <x>cm de haut ! » x est le height*2
        def jump(self):
            print(f"({self.name}) saute {self.height*2}cm de haut !")

    #En dehors de la classe, créez un objet appelé davids_dog.
    #Le nom de son chien est « Rex » et sa taille est de 50 cm.
    davids_dog=Dog('Rex', 50)

    #imprimez les détails de son chien (c'est-à-dire name et height)
    print(f"(davids_dog), le detail de son chien est ({davids_dog.name}) de taille {davids_dog.height}cm")
    #et appelez les méthodes barket jump.
    davids_dog.bark()
    davids_dog.jump()
    print()

    # Créez un objet appelé sarahs_dog. Le nom de son chien est « Teacup » et sa taille est de 20 cm.
    sarahs_dog=Dog('Teacup', 20)

    # Imprimez les détails de son chien (c'est-à-dire name et height)
    print(f"(sarahs_dog), le detail de son chien est ({sarahs_dog.name}) de taille {sarahs_dog.height}cm")
    #et appelez les méthodes barket jump.
    sarahs_dog.bark()
    sarahs_dog.jump()
    print()

    # Créez une instruction if en dehors de la classe pour vérifier quel chien est le plus grand.
    def verif_plus_grand(d1,d2):
        if d1.height>d2.height:
            return d1
        else:
            return d2

    # Imprimez le name du plus grand chien.
    print(f"le chien le plus grand entre ({davids_dog.name}) et ({sarahs_dog.name}) "+
          f"s'appelle ({verif_plus_grand(davids_dog, sarahs_dog).name })")

    # Exo3
    print("\nExo3")
    # classe appelée Song, elle affichera les paroles d'une chanson. Sa __init__()méthode a 2 arguments : self et lyrics(une liste)
    class Song:
        def __init__(self, lyrics=[]):# liste
            self.playlist=lyrics

        #méthode appelée sing_me_a_song qui imprime chaque élément lyrics sur sa propre ligne.
        def sing_me_a_song(self):
            for title in self.playlist:
                print(title)

    # Créez un objet de la Classe Song
    stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

    # appelez la méthode sing_me_a_song() de la Classe Song
    stairway.sing_me_a_song()

    # Exo4
    print("\nExo4")
    # Créez classe Zoo+méthode __init__paramètre: zoo_name.
    # instancie 2 attributs : animals(une liste vide) et name(le nom du zoo)
    class Zoo:
        def __init__(self, zoo_name):
            self.animals=[]
            self.name=zoo_name # nom du zoo

        # Créez une méthode add_animal() qui prend un paramètre new_animal
        # Cette méthode ajoute le new_animal à la liste animals tant qu'il n'y figure pas déjà.
        def add_animal(self, new_animal):
            if new_animal not in self.animals:
                self.animals.append(new_animal)

        # Créez une méthode appelée get_animals qui imprime tous les animaux du zoo.
        def get_animals(self):
            for i in range(len(self.animals) ):
                print(self.animals[i])

        # Créez une méthode appelée sell_animal qui prend un paramètre animal_sold.
        # Cette méthode supprime l'animal de la liste et bien sûr, l'animal doit exister dans la liste.
        def sell_animal(self, animal_sold):
            if animal_sold in self.animals:
                self.animals.remove(animal_sold)
            else:
                print(f"error, ({animal_sold}) n'existe pas dans {self.name}")

        # Créez une méthode appelée sort_animals qui trie les animaux par ordre alphabétique
        # et les regroupe en fonction de leur première lettre.
        # dico{clé, value} => clé alphabétique, value=list[name1, name2] avec 1ère lettre de la clé
        def sort_animals(self):
            # tri ordre alphabétique, puis regroupe dans une liste sur 1ère lettre de chaque chaine
            l=self.animals.copy()
            # sorted(set([w[0] for w in l]) ) => liste triée selon la 1ère lettre de chaque animal de la liste du zoo
            dico_animal_sorted={c:[w for w in l if w.lower().startswith(c.lower() )] \
                                                                        for c in sorted(set([w[0].upper() for w in l]) )}
            #print(f"regroupement des animaux du zoo({self.name}):\n", dico_animal_sorted)
            return dico_animal_sorted

        # Créez une méthode appelée get_groups qui imprime l’animal/les animaux à l’intérieur de chaque groupe
        # groupe 'grp'
        #def get_groups(self, ddico_animal_sorted):
        def get_groups(self):
            g=input("donner le groupe (lettre?) a afficher svp? ").upper()
            #d=ddico_animal_sorted[g]
            d=self.sort_animals()[g] # récupère le regroupement en dico et extrait la liste selon le groupe (lettre?)
            if len(d)>1: # liste de plusieurs animaux
                print(f"Voici les animaux a l'interieur du groupe ({g}):\n", d)
            else: # sinon
                print(f"Voici l’animal à l'interieur du groupe ({g}):\n", d[0])

    # Créez un objet appelé ramat_gan_safari
    #     Astuce : C'est le gardien du zoo qui utilisera cette classe.
    ramat_gan_safari=Zoo('le safari')

    # appelez toutes les méthodes avec ramat_gan_safari => add_animal()
    print("### initialisation...")
    ramat_gan_safari.add_animal('cat')
    ramat_gan_safari.add_animal('baboon')
    ramat_gan_safari.add_animal('Ape')
    ramat_gan_safari.add_animal('eel')
    ramat_gan_safari.add_animal('bear')
    ramat_gan_safari.add_animal('cougar')
    ramat_gan_safari.add_animal('girafe')
    ramat_gan_safari.add_animal('emu')
    ramat_gan_safari.add_animal('dog')

    # appelez toutes les méthodes avec ramat_gan_safari => get_animals() => all
    print("\n### methode get_animals()...")
    ramat_gan_safari.get_animals()

    # appelez toutes les méthodes avec ramat_gan_safari => sell_animal() => del
    print("\n### methode sell_animal(animal_sold)...")
    ramat_gan_safari.sell_animal('toto')
    ramat_gan_safari.sell_animal('dog')
    print("\n### methode get_animals()...")
    ramat_gan_safari.get_animals()

    # appelez toutes les méthodes avec ramat_gan_safari => sort_animals()
    print("\n### methode sort_animals()...")
    #dico_animals=ramat_gan_safari.sort_animals()
    ramat_gan_safari.sort_animals()

    # appelez toutes les méthodes avec ramat_gan_safari => get_groups()
    print("\n### methode get_groups()...")
    #ramat_gan_safari.get_groups(dico_animals)
    ramat_gan_safari.get_groups()
    print()
#EOF
