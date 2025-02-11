#!/usr/bin/python
# execution : $python XP_day2.py

if __name__ == "__main__":
    # Exo1
    print("Exo1")
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    print("Convertissez les deux listes suivantes en dictionnaires\n", dict(zip(keys, values) ) )

    # Exo2
    print("\nExo2")
    #family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
    # bonus
    print("donner 4 noms et ages sous la forme:")
    family={}
    for i in range(4):
        nom,age=input("nom,age? ").split(",")
        if len(nom)*len(age)==0:
            print("valeur manquante, merci de recommancer")
            exit(0)
        else:
            family[nom]=int(age)
    print("\nvoici le dico de la famille que vous avez tapez:",family)
    print()
    tot=0
    for k in family.keys():
        #print(k, family[k])
        #si age<3 ans    => gratuit.
        if family[k]<=3:
            print(f"{k} doit rien payer: gratuit pour les jeunes", )
        #si 3<age<12 ans => 10$
        elif 3<family[k]<12:
            print(f"{k} doit payer: 10$")
            tot += 10
        #si age>=12 ans  => 15 $.
        else:
            print(f"{k} doit payer: 15$")
            tot += 15

    print("\ncoût total des films pour la famille:",tot,"$")

    #Exo3
    print("\nExo3")
    brand={'name': 'Zara',
           'creation_date': 1975,
           'creator_name': ['Amancio', 'Ortega', 'Gaona'],
           'number_stores': 7000,
           'type_of_clotheset':['men', 'women', 'children', 'home'],
            'international_competitors':['Gap', 'H&M', 'Benetton'],
            'major_colord':{ 'France': 'blue', 'Spain': 'red', 'US': ['pink', 'green']},
    }
    # 2. Modifiez le nombre de magasins à 2.
    brand['number_stores']=2
    print()
    # 3. Utilisez la clé [type_of_clothes] pour imprimer une phrase qui explique qui sont les clients de Zara.brand['name']
    print(f"les clients de {brand['name']} sont des {brand['type_of_clotheset'][0]}, des {brand['type_of_clotheset'][1]}"+
          f" et des {brand['type_of_clotheset'][2]} ou pour le {brand['type_of_clotheset'][3]}")
    print()

    # 4. Ajoutez une clé appelée country_creation avec une valeur de Espagne.
    brand['country_creation']='Espagne'
    print(brand)
    print()
    # 5. Vérifiez si la clé international_competitors est dans le dictionnaire. Si c'est le cas, ajoutez le magasin Desigual.
    if 'international_competitors' in brand.keys():
          brand['international_competitors'].append('Desigual')

    # 6. Supprimez les informations sur la date de création.
    brand.pop('creation_date')

    # 7. Imprimez le dernier concurrent international.
    print("dernier concurrent international:", brand['international_competitors'][-1])

    # 8. Imprimez les principales couleurs de vêtements aux États-Unis.
    print("colors in US:", brand['major_colord']['US'])

    # 9. Imprimez le nombre de paires clé-valeur (c'est-à-dire la longueur du dictionnaire).
    print("len(brand)=", len(brand) )
    print()
    # 10. Imprimez les clés du dictionnaire.
    print("clé du dico Brand:\n", brand.keys() )

    # 11. Créez un autre dictionnaire appelé more_on_zara avec les détails suivants :
    # - creation_date: 1975
    # - number_stores: 10 000
    more_on_zara={'creation_date': 1975, 'number_stores': 10000}
    print()
    # 12. Utilisez une méthode pour ajouter les informations du dictionnaire more_on_zara au dictionnaire brand.
    brand.update(more_on_zara)

    # 13. Imprimez la valeur de la clé number_stores. Que vient-il de se passer ?
    print("number_stores=", brand['number_stores']," MAJ suite à l'update()")

    # Exo4
    print("\nExo4")
    def describe_city(city, country="Iceland"):
        # # La fonction doit imprimer une phrase simple, telle que « city est dans country».
        print(f"{city} est dans la région {country}")
        return

    # Appelez votre fonction.
    describe_city("Reykjavik")
    describe_city("Paris", "Ile de France")

    print("\nExo5")
    # Créez une fonction qui accepte un nombre entre 1 et 100
    # et génère un autre nombre aléatoirement entre 1 et 100. Utilisez le random module.
    import random
    def nb_aleatoire(n1):
        n2=random.randint(1, 100)
        if n1==n2:
            print(f"({n1})==({n2}), bravo")
        else:
            print("les 2 nombres ne sont pas egaux:", n1," et",n2)
        return

    n=int(input("donner un numbre entre 1 et 100? "))
    if 1<=n<=100:
        nb_aleatoire(n)
    else:
        print("recommencer avec nombre correct")
    # Comparez les deux nombres, si c'est le même nombre, affichez un success message,
    # sinon affichez un fail message et display both numbers.

    print("\nExo6")
    # Écrivez une fonction appelée make_shirt()
    # Modifiez la fonction make_shirt() pour que les chemises soient grandes par défaut + avec un message indiquant « J'aime Python » par défaut.
    #def make_shirt(size:str, text:str):
    def make_shirt(size="grande", text="J'aime Python"):
        if size=="grande":
            print(text)
        else:
            # La fonction doit imprimer une phrase résumant la taille de la chemise et le message imprimé dessus:
            print(f"La taille de la chemise est {size} et le texte est '{text}'")

        return

    # Appelez la fonction make_shirt()
    make_shirt("petite", "mon message imprime")
    # Appelez la fonction, afin de créer une grande chemise avec le message par défaut
    make_shirt()

    # Créer une chemise moyenne avec le message par défaut
    make_shirt("moyenne")

    # Créez une chemise de n’importe quelle taille avec un message différent.
    make_shirt("de n'importe quelle taille", "message different")
    print()
    # Bonus : appelez make_shirt() en utilisant des arguments de mots-clés(keyword arguments:affectation lors de l'appel).
    make_shirt(size='large', text='message2')

    ####################################
    print("\nExo7")
    import random

    # Créez une fonction appelée get_random_temp()
    # Ajoutez un paramètre à la fonction, nommé « saison ».
    #def get_random_temp():
    def get_random_temp(saison:str):
        if saison=='hiver':
            return random.randint(-10, 16)#si la saison est « hiver », les températures ne devraient tomber qu'entre -10 et 16
        else:
            return random.randint(-10, 40)# renvoyer un entier compris entre -10 et 40 degrés (Celsius), sélectionné au hasard

    # Testez votre fonction pour vous assurer qu'elle génère les résultats escomptés.
    #print(get_random_temp() )

    # Bonus : donnez la température sous forme de nombre à virgule flottante au lieu d'un entier.
    def get_random_temp2(saison:str):
        if saison=='hiver':
            return random.uniform(-10, 16)#si la saison est « hiver », les températures float ne devraient etre entre -10 et 16
        else:
            return random.uniform(-10, 40)# renvoyer un float compris entre -10 et 40 degrés (Celsius), sélectionné au hasard

    # Créez une fonction appelée main().
    def main(saison1):
        # appelez get_random_temp()pour obtenir une température et stockez sa valeur dans une variable.
        t=get_random_temp(saison1) # # Utilisez la saison comme argument lors de l'appel get_random_temp().
        t2=get_random_temp2(saison1)

        # Informez l'utilisateur, par exemple : « La température actuelle est de 32 degrés Celsius. »
        print(f"La temperature actuelle est de {t} degrés Celsius")

        # Ajoutons plus de fonctionnalités à la fonction main().
        # Écrivez quelques conseils amicaux concernant la température :
        if t<0:
            print("Brrr, il fait un froid glacial ! Portez des couches supplementaires aujourd'hui")
        elif 0<=t<16 :
            print("Il fait plutôt froid ! N'oubliez pas votre manteau")
        elif 16<=t<23:
            print("cela commence a etre agreable")
        elif 23<=t<32:
            print("chaud devant")
        else:
            print("trop chaud au dela de 32°c")

        print(f"\nLa temperature2 actuelle est de {t2:.3f} degrés Celsius")
        if t2<2:
            print("Brrr, il fait un froid glacial ! Portez des couches supplementaires aujourd'hui")
        elif 0<=t2<16:
            print("Il fait plutôt froid ! N'oubliez pas votre manteau")
        elif 16<=t2<23:
            print("cela commence a etre agreable")
        elif 23<=t2<32:
            print("chaud devant")
        else:
            print("trop chaud au dela de 32°c")

    # Créez une fonction appelée main2().
    # Bonus : Au lieu de demander la saison, demandez à l'utilisateur le numéro du mois
    def main2(saison1:int):
        if 3<=saison1<6:
            t=get_random_temp("primptemps")
        elif 6<=saison1<9:
            t=get_random_temp("ete")
        elif 9<=saison1<11:
            t=get_random_temp("automne")
        else:
            t=get_random_temp("hiver") # # Utilisez la saison comme argument lors de l'appel get_random_temp().

        # Informez l'utilisateur, par exemple : « La température actuelle est de 32 degrés Celsius. »
        print(f"La temperature actuelle est de {t} degrés Celsius")

        # Ajoutons plus de fonctionnalités à la fonction main().
        # Écrivez quelques conseils amicaux concernant la température :
        if t<0:
            print("Brrr, il fait un froid glacial ! Portez des couches supplementaires aujourd'hui")
        elif 0<=t<16 :
            print("Il fait plutot froid ! N'oubliez pas votre manteau")
        elif 16<=t<23:
            print("cela commence a etre agreable")
        elif 23<=t<32:
            print("chaud devant")
        else:
            print("trop chaud au dela de 32°c")

    # Demandez à l'utilisateur de saisir une saison
    ssaison=input("saisir une des 4 saisons (ete/automne/hiver/ou primptemps) svp? ")
    if len(ssaison)>0:
        main(ssaison)
    else:
        print("error, recommencer svp avec les choix prevus!")
    print()
    # Bonus : Au lieu de demander la saison, demandez à l'utilisateur le numéro du mois (1 = janvier, 12 = décembre).
    # Déterminez la saison en fonction du mois.
    ssaison3=int(input("saisir un mois des 4 saisons (entre 1 et 12) svp? ") )
    if 1<=ssaison3<=12:
        main2(ssaison3)
    else:
        print("error, recommencer svp avec les choix prevus!")

    ###############################
    print("\nExo8")
    # Ce projet permet aux utilisateurs de répondre à un quiz pour tester leurs connaissances sur Star Wars.
    # Le nombre de réponses correctes/incorrectes est comptabilisé et l'utilisateur reçoit différents messages en fonction de ses résultats au quiz.
    data = [
        {
            "question": "What is Baby Yoda's real name?",
            "answer": "Grogu"
        },
        {
            "question": "Where did Obi-Wan take Luke after his birth?",
            "answer": "Tatooine"
        },
        {
            "question": "What year did the first Star Wars movie come out?",
            "answer": "1977"
        },
        {
            "question": "Who built C-3PO?",
            "answer": "Anakin Skywalker"
        },
        {
            "question": "Anakin Skywalker grew up to be who?",
            "answer": "Darth Vader"
        },
        {
            "question": "What species is Chewbacca?",
            "answer": "Wookiee"
        }
    ]
    # Créez une fonction qui pose des questions à l'utilisateur et vérifie ses réponses.
    # Suivez le nombre de réponses correctes et incorrectes. Créez une liste de réponses incorrectes
    def print_question():
        correct=0
        l_erreur=[]
        l_bonne_reponse=[]
        l_question=[]
        for idx in range(len(data) ):
            rep=input(data[idx]['question']) # fonction qui pose des questions à l'utilisateur
            if rep.lower()==data[idx]['answer'].lower(): # vérifie ses réponses
                correct += 1 # Suivez le nombre de réponses correctes
            else:
                l_erreur.append(rep) # liste de réponses incorrectes
                l_bonne_reponse.append(data[idx]['answer'])
                l_question.append(data[idx]['question'])
        return l_question, l_erreur, l_bonne_reponse, correct

    def print_tot(l,n):
        print("\nnb de réponses correctes:", n)
        print("nb de réponses incorrectes:", len(l) )
        return

    print("Quizz StarWars")
    # Créer une fonction qui informe l'utilisateur de son nombre de réponses correctes/incorrectes
    l_questions, l_erreurs, l_bonne_reponse, corrects=print_question()
    print_tot(l_erreurs, corrects)

    # Bonus : affiche à l'utilisateur les questions auxquelles il a mal répondu, sa réponse et la bonne réponse.
    print("\nvoici le resultat et detail de mauvaises reponses:")
    print('==============')
    for i in range(len(l_erreurs) ):
        print("question:", l_questions[i])
        print("=> votre reponse:", l_erreurs[i])
        print("==> la bonne reponse:", l_bonne_reponse[i])
        print()

    # S'il a eu plus de 3 mauvaises réponses, demandez-lui de rejouer.
    if len(l_erreurs)>3:
        print("merci de refaire le quizz pour avoir plus de bonnes reponses !")
    else:
        print("Bravo, vous avez reussi le quizz")

    print()
#EOF
