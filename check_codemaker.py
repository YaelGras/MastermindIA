#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import common

def check_codemaker(nom_fichier):
    
    combinaisons = []
    evaluations = []
    ligne_est_combinaison = True
    
    with open(nom_fichier, 'r') as f:
        for line in f:
            if ligne_est_combinaison:
                combinaisons.append(line[:-1])
                ligne_est_combinaison = False
            else:
                evaluations.append(tuple([int(line[0]),int(line[2])]))
                ligne_est_combinaison = True
    
    if evaluations[-1] != (4,0):
        print('Le codebreaker n\'a pas trouve la solution donc le codemaker a probablement triche.')
        return False
    
    solution = combinaisons[-1]
    nb_tour = len(combinaisons)
    a_triche = False
    for i in range(0, nb_tour):
        if common.evaluation(combinaisons[i], solution) != evaluations[i]:
            a_triche = True
    
    if a_triche:
        print('Le codemaker a visiblement triché !')
    else:
        print('Il semblerait que le codemaker n\'ait pas triche.')
    return a_triche
            
check_codemaker('test_log.txt')
