#!/usr/bin/python

# disposition des fichiers : ./exam.py, ./data/congrats.7z et ./tools/utils.py
# execution : $>python exam.py

# Assurez-vous que Python 3.x est installé.
# Environment Variables : “Path” under “System variables,” add C:\Program Files\7-Zip\
# Doc : https://realpython.com/python-subprocess/

import os
from tools.utils import unzip_with_7z # ./tools/utils.py

zip_path="./data/"
zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is
dest_file = "./congrats.png" # À l'intérieur de 'congrats.7z' se trouve un fichier image

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------

# déchiffrer ? le mot de passe d'un fichier d'archive 7z sécurisé nommé congrats.7z.
# Vous recherchez deux lettres minuscules manquantes qui complètent le mot de passe.

if __name__ == "__main__":
    # RAZ
    if os.path.isfile(dest_file):
        os.remove(dest_file)

    # Vous recherchez 2 lettres minuscules manquantes qui complètent le mot de passe.
    for l1 in "abcdefghijklmnopqrstuyz":     # 1ère lettre du password en minuscule
        for l2 in "abcdefghijklmnopqrstuyz": # 2ème lettre du password en minuscule
            find_me=l1+l2
            secret_password = find_me + 'bcmpda'#plusieurs reprises de mots de passe différents(2 lettres manquantes qui complètent password) jusqu'à ce que vous trouviez

            # Cette fonction tente de décompresser un fichier 7z donné à l'aide d'un mot de passe.
            # elle retournera False si la décompression a échoué sinon True
            # Appelez cette fonction à plusieurs reprises avec des mots de passe différents jusqu'à ce que vous trouviez celui qui renvoie True.
            # call(['C:\\Program Files\\7-Zip\\7z.exe', 'x', '-p'+secret_password, '-o'+'./', "./data/congrats.7z"])
            statut=unzip_with_7z(zip_path+zip_file_path, dest_path, secret_password)
            # zip_file_path  :Le chemin vers l'archive 7z.
            # dest_path      :Où le contenu sera extrait.
            # secret_password:Le mot de passe qui, selon vous, permettra de déchiffrer le fichier 7z.
            # Systèmes d'exploitation pris en charge : fonctionne sur macOS et Windows.

            if statut:
                print(f"le password est ({secret_password}) avec les 2 lettres ({find_me}) et la fonction 'unzip_with_7z()' retourne alors un statut=({statut})")
                exit() # arret des 2 boucles for, si le password est trouvé

    # EOF
