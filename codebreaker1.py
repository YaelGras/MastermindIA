#!/usr/bin/env python3

import common
import itertools
import random

combinaisons_possibles_debut = {}

def init():
    
    global combinaisons_possibles_debut
    global combinaisons_possibles
    global i
    i=-1
    cle = str(common.LENGTH) + str(common.COLORS)
    if cle not in combinaisons_possibles_debut:
        combinaisons_possibles_debut[cle] = [''.join(i) for i in set(itertools.product(common.COLORS, repeat = common.LENGTH))]
    combinaisons_possibles = combinaisons_possibles_debut[cle].copy()
    random.shuffle(combinaisons_possibles)
    return


def codebreaker(evaluation_p):
    """
    L'argument evaluation_p est l'évaluation qu'on reçoit pour la dernière
    combinaison qu'on a proposée (et vaut None si c'est le premier coup de la
    partie).
    """
    global combinaisons_possibles
    global i
    i+=1
    return combinaisons_possibles[i]
