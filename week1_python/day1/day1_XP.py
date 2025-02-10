#!/usr/bin/python
# execution : $python day1_XP.py

# Exo1
for i in range(4):
    print("Hello world")

# Exo2
print("Exo2:", (99^3)*8 )

# Exo3
iinput=input("Exo3: nom? ")
if iinput=="dao":
    print("nom identique")
else:
    print("nom different!")

# Exo4
print()
iinput=int(input("Exo4: taille en centimetres? ") )
if iinput>145:
    print("suffisamment grands pour monter a bord")
else:
    print("doivent grandir encore un peu pour pouvoir monter !")

#exo5
print()
# créer un set={}
my_fav_numbers={1,5,15,30,40}
print("Exo5: ", my_fav_numbers)
# ajout
my_fav_numbers.update([-1,-5])
print("Exo5: ", my_fav_numbers)
# supprimer le dernier
my_fav_numbers.pop()
print("Exo5: ", my_fav_numbers)
# concatenation
friend_fav_numbers={0,2,8}
our_fav_numbers=set((*my_fav_numbers, *friend_fav_numbers))
print("Exo5:", our_fav_numbers)

# Exo6
#their contents cannot be changed after creation, also tuple allows us to add duplicate values.
#To append elements, we can create a new tuple that includes the original tuple and the new elements

# Exo7
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Supprimer Bananade de la liste.
basket.remove("Banana")
print("Exo7:", basket)

#Supprimer Blueberriesde la liste.
basket.pop(-1)
print("Exo7:", basket)

#Ajouter Kiwi à la fin de la liste.
basket.append('kiwi')
print("Exo7:", basket)

#Ajouter Apples au début de la liste.
basket.insert(0, 'Apples')
print("Exo7:", basket)

#Comptez combien de pommes il y a dans le basket.
print("Exo7:", basket.count("Apples") )

#Vider le basket.
basket.clear()
print("Exo7:", basket)

# Exo8
print()
sandwich_orders=["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# supprimer toutes les occurrences de Pastrami
i=0
list_temp=[]
while i<len(sandwich_orders):
    if sandwich_orders[i] != "Pastrami sandwich":
        list_temp.append(sandwich_orders[i])
    i += 1
sandwich_orders=list_temp

#sandwich_orders=[s for s in sandwich_orders if s != "Pastrami sandwich"]
print("Exo8-supprimer les occurrences de Pastrami sandwich:",sandwich_orders)

finished_sandwiches=[]
for i in range(len(sandwich_orders) ):
        finished_sandwiches.append(sandwich_orders.pop(0) )

#print(finished_sandwiches)
#print(sandwich_orders)
for s in finished_sandwiches:
    print("I made your",s)

#EOF

