
# def inverser_chaine(chaine):
#     chaine_inversee = ''
#     for i in range(len(chaine)-1, -1, -1):
#         chaine_inversee += chaine[i]
#     return chaine_inversee

# print(inverser_chaine("Bonjour")) # Affiche "ruojnoB"

#2
# def somme_liste(liste):
#     somme = 0
#     for chiffre in liste:
#         somme += chiffre
#     return somme

# print(somme_liste([1, 2, 3, 4])) # Affiche 10

# #3
# def plus_grand_nombre(liste):
#     max_nombre = liste[0]
#     for nombre in liste:
#         if nombre > max_nombre:
#             max_nombre = nombre
#     return max_nombre

# print(plus_grand_nombre([3, 58, 11, 21])) # Affiche 58

#4
# def factorielle(n):
#     resultat = 1
#     for i in range(1, n + 1):
#         resultat *= i
#     return resultat

# print(factorielle(5)) # Affiche 120

# #5
# def est_palindrome(mot):
#     longueur = len(mot)
#     for i in range(0, longueur):
#         if mot[i] != mot[longueur-i-1]:
#             return False()
#     return True

# print(est_palindrome("radar")) # Affiche True

#6
# def compter_mots(phrase):
#     mots = phrase.split(' ')
#     return len(mots)

# print(compter_mots("Le test logiciel est essentiel")) # Affiche 5
