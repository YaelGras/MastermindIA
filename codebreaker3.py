#!/usr/bin/env python3

import common
import itertools

combinaisons_possibles_debut = {}
ensemble_combinaison_a_testees_premier = {}

def init():
    
    global combinaisons_possibles_debut
    global combinaisons_non_testees
    global combinaisons_possibles
    global cle    
    
    cle = str(common.LENGTH) + str(common.COLORS)
    if cle not in combinaisons_possibles_debut:
        combinaisons_possibles_debut[cle] = [''.join(i) for i in set(itertools.product(common.COLORS, repeat = common.LENGTH))]
    combinaisons_possibles = set(combinaisons_possibles_debut[cle].copy())
    combinaisons_non_testees = combinaisons_possibles.copy()
    return 


def codebreaker(evaluation_p):
    """
    L'argument evaluation_p est l'évaluation qu'on reçoit pour la dernière
    combinaison qu'on a proposée (et vaut None si c'est le premier coup de la
    partie). 
    """
    global combinaisons_non_testees
    global combinaisons_possibles
    global ensemble_combinaison_a_testees_premier
    global combinaison_testee
    global cle 
    
    if evaluation_p != None:
        common.maj_possibles(combinaisons_possibles, combinaison_testee, evaluation_p)
        
    #Le premier tour donnera toujours les memes possibilité pour un lenght et un ensemble de COLORS unique
    #Cette partie est utile lorsque nous lançons un grand nombre de parties
    if evaluation_p == None : 
        if cle in ensemble_combinaison_a_testees_premier:
            combinaisons_interessantes = ensemble_combinaison_a_testees_premier[cle]
            combinaison_testee = common.choices_v2(combinaisons_interessantes)
            combinaisons_non_testees.remove(combinaison_testee)
            return combinaison_testee
        
    taillemeilleurchoix = len(combinaisons_possibles_debut[cle])
    #ensemble des combinaison ayant le meilleur rendement
    combinaisons_a_testee = set()
    
    for cTestee in combinaisons_non_testees: 
        
        eval_tailleensemblepossible = {}
        
        for cSolution in combinaisons_possibles:
            evaluation_tmp = common.evaluation(cTestee, cSolution)
            #Si l'evaluation a déjà été vu pour une combinaison précédente alors 
            #on ajoute 1 sur la longueur de l'ensemble des solutions possible 
            #pour cette evaluation
            if evaluation_tmp in eval_tailleensemblepossible:
                eval_tailleensemblepossible[evaluation_tmp] += 1
            #sinon on ajoute cette evalutation dans le dictionnaire avec comme
            #taille de l'ensemble des solution possible valant 1.
            else : 
                eval_tailleensemblepossible[evaluation_tmp] = 1 
            
        #Le pire cas est l'ensemble le plus grand
        taillepirecas = max([eval_tailleensemblepossible[i] for i in eval_tailleensemblepossible])
        
        #Si l'ensemble le plus grand est plus petit que le meilleur ensemble alors c'est qu'il est mieux que celui-ci
        if taillepirecas < taillemeilleurchoix:
            taillemeilleurchoix = taillepirecas
            combinaisons_a_testee = set()
            combinaisons_a_testee.add(cTestee)
            
        #Si l'ensemble le plus grand est égal au meilleur ensemble alors on enregistre la combinaison à tester car elle est aussi optimale
        elif taillepirecas == taillemeilleurchoix:
            combinaisons_a_testee.add(cTestee)
            
    combinaisons_interessantes = list(combinaisons_possibles.intersection(combinaisons_a_testee))
    
    #Nous enregistrons les combinaisons intéréssantes du premier tour pour que les parties suivantes n'aient pas à les recalculer
    if evaluation_p == None: 
        ensemble_combinaison_a_testees_premier[cle] = combinaisons_interessantes   
        
    #Nous sélectionnons si elle existe une combinaison possible et optimale
    if len(combinaisons_interessantes) != 0:
        combinaison_testee = common.choices_v2(combinaisons_interessantes)
        combinaisons_non_testees.remove(combinaison_testee)
        return combinaison_testee
    
    #Nous sélectionnons une combinaison impossible mais qui va nous apporter plus d'informations qu'une combinaison possible
    else:  
        combinaison_testee = common.choices_v2(list(combinaisons_a_testee))
        combinaisons_non_testees.remove(combinaison_testee)
        return combinaison_testee
