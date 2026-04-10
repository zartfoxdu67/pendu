from random import choice

def lire_dictionnaire(nom_de_fichier: str):
    """
    ouvre le fichier liste_francaise et choisi un mot au hasard
    
    args:
        nom_de_fichier: nom du fichioer dans le quel on recuepere un mot
    
    returns:
        mot_aleatoire : str : mot aleatoire dans le fichier nom_de_fichier
    """
    dictionaire_francais = []
    with open(nom_de_fichier, 'r') as fichier:
        contenu = fichier.read()
        dictionaire_francais = contenu.split('\n')  
    mot_aleatoire = choice(dictionaire_francais)
    return mot_aleatoire



def affiche_mot(mot_choisi: str, lettres_trouves: list[str]):
    """
    affiche le mot du pendu en fonction des lettre trouve

    args:
        mot_str : mot a trouver
        lettrtes_trouves : list_str: liste desd lettres deja essayes
    
    returns:
         mot_aleatoire : str : mot qui doit etre afficher
    """
    # variable pour afficher le mot
    mot_affiche = ""
    # boucle qui parcours les lettres du mot choisi
    for lettre in mot_choisi:
        # Si la lettre est dans les lettres trouvés bb bvh,
        if lettre in lettres_trouves:
            # Elle va s'afficher
            mot_affiche += lettre
        # Si la lettre n'est pas dans les lettres trouvés
        else:
            # Elle ne va pas s'afficher
            mot_affiche += "-"
    return mot_affiche



def jeu_est_fini(mot_choisi : str, lettres_trouves : list[str]):
    """
    jeu_est_fini : 
        True si le mot est trouvé
        False si le mot est pas encore trouvé=

    Args:
        mot_choisi : str : mot a trouver
        lettres_trouves : list[str] : tableau des lettres donnéesz

    Returns:
        booleen : Le mot est trouvé ou pas
    """
    # si le mot affiché est celui qui est choisi alors c'est qu'on a trouvé toutes les lettres
    return (affiche_mot(mot_choisi, lettres_trouves) == mot_choisi)



def donne_nouvelle_lettre(lettres_trouvees: list[str], mot_choisi: str) -> list[str]:
    """
    args:
        lettre_trouver : list[str] : tableau des lettre deja trouves
        mot_choisi : str : mot choisi a trouver
    returns:
        nouvelle_lettre : list[str] : nouveau tableau des lettre
    """
    lettre_correcte = False
    alphabet = "azertyuiopqsdfghjklmwxbncv"
    while not lettre_correcte: 
        # Demande une lettre
        nouvelle_lettre = input("donne_moi_une_lettre : ")
        petite_lettre = nouvelle_lettre.lower()
        if len(petite_lettre) == 1 and petite_lettre in alphabet and not petite_lettre in lettres_trouvees :
            lettre_correcte = True
    
    # On ajoute la nouvelle lettre a la liste des lettres trouvées
    lettres_trouvees.append(petite_lettre)
    if petite_lettre == "e":
        lettres_trouvees.append("ê")
        lettres_trouvees.append("é")
        lettres_trouvees.append("è")
    if petite_lettre == "c":
        lettres_trouvees.append("ç")
    if petite_lettre == "a":
        lettres_trouvees.append("à")
        lettres_trouvees.append("â")
    if petite_lettre == "u":
        lettres_trouvees.append("û")
        lettres_trouvees.append("ù")
    if petite_lettre == "o":
        lettres_trouvees.append("ô")
    if petite_lettre == "i":
        lettres_trouvees.append("î")
        lettres_trouvees.append("ï")
        
    # Dit si la nouvelle lettre est dans le mot
    lettre_dans_mot = petite_lettre in mot_choisi
    # On retourne la nouvelle liste des lettres avec la nouvelle lettre dedans et si la lettre est dans le mot
    return lettres_trouvees, lettre_dans_mot

def affiche_lettres (lettre_trouver):
    for lettre_mot in lettre_trouver:
        print(lettre_mot, end=" ")
    print("")
    

    
    """
    
    """


if __name__ == "__main__":
    """
    Programme principal
    
    Execute le jeu du pendu
    """
    # Lit dans le dictionnaire et choisi au hasard un mot dedans
    mot_choisi = lire_dictionnaire("liste_francais.txt")
    # Initialisation de la liste des lettres trouvées
    lettres_trouvees = []
    # Initialisation des vies
    nb_vies = 11
    # Boucle du jeu qui s'arrete quand il est fini
    # C'est a dire - quand on a trouvé le mot choisi
    # C'est a dire - quand on a trouvé toutes les lettres qui compose le mot choisi
    while not jeu_est_fini(mot_choisi, lettres_trouvees) and nb_vies > 0 : 
        # Le programme demande une lettre
        # Pour en faire quoi - Pour l'ajouter a la liste des lettres trouvées
        print("voici les lettre deja donner")
        affiche_lettres(lettres_trouvees)
        lettres_trouvees, lettre_dans_mot = donne_nouvelle_lettre(lettres_trouvees, mot_choisi)
        if not lettre_dans_mot:
            nb_vies = nb_vies - 1
        # On affiche le mot en fonction des lettres dans la liste des lettres données
        print("> " + affiche_mot(mot_choisi, lettres_trouvees))
        print (f"il vous reste {nb_vies} vies")

    if nb_vies > 0:
        print("bravo ta gagner")
    else:
        print("ta perdu")
        print(f"le mot etait '{mot_choisi}'")