#!/usr/bin/env python3

import common


def play(codemaker, codebreaker):
    """
    Fonction principale de ce programme :
    Fait jouer ensemble le codebreaker et le codemaker donnés en arguments
    """
    n_tries = 0
    codebreaker.init()
    codemaker.init()
    evaluation_p = None
    print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        attempt = codebreaker.codebreaker(evaluation_p)
        (red, white) = codemaker.codemaker(attempt)
        n_tries += 1
        print("Essai {} : {} ({},{})".format(n_tries, attempt, red, white))
        evaluation_p = (red, white)
        if red >= common.LENGTH:
            print("Bravo ! Trouvé {} en {} essais".format(attempt, n_tries))
            break
        
def play_log(codemaker, codebreaker, nom_fichier):
    """
    Reprend la fonction principale de ce programme mais en enregistrant les évaluations et les combinaisons essayées :
    Fait jouer ensemble le codebreaker et le codemaker donnés en arguments
    """
    
    with open(nom_fichier, 'w') as f:
        codebreaker.init()
        codemaker.init()
        evaluation_p = None
        while True:
            attempt = codebreaker.codebreaker(evaluation_p)
            f.write(attempt + '\n')
            (red, white) = codemaker.codemaker(attempt)
            f.write(str(red) + ',' + str(white) + '\n')
            evaluation_p = (red, white)
            if red >= common.LENGTH:
                break


def play_human_against_codemaker(codemaker):
    """
    Fait jouer l'utilisateur humain (au clavier) dans le role du codebreaker
    contre un codemaker donné en argument
    """
    n_tries = 0
    codemaker.init()
    evaluation_p = None
    print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        attempt = input("Saisir combinaison: ")  # On lit une combinaison au clavier au lieu d'appeler le codebreaker (qui sera donc joué par un humain)
        if len(attempt) != 4:
            print("Combinaison invalide (pas la bonne taille)")
            continue
        (red, white) = codemaker.codemaker(attempt)
        n_tries += 1
        print("Essai {} : {} ({},{})".format(n_tries, attempt, red, white))
        evaluation_p = (red, white)
        if red >= common.LENGTH:
            print("Bravo ! Trouvé {} en {} essais".format(attempt, n_tries))
            break


def play_human_against_codebreaker(codebreaker):
    """
    Fait jouer l'utilisateur humain (au clavier) dans le role du codemaker
    contre un codebreaker donné en argument
    """
    n_tries = 0
    codebreaker.init()
    evaluation_p = None
    print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        attempt = codebreaker.codebreaker(evaluation_p)
        print('Combinaison proposée: {}'.format(attempt))
        red = int(input('Saisir nombre de plots rouges: '))
        white = int(input('Saisir nombre de plots blancs: '))
        n_tries += 1
        print("Essai {} : {} ({},{})".format(n_tries, attempt, red, white))
        evaluation_p = (red, white)
        if red >= common.LENGTH:
            print("Le codebreaker a trouvé {} en {} essais".format(attempt, n_tries))
            break


# Les lignes suivantes sont à modifier / supprimer selon ce qu'on veut faire, quelques exemples :
"""
# Faire jouer ensemble codemaker0.py et codebreaker0.py pour 5 parties :
import codebreaker0
import codemaker0
for i in range(5):
    play(codemaker0, codebreaker0)
exit()
"""

"""
# Faire jouer un humain contre codemaker0.py :
import codemaker0
play_human_against_codemaker(codemaker0)
"""

"""
# Et plus tard, vous pourrez faire jouer vos nouvelles version du codebreaker et codemaker :
import codemaker1
play_human_against_codemaker(codemaker1)
"""

"""
# Faire jouer ensemble codemaker2.py et cobreaker2.py :
import codebreaker2
import codemaker2
play(codemaker2, codebreaker2)
"""

"""
# Faire jouer ensemble codemaker2.py et cobreaker2.py en enregistrant le détail de la partie :
import codebreaker2
import codemaker2
play_log(codemaker2, codebreaker2, 'test.txt')
"""

"""
# Autre façon de creer un log de partie sans écrasé les log précédant :
import codebreaker2
import codemaker2
import datetime
date = datetime.datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
play_log(codemaker2, codebreaker2, 'test{}.txt'.format(date))
"""
