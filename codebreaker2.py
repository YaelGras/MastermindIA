#!/usr/bin/env python3

import common
import itertools

combinaisons_possibles_debut = {}

def init():
    
    global combinaisons_possibles_debut
    global combinaisons_possibles
    
    cle = str(common.LENGTH) + str(common.COLORS)
    if cle not in combinaisons_possibles_debut:
        combinaisons_possibles_debut[cle] = [''.join(i) for i in set(itertools.product(common.COLORS, repeat = common.LENGTH))]
    combinaisons_possibles = set(combinaisons_possibles_debut[cle].copy())
    return


def codebreaker(evaluation_p):
    """
    L'argument evaluation_p est l'évaluation qu'on reçoit pour la dernière
    combinaison qu'on a proposée (et vaut None si c'est le premier coup de la
    partie).
    """
    
    global combinaisons_possibles
    global combinaison_testee
    #Si aucune proposition n'a encore été faite nous faisons un choix au hasard
    if evaluation_p == None:
        combinaison_testee = common.choices_v2(list(combinaisons_possibles))
        return combinaison_testee
    #Sinon on choisit parmis les possibilité restante
    #On commence par mettre a jour la liste des possibilité avec l'evaluation de la dernière proposition
    common.maj_possibles(combinaisons_possibles, combinaison_testee, evaluation_p)
    #Puis on choisit dans cette liste, on enregistre cette valeur car on en aura 
    #possiblement besoin au prochain appel de codebreaker
    combinaison_testee = common.choices_v2(list(combinaisons_possibles))
    return combinaison_testee
