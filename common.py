#!/usr/bin/env python3

import random
import sys
import itertools

LENGTH = 4
#COLORS = ['A', 'B', 'C', 'D']
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']

combinaisons_possibles_debut = {}
eval_combi_solu = {}

def choices(e, n):
    """Renvoie une liste composée de n éléments tirés de e avec remise
    On pourrait utiliser random.choices, mais cette fonction n'est pas
    disponible dans les versions plus anciennes de Python
    """
    return [random.choice(e) for i in range(n)]

def choices_v2(e):
    return random.choice(e)

def evaluation(combinaison, reference):
    #On regarde si le tuple (combinaison, reference) a déjà été evalué
    global eval_combi_solu
    if (combinaison, reference) in eval_combi_solu:
        return eval_combi_solu[(combinaison, reference)]
    elif (reference, combinaison) in eval_combi_solu:
        return eval_combi_solu[(reference, combinaison)]
    
    red = 0
    white = 0
    plots_combinaison_restants = []
    plots_reference_restants = []
    longueur_combinaison = len(combinaison)
    
    for i in range(0, longueur_combinaison):
        if combinaison[i] == reference[i]:
            red += 1
        else:
            plots_combinaison_restants.append(combinaison[i])
            plots_reference_restants.append(reference[i])
    
    nb_plots_restants = len(plots_combinaison_restants)
    
    for i in range(0, nb_plots_restants):
        if plots_combinaison_restants[i] in plots_reference_restants:
            white += 1
            plots_reference_restants.remove(plots_combinaison_restants[i])
            
    eval_combi_solu[(combinaison, reference)] = (red, white)
    return (red, white)

def donner_possibles(combinaison, evaluation_p):
    
    global combinaisons_possibles_debut
    
    cle = str(LENGTH) + str(COLORS)
    if cle not in combinaisons_possibles_debut:
        combinaisons_possibles_debut[cle] = [''.join(i) for i in set(itertools.product(COLORS, repeat = LENGTH))]
    combinaisons_possibles = set()
    #On regarde chaque possibilité imaginable
    for c in combinaisons_possibles_debut[cle]:
        #Si la possibilité que l'on a choisis donne la même evaluation que la référence avec la combinaison proposé
        #Alors on l'ajoute dans l'ensemble des possibilité valide
        if evaluation(combinaison, c) == evaluation_p:
            combinaisons_possibles.add(c)
    #On renvoie l'ensemble des possibilités encore valide apres cette combinaison
    return combinaisons_possibles

def maj_possibles(combinaisons_possibles, combinaison, evaluation_p):
    
    combinaisons_possibles_update = set()
    for c in combinaisons_possibles:
        if evaluation(combinaison, c) == evaluation_p:
            combinaisons_possibles_update.add(c)
    
    combinaisons_possibles.intersection_update(combinaisons_possibles_update)











