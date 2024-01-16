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
    
    global solution
    solution = ''.join(common.choices(common.COLORS, common.LENGTH))
    # Pour une version encore plus triviale, on pourrait aussi utiliser solution = ''.join([common.COLORS[0] for i in range(common.LENGTH)])
    


def codemaker(attempt):
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument)
    """
    global solution
    global combinaisons_possibles
    
    #Dans le dictionnaire : 
    #on associe au tuple evaluation, la liste contenant la longueur de 
    #l'ensemble des combinaison possibles et une solution possible
    eval_tailleensemblepossible = {}
    
    
    for c in combinaisons_possibles:
        evaluation_p = common.evaluation(attempt, c)
        #Si l'evaluation a déjà été vu pour une combinaison précédente alors 
        #on ajoute 1 sur la longueur de l'ensemble des combinaison possible 
        #pour cette evaluation
        if evaluation_p in eval_tailleensemblepossible:
            eval_tailleensemblepossible[evaluation_p] += 1
        #sinon on ajoute cette evalutation dans le dictionnaire avec comme
        #taille de l'ensemble des combinaisons possible valant 1
        else : 
            eval_tailleensemblepossible[evaluation_p] = 1
    
    
    #on résupère la taille de l'ensemble le plus grand
    tmp = max([eval_tailleensemblepossible[i] for i in eval_tailleensemblepossible])
    #On récupère l'evaluation attaché à cet ensemble
    #Le 0 sert à que si il y a plusieurs possibilité on en récupère qu'une seule
    red, white = [k for (k, val) in eval_tailleensemblepossible.items() if (val == tmp)][0]
    
            
   
    #La solution est choisie, on retourne donc l'evaluation et on actualise les possibilité restante
    common.maj_possibles(combinaisons_possibles, attempt, (red, white))
    
    return (red, white)
