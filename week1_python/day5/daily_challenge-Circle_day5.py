#!/usr/bin/python
# execution : $python daily_challenge-Circle_day5.py

# Les dunder méthodes
import math   # pour le nombre pi
import turtle # dessiner les cercles
#from circle import Circle

#créer une classe qui représente un cercle
# et spécifier soit le rayon, soit le diamètre
class Circle:
    def __init__(self, rayon=1.0):
        self.rayon=rayon

    # autres capacités d'une instance Cercle :

    # Calculer l'aire du cercle
    def get_aire(self):
        return math.pi*(self.rayon**2)

    # Attributs par name: spécifier soit le name=rayon , soit le name=diamètre
    # Dunder: pour gérer l'accès aux attributs il y a 2 méthodes
    # =>.__getattribute__(): s'exécute à chaque accès à un attribut, et
    # =>.__getattr__(): s'exécute uniquement si l'attribut cible n'existe pas dans l'objet actuel
    # enfin pour Imprimer les attributs, on utilisera __str__
    def __getattribute__(self, name): # attributs (rayon) du cercle - utiliser une dunder méthode
        print(f"__getattribute__ appele par {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name): #attributs (diametre) du cercle - utiliser une dunder méthode
        print(f"__getattr__ appele par {name}")
        if name=="diametre":
            return self.rayon*2# Diametre=2xrayon
        return super().__getattr__(name)

    def __str__(self): # string - utiliser une méthode dunder
        return f"le cercle avec un rayon de ({self.rayon})"

    # __add__ une dunder méthode
    def __add__(self, other):                       # Add pour 2 cercles
        return Circle(self.rayon + other.rayon)     # renvoyer un nouveau cercle avec le nouveau rayon
    # __eq__ une dunder méthode (==)
    def __eq__(self, other):                        # comparaison par '==' entre 2 cercles
        return self.rayon == other.rayon             # Comparaison de rayons
    # __lt__ une dunder méthode (<)
    def __lt__(self, other):                        # comparaison par '<' entre 2 cercles
        return self.rayon < other.rayon             # Comparaison de rayons

if __name__ == "__main__":
    # daily_challenge N°1
    print("challenge")
    # l'aire du cercle
    rrayon=1
    cercle=Circle(rrayon)
    print(f"l'aire du cercle d'un rayon ({rrayon}) est: {cercle.get_aire():.2f}")
    print()

    # Imprimer les attributs (rayon) du cercle - utiliser une dunder méthode
    rrayon=20
    #init
    cercle=Circle(rrayon)
    print(cercle)
    print()

    # dunder méthode, attribut rayon
    cercle=Circle(10)
    print(cercle.rayon)# __getattribute__ appelé par 'rayon'
    # __getattribute__ appele par 'radius'
    # 10
    print()
    # dunder méthode, attribut diamètre
    print(cercle.diametre)
    # __getattribute__ appele par 'diametre'
    # __getattr__ appele par 'diametre'
    # __getattribute__ appele par 'rayon'
    # 20
    print()

    # ajouter 2 cercles ensemble et de renvoyer un nouveau cercle avec le nouveau rayon - utiliser une dunder méthode
    print("somme de 2 cercles:")
    cercle1=Circle(20)
    cercle2= Circle(10)
    somme_cercle = cercle1 + cercle2# nouveau cercle avec le nouveau rayon
    print(somme_cercle)
    print()

    # comparaison de 2 cercles pour voir s'ils sont égaux, et de renvoyer un booléen- utiliser une dunder méthode
    print("egalite de 2 cercles:")
    print( cercle1==cercle2 ) # False car 5 différent de 10
    print()

    # comparaison de 2 cercles pour voir lequel est le plus grand et renvoyer un booléen - utiliser une dunder méthode
    print("difference de 2 cercles:")
    print( cercle1<cercle2 ) # True car 5<10
    print()

    # les mettre dans une liste et de les trier
    print("trier 3 cercles")
    # Polymorphisme
    cercle3= Circle(5)
    cercles_sorted_l='['
    for cercle in sorted([cercle3, cercle1, cercle2]): # tri
        cercles_sorted_l += f"{cercle}, "

    print("liste triee de 3 cercles:", cercles_sorted_l+']')
    print()

    # Bonus (non obligatoire) : Installez le module Turtle => pip install Turtle
    # et dessinez les cercles triés
    print("dessinez les cercles tries")
    couleurs={cercle3.rayon:'red', cercle2.rayon:'cyan', cercle1.rayon:'blue'} # une couleur différente selon la taille ou rayon de cercle à dessiner
    for c in sorted([cercle3, cercle1, cercle2], reverse=True): # trie decroissant
        # Set up the turtle screen and set the background color to white
        screen = turtle.Screen()
        screen.bgcolor("white")

        # Create a new turtle and set its speed to the fastest possible
        pen = turtle.Turtle()
        pen.speed(0)

        print(c.rayon)
        # Set the fill color to red
        pen.fillcolor(couleurs[c.rayon])
        pen.begin_fill()

        # Draw the circle with a radius of 100 pixels
        pen.circle(c.rayon*10)# 5=>50, 10=>100, 20=>200

        # End the fill
        pen.end_fill()
    #and stop drawing
    pen.hideturtle()

    # Keep the turtle window open until it is manually closed
    turtle.done()

#EOF
