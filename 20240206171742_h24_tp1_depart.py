import os
import csv
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

NOM_ÉTUDIANT = "Leduc, Benjamin" # Écrivez votre nom et prénom ici
GROUPE_ÉTUDIANT = ""         # Écrivez votre groupe ici.



# Objectif :
# Vous avez un fichier csv : "resultats_evaluation.csv". Il s'agit de résultats d'évaluations d'étudiants.
# On veut que vous en extrayiez l'information.
# Que vous faisiez des calculs pour faire une analyse statistique.
# Puis que vous transformiez les résultats obtenus en un dictionnaire.


###################################################################
##                          Partie 1                            ###
###################################################################

# Vous devez lire et extraire les informations du csv "resultats_evaluation.csv"
# Le format de ce csv ne permet pas d'extraire les données très facilement. Regardez-le avant de commencer.

# Ce csv contient 20 étudiants, chaque ligne correspondant à l'ID unique de l'étudiant, son nom, son programme, et le résultat de 8 évaluations. 5 Tps et 3 examens.

# Le but de cette partie est d'obtenir une liste qui contient chacune des valeurs du csv.
# MAIS, nous n'avons pas besoin du nom de l'étudiant ou du programme.

liste_étudiants = []

with open ('resultats_evaluation.csv', 'r') as files:
    lecteur = csv.reader(files, delimiter=";")
    next(lecteur)
    next(lecteur)
    for line in lecteur:
        lecteur = [line[0]]
        lecteur.extend(line[3:])
        liste_étudiants.append(lecteur)

print(liste_étudiants)


# À la fin de cette partie. "liste_etudiants" doit contenir toutes la valeurs des étudiants. Sauf le nom et le programme de l'étudiant



###################################################################
##                          Partie 2                            ###
###################################################################

# On veut savoir le nombre d'étudiants ayant passé le cours ainsi que la moyenne de ceux ayant passé le cours.
# À partir de la "liste_etudiants" produite dans la partie 1, passé au travers et prenez note du nombre d'étudiants ayant passé et de leur note finale.
# Le cours est à double seuil, un étudiant doit avoir une moyenne de 60% ou plus dans la partie TPs AINSI qu'une moyenne de 60% ou plus dans la partie examen.
#       SI UN ÉTUDIANT À MOINS DE 60% dans une des deux parties, ca note final ne peut pas être supérieur à la note dans cette partie.

# À la fin de cette partie, on veut imprimer : 
#           - Le nombre d'étudiants ayant passé.
#           - La moyenne de ces étudiants
#           - La moyenne de tous les étudiants
#           - Le taux de succès au cours (pourcentage d'étudiants ayant passé)


# Variable
note_finale = 0 
moyennes_étudiants = 0
moyennes_passés = 0
étudiant_passés = 0
taux_succès = 0
dictionnaire = []

for étudiant in liste_étudiants:
    moyenne_tp = 0
    moyenne_examen = 0
    note_étudiant = 0
# Calcul de la moyenne des TPs d'un étudiant.
    for note_tp in étudiant [1:6]:
        moyenne_tp += int(note_tp)/5

# Calcul de la moyenne des examens d'un étudiant.
    for note_exam in étudiant[6:9]:
        moyenne_examen += int(note_exam)/3

# Vérification du double seuil de 60% et calcul du nombre d'étudiants ayant passé le cours.
    if moyenne_tp >= 60 and moyenne_examen >= 60 :
        étudiant_passés +=1
        
        moyennes_étudiants += ((moyenne_examen + moyenne_tp) /2)
        moyennes_passés = moyennes_étudiants / étudiant_passés

# Calcul des notes
    note_finale += ((moyenne_examen + moyenne_tp) /2) / len(liste_étudiants)
    note_étudiant = (moyenne_examen + moyenne_tp) /2
    taux_succès = (étudiant_passés /len(liste_étudiants)) *100 


# Arrondir les nombres
    note_étudiant_arr = round(note_étudiant,2)
    moyennes_passé_arr = round(moyennes_passés,2)
    note_finale_arr = round(note_finale,2)
    taux_succès_arr = round(taux_succès,2)

    dictionnaire.append({"ID": étudiant[0], "note": note_étudiant_arr, "échec": note_étudiant_arr < 60})


    
    
    
  

print(f"Le nombre d'étudiants ayant passé le cours est de : {étudiant_passés} étudiants")
print(f"La moyenne de ces étudiants est de : {moyennes_passé_arr}%")
print(f"La moyenne de tous les étudiants est de : {note_finale_arr}%")
print(f"Le taux de succès est de : {taux_succès_arr}%")
print(dictionnaire)





###################################################################
##                          Partie 3                            ###
###################################################################

# On veut créer une liste de dictionnaires à partir de la liste obtenue dans la partie 1.
# Pour chaque étudiant on veut 3 paires clefs-valeurs dans le dictionnaire :
#               "ID" : Le id de l'étudiant
#               "note" : La note finale de l'étudiant.
#               "echec" : Une booléenne ayant la valeur True si l'étudiant échoue. Sinon la valeur False.
#
# Une fois cette liste de dictionnaire obtenue, imprimez-la dans le terminal. 


#Je teste ce qui ne marche pas




