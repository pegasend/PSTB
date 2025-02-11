#!/usr/bin/python
# execution : $>python daily_challenge_day3.py

if __name__ == "__main__":
    # Challenge#1

    # Écrivez un programme qui crée un dictionnaire. Ce dictionnaire stocke les index de chaque élément
    # Demandez un mot à un utilisateur
    s=input("donner un mot de plusieurs lettres? ")

    # Assurez-vous que les lettres sont les keys => Ce dictionnaire stocke les index de chaque élément letter { 'letter':[] }
    # => for l in s

    # stocke les index de chaque élément letterdans une liste.
    #     Assurez-vous que les index sont stockés dans un fichier list, et que ces listes sont des values
    #     => [1e position de la lettre, 2e  position de la lettre] => [pos for pos in range(len(s) ) if s.startswith(l, pos)]
    #             if s.startswith(l, pos) => donne la(les) position(s) si la lettre est dans la chaine s
    print({l:[pos for pos in range(len(s) ) if s.startswith(l, pos)] for l in s})

    print()

#EOF
