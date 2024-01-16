#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
                  ATTENTION
VERIFIEZ LE NOMBRE DE PARTIES QUE VOUS VOULEZ 
   LANCER AVANT L'EXECUTION DU PROGRAMME
"""


import common
import codemaker1 
import codemaker2
import codebreaker0 
import codebreaker1
import codebreaker2
import codebreaker3
import matplotlib.pyplot as plt
import numpy as np

#Nous reprenons le code de la fonction play du fichier du meme nom, et on enleve les 
#print pour gagner de la rapidité d'exécution
def play(codemaker, codebreaker):
    """
    Fonction principale de ce programme :
    Fait jouer ensemble le codebreaker et le codemaker donnés en arguments
    """
    n_tries = 0
    codebreaker.init()
    codemaker.init()
    evaluation_p = None
    while True:
        attempt = codebreaker.codebreaker(evaluation_p)
        (red, white) = codemaker.codemaker(attempt)
        n_tries += 1
        
        evaluation_p = (red, white)
        if red >= common.LENGTH:
            return n_tries
            break
    
#%% Question 3 ================================================================

def afficher_histogramme_q3(nb_parties):
    resultats = []
    for i in range(nb_parties):
        resultats.append(play(codemaker1,codebreaker0))
    plt.figure()
    plt.hist(resultats, bins = 20, color = 'red', edgecolor = 'white', range = (0, max(resultats)))
    plt.title("Histogramme")
    plt.xlabel("Nombre d'essai")
    plt.ylabel("Nombre de parties")
    plt.show()
    print("La moyenne des valeurs de l'histogramme sur {} parties est {}".format(nb_parties, np.mean(resultats)))
    
#afficher_histogramme_q3(1000)
#L'esperance de cette méthode est de 8^4 = 4096 essais
    
#%% Question 4 ================================================================

def afficher_histogramme_q4(nb_parties):
    resultats = np.zeros((nb_parties,2))
    labels=["codebreaker0","codebreaker1"]
    for i in range(nb_parties):
        resultats[i,0]=play(codemaker1,codebreaker0)
        resultats[i,1]=play(codemaker1,codebreaker1)    
    plt.figure()
    #Affichage des histogrammes séparés et des moyennes
    plt.hist(resultats[:,0],#On prend que la première colonne de resultats qui contient les nb d'essais pour codebreaker0
             bins = 20, color = 'red', edgecolor = 'white', range = (0, max(resultats[:,0]))) #On définit la taille et la couleur des barres
    plt.title("Histogramme {}".format(labels[0]))
    plt.xlabel("Nombre d'essai")
    plt.ylabel("Nombre de parties")
    plt.show()
    print("La moyenne des valeurs de l'histogramme pour le {} sur {} parties est {}".format(labels[0],nb_parties, np.mean(resultats[:,0])))
    plt.hist(resultats[:,1], #On prend que la seconde colonne de resultats qui contient les nb d'essais pour codebreaker1
             bins = 20, color = 'blue', edgecolor = 'white', range = (0, max(resultats[:,1]))) #On paramètre le rendu visuelle
    plt.title("Histogramme {}".format(labels[1]))
    plt.xlabel("Nombre d'essai")
    plt.ylabel("Nombre de parties")
    plt.show()
    print("La moyenne des valeurs de l'histogramme pour le {} sur {} parties est {}".format(labels[1], nb_parties, np.mean(resultats[:,1])))
    #Affichage des histogrammes ensembles
    plt.hist(resultats, #Cette fois-ci, on prend l'array en entier pour afficher les deux, le hist détectera alors deux colonnes donc deux types de données
             bins=20, histtype='bar', color= ['red', 'blue'], #On paramètre le visuel en donnant une liste pour les fois où il faut différencier les données 
             label=labels)#On indique le nom pour la légende de chaque donnée
    plt.legend() #On affiche la légende
    plt.title('Histogrammes de {} et {}'.format(labels[0],labels[1]))
    plt.show()
    #Affichage du violin plot (un graphe proche de la boite à moustaches mais plus intéressant pour notre cas)
    plt.violinplot(resultats,
                   vert=False,  #On affiche horizontalement (pas vertivalement donc false pour vertical)
                   showmeans=True,showextrema=True) #On affiche la moyenne et les extremums sous forme de traits
    ax=plt.gca() #On récupère l'objet Axes courant
    #On travaille sur cette objet Axes pour pouvoir afficher sur l'ordonnée les noms des données en face des données concernées
    ax.set_yticks(np.arange(1, 3)) #On défini les positions sur l'axe des ordonnées où l'on va mettre nos indications
    ax.set_yticklabels(labels) #On indique ce que l'on met à ces positions
    plt.xlabel("Nombre d'essais")
    plt.title('Violin plot pour {} et {}'.format(labels[0],labels[1]))
    plt.show()
    
#afficher_histogramme_q4(1000)

#%% Question 7 ================================================================

def afficher_histogramme_q7(nb_parties):
    resultats = np.zeros((nb_parties,2))
    labels=["codebreaker1","codebreaker2"]
    for i in range(nb_parties):
        resultats[i,0]=play(codemaker1,codebreaker1)
        resultats[i,1]=play(codemaker1,codebreaker2)    
    plt.figure()
    #On applique le même affichage que la question 4
    #Affichage des histogrammes séparés et des moyennes
    plt.hist(resultats[:,0],bins = 20, color = 'red', edgecolor = 'white', range = (0, max(resultats[:,0]))) 
    plt.title("Histogramme {}".format(labels[0]))
    plt.xlabel("Nombre d'essai")
    plt.ylabel("Nombre de parties")
    plt.show()
    print("La moyenne des valeurs de l'histogramme pour le {} sur {} parties est {}".format(labels[0],nb_parties, np.mean(resultats[:,0])))
    plt.hist(resultats[:,1],bins = 20, color = 'blue', edgecolor = 'white', range = (0, max(resultats[:,1])))
    plt.title("Histogramme {}".format(labels[1]))
    plt.xlabel("Nombre d'essai")
    plt.ylabel("Nombre de parties")
    plt.show()
    print("La moyenne des valeurs de l'histogramme pour le {} sur {} parties est {}".format(labels[1], nb_parties, np.mean(resultats[:,1])))
    #Affichage des histogrammes ensembles
    plt.hist(resultats,bins=20, histtype='bar', color= ['red', 'blue'],label=labels)
    plt.legend() 
    plt.title('Histogrammes de {} et {}'.format(labels[0],labels[1]))
    plt.show()
    #Affichage du violin plot (un graphe proche de la boite à moustaches mais plus intéressant pour notre cas)
    plt.violinplot(resultats, vert=False,showmeans=True,showextrema=True) 
    ax=plt.gca()
    ax.set_yticks(np.arange(1, 3)) 
    ax.set_yticklabels(labels) 
    plt.xlabel("Nombre d'essais")
    plt.title('Violin plot pour {} et {}'.format(labels[0],labels[1]))
    plt.show() 

#afficher_histogramme_q7(100)

#%% Question 8 ================================================================

def afficher_histogramme_q8(nb_parties):
    resultats = np.zeros((nb_parties,2))
    labels=["codemaker1","codemaker2"]
    for i in range(nb_parties):
        resultats[i,0]=play(codemaker1,codebreaker2)
        resultats[i,1]=play(codemaker2,codebreaker2)    
    plt.figure()
    #On applique le même affichage que la question 4
    #Affichage des histogrammes séparés et des moyennes
    plt.hist(resultats[:,0],bins = 20, color = 'red', edgecolor = 'white', range = (0, max(resultats[:,0]))) 
    plt.title("Histogramme {}".format(labels[0]))
    plt.xlabel("Nombre d'essai")
    plt.ylabel("Nombre de parties")
    plt.show()
    print("La moyenne des valeurs de l'histogramme pour le {} sur {} parties est {}".format(labels[0],nb_parties, np.mean(resultats[:,0])))
    plt.hist(resultats[:,1],bins = 20, color = 'blue', edgecolor = 'white', range = (0, max(resultats[:,1])))
    plt.title("Histogramme {}".format(labels[1]))
    plt.xlabel("Nombre d'essai")
    plt.ylabel("Nombre de parties")
    plt.show()
    print("La moyenne des valeurs de l'histogramme pour le {} sur {} parties est {}".format(labels[1], nb_parties, np.mean(resultats[:,1])))
    #Affichage des histogrammes ensembles
    plt.hist(resultats,bins=20, histtype='bar', color= ['red', 'blue'],label=labels)
    plt.legend() 
    plt.title('Histogrammes de {} et {}'.format(labels[0],labels[1]))
    plt.show()
    #Affichage du violin plot (un graphe proche de la boite à moustaches mais plus intéressant pour notre cas)
    plt.violinplot(resultats, vert=False,showmeans=True,showextrema=True) 
    ax=plt.gca()
    ax.set_yticks(np.arange(1, 3)) 
    ax.set_yticklabels(labels) 
    plt.xlabel("Nombre d'essais")
    plt.title('Violin plot pour {} et {}'.format(labels[0],labels[1]))
    plt.show()
    
#afficher_histogramme_q8(1)

#%% Question 10 ================================================================

def afficher_histogramme_q10(nb_parties):
    resultats = np.zeros((nb_parties,4))
    labels=["codemaker1","codemaker2","codebreaker2","codebreaker3"]
    for i in range(nb_parties):
        resultats[i,0]=play(codemaker1,codebreaker2)
        resultats[i,1]=play(codemaker1,codebreaker3)
        resultats[i,2]=play(codemaker2,codebreaker2)
        resultats[i,3]=play(codemaker2,codebreaker3)
    plt.figure()
    #On applique un affichage similaire à celle de la question 4 mais en deux fois car on compare deux groupes
    #Affichage des histogrammes séparés et des moyennes
    for i in range (4):
        plt.hist(resultats[:,i],bins = 20, color = 'red', edgecolor = 'white', range = (0, max(resultats[:,i]))) 
        plt.title("Histogramme {} contre {}".format(labels[int((i-i%2)/2)],labels[int(2+i%2)]))
        plt.xlabel("Nombre d'essai")
        plt.ylabel("Nombre de parties")
        plt.show()
        print("La moyenne des valeurs de l'histogramme pour le {} contre {} sur {} parties est {}".format(labels[int((i-i%2)/2)],labels[int(2+i%2)],nb_parties, np.mean(resultats[:,i])))
    #Affichage des histogrammes ensembles
    plt.hist(resultats[:,:2],bins=20, histtype='bar', color= ['red', 'blue'],label=labels[2:])
    plt.legend() 
    plt.title('Histogrammes de {} et {} contre {}'.format(labels[2],labels[3],labels[0]))
    plt.show()
    plt.hist(resultats[:,2:],bins=20, histtype='bar', color= ['red', 'blue'],label=labels[2:])
    plt.legend() 
    plt.title('Histogrammes de {} et {} contre {}'.format(labels[2],labels[3],labels[1]))
    plt.show()
    #Affichage du violin plot (un graphe proche de la boite à moustaches mais plus intéressant pour notre cas)
    plt.violinplot(resultats[:,:2], vert=False,showmeans=True,showextrema=True) 
    ax=plt.gca()
    ax.set_yticks(np.arange(1, 3)) 
    ax.set_yticklabels(labels[2:]) 
    plt.xlabel("Nombre d'essais")
    plt.title('Violin plot pour {} et {} contre {}'.format(labels[2],labels[3],labels[0]))
    plt.show()
    plt.violinplot(resultats[:,2:], vert=False,showmeans=True,showextrema=True) 
    ax=plt.gca()
    ax.set_yticks(np.arange(1, 3)) 
    ax.set_yticklabels(labels[2:]) 
    plt.xlabel("Nombre d'essais")
    plt.title('Violin plot pour {} et {} contre {}'.format(labels[2],labels[3],labels[1]))
    plt.show()
    
#afficher_histogramme_q10(100)
