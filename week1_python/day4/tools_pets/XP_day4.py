#!/usr/bin/python
# execution : $python XP_day3.py

#if __name__ == "__main__":
    # Exo1
print("Exo1")
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk() )

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Créez une autre race de chat nommée Siamese qui hérite de la Cat
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# instancier 3 types de Chat
cat_b, cat_c, cat_s=(Bengal("name_bengal",10), Chartreux("name_chartreux",20), Siamese("name_siamois",30) )

# Créez une liste appelée all_cats, qui contient trois instances de chat : un Bengal, un Chartreux et un Siamois
all_cats=[cat_b, cat_c, cat_s]

#for k,v in enumerate(['bengal','chartreux','siamois']):
#    print(f"check instances {k}:", all_cats[i].sing(v) )
#print()

# Ces trois chats sont les animaux de compagnie de Sara.
#Créez une variable appelée sara_pets dont la valeur est une instance de la classe Pets
#et transmettez la variable all_cats à la nouvelle instance.
sara_pets=Pets(all_cats)

# Emmenez tous les chats en promenade, utilisez la walk méthode.
sara_pets.walk()

# Exo2
print("\nExo2")
class Dog():
    def __init__(self, name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    # Implémentez les méthodes suivantes dans la classe Dog :
    # bark: renvoie une chaîne qui indique : « <dog_name> is barking »
    def bark(self):
        return f"{self.name} is barking"

    # run_speed: renvoie la vitesse de course du chien (weight/age*10)
    def run_speed(self):
        return self.weight/self.age*10

    # fight() appel run_speed()
    # fight: prend un paramètre dont la valeur est une autre instance Dog, appelée other_dog.
    # Cette méthode renvoie une chaîne indiquant quel chien a remporté le combat.
    # Le gagnant doit être le chien avec (run_speed x weight) le plus élevé .
    def fight(self, other_dog):
        if self.run_speed()*self.weight<other_dog.run_speed()*other_dog.weight:
            return f"the dog {other_dog.name} win !"
        else:
            return f"the dog {self.name} win !"

# Créez 3 chiens et faites-les courir dans votre classe.
#instanciation
toutou1=Dog("snoupi", 5,15)
toutou2=Dog("cookie", 10,30)
toutou3=Dog("max", 20,60)

print(toutou1.bark() )
print(f"vitesse: {toutou1.run_speed()} km/h")

print(f"{toutou1.name} vs {toutou2.name}:", toutou1.fight(toutou2) )
print(f"{toutou1.name} vs {toutou3.name}:", toutou1.fight(toutou3) )

print()
#EOF
