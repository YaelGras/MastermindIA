# Projet-Info

Projet fait par : Quentin Zoppis, Romain Peyremorte, Yael Gras

Toutes les fonctions suivantes sont dans le fichier play.py et les codemakers et codebreakers sont dans des fichiers séparés

Pour lancer une partie entre 2 IA :
Importer le codemaker et le codebreaker,
Lancer la fonction : play(codemaker, codebreaker)
Si vous souhaitez un log de la partie, vous pouvez modifier la fonction play par la fonction : play_log(codemaker, codebreaker, nom_fichier)

Pour lancer une partie en jouant le codebreaker contre une IA qui fait le codemaker :
Importer le codemaker
Lancer la fonction : play_human_against_codemaker(codemaker)

Pour lancer une partie en jouant le codemaker contre une IA qui fait le codebreaker :
Importer le codemaker
Lancer la fonction : play_human_against_codebreaker(codebreaker)

Si vous souhaitez reproduire les histogrammes, vous pouvez utiliser le fichier histogramme.py et appeler la fonction : afficher_histogramme_qX(nb_de_parties) en modifiant X par la question souhaitée. Attention au nombre de partie, car il n'y a pas d'optimisation de performance ou de parties lancées simultannément.