#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

#affichage d'une fenetre fille en cliquant sur un bouton

from functools import partial # permet dans un bouton d'avoir une commande avec des variable
from tkinter import * 


def resultat():
    fenetre_resultat = Toplevel() 
    fenetre_resultat.title("Indication des résultats")     ### titre de la fenetre avec le nombre de stade
    fenetre_resultat.geometry("300x200")
    fenetre_resultat.config(bg="red")
    
    
    
    Button(fenetre_resultat, text="Bye!", command=fenetre_resultat.destroy).pack(pady=10) ##bouton de sortie de la fenetre
    print("bonjour")
         
    
def nouvelle_fenetre (variable, StadeEquipes): 
    """ 
        cette fonction crée une nouvelle fenêtre fille à chaque fois 
        qu'on clique sur le bouton correspondant 
    """ 
    # variable est le nom du stade 
    # StadeEquipes est le dico avec l'ensemble des stades et des equipes de chaque stade
    
    global fenetre_fille 
  
    # ceci est une fenêtre fille (Toplevel) 
    # elle sera automatiquement détruite lorsque vous quitterez le 
    # programme en fermant la fenêtre principale 
  
    fenetre_fille = Toplevel() 
    fenetre_fille.title(variable)     ### titre de la fenetre avec le nombre de stade
    fenetre_fille.geometry("300x700")
    fenetre_fille.config(bg="white")
    
    equipes=StadeEquipes[variable]   ## mettre dans une liste 'equipes'' la liste du dico 'StadeEquipe' qui a la clée 'variable'    
    nb=len(equipes)   ##compter le nombre d'équipe
    
    
   
    ##Label(fenetre_fille, text= variable).pack(pady=10, padx=0) 
    
    ##while i< nb:
        #### affiche les équipes  et leur resultats les une sous les autres
        ##textAffichage = (str(equipes[i][0])+" "+str(equipes[i][3])+" "+str(equipes[i][4])+" "+str(equipes[i][5]))
        ##Label(fenetre_fille, text= textAffichage).pack(pady=2, padx=0)
        ##i+=1
    
    
    ## affiche les équipes  et leur resultats les une sous les autres
    #### premier match
    ##Label(fenetre_fille, text= "premier match ",font=("Helvetica", 12)).pack(pady=2, padx=0)
    ##textAffichage = (str(equipes[0][0])+" "+str(equipes[0][3]))
    ##Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
    ##textAffichage = (str(equipes[1][0])+" "+str(equipes[1][3]))
    ##Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
    ##Label(fenetre_fille, text= " ").pack(pady=1, padx=0)
    
    #### second match
    ##Label(fenetre_fille, text= "second match ",font=("Helvetica", 12)).pack(pady=2, padx=0)
    ##textAffichage = (str(equipes[2][0])+" "+str(equipes[2][3]))
    ##Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
    ##textAffichage = (str(equipes[3][0])+" "+str(equipes[3][3]))
    ##Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
    ##Label(fenetre_fille, text= " ").pack(pady=1, padx=0)
    
    #### troisieme match
    ##Label(fenetre_fille, text= "troisieme match ",font=("Helvetica", 12)).pack(pady=2, padx=0)
    ##textAffichage = (str(equipes[0][0])+" "+str(equipes[0][4]))
    ##Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
    ##textAffichage = (str(equipes[2][0])+" "+str(equipes[2][4]))
    ##Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
    ##Label(fenetre_fille, text= " ").pack(pady=1, padx=0)
    
    #### quatrième match
    ##Label(fenetre_fille, text= "quatrième match ",font=("Helvetica", 12)).pack(pady=2, padx=0)
    ##textAffichage = (str(equipes[1][0])+" "+str(equipes[1][4]))
    ##Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
    ##textAffichage = (str(equipes[3][0])+" "+str(equipes[3][4]))
    ##Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
    ##Label(fenetre_fille, text= " ").pack(pady=1, padx=0)
    
    #### cinquième match
    ##Label(fenetre_fille, text= "cinquième match ",font=("Helvetica", 12)).pack(pady=2, padx=0)
    ##textAffichage = (str(equipes[0][0])+" "+str(equipes[0][5]))
    ##Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
    ##textAffichage = (str(equipes[3][0])+" "+str(equipes[3][5]))
    ##Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
    ##Label(fenetre_fille, text= " ").pack(pady=1, padx=0)
    
    ####sixième match
    ##Label(fenetre_fille, text= "sixième match ",font=("Helvetica", 12)).pack(pady=2, padx=0)
    ##textAffichage = (str(equipes[1][0])+" "+str(equipes[1][5]))
    ##Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
    ##textAffichage = (str(equipes[2][0])+" "+str(equipes[2][5]))
    ##Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
    ##Label(fenetre_fille, text= " ").pack(pady=1, padx=0)
    
    
    ## créer l'ensemble des matchs en fonction du nombre d'équipe
    
    ### supprimé en double? nbEquipe = nb
    
    i=0
    j=1
    
    print(equipes)
    
    while j< nb:
        while i+j < nb:
            i+=1
            w=j+i
            print ("equipe "+str(j)+"\n"+"equipe "+str(w)+"\n")
            textAffichage = (str(equipes[j-1][0])+" "+str(equipes[j-1][3]))
            Button(fenetre_fille, text=textAffichage, command=resultat).pack(pady=1, padx=0)  ### test bouton
            ###Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
            textAffichage = (str(equipes[(w-1)][0])+" "+str(equipes[(w-1)][3]))
            Button(fenetre_fille, text=textAffichage, command=resultat).pack(pady=1, padx=0)  ### test bouton
            ###Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
            Label(fenetre_fille, text= " ").pack(pady=1, padx=0)
            ### test bouton
            
            
        j+=1
        i=0    
    
    Button(fenetre_fille, text="Quitter", command=fenetre_fille.destroy).pack(pady=10) ##bouton de sortie de la fenetre

    
    
    
    
    
    
if __name__ == '__main__':
    # ceci est la fenêtre principale du programme (Tk) 
      
    fenetre = Tk() 
      
    fenetre.title("Fenêtre principale") 
      
    ## StadeEquipes est un dico pour tester ce programme
    ## Stade1 permet de choisir le dico avec Stade1  on peut tester avec Stade2 et autre
    stade="Stade1" 
    StadeEquipes= {'Stade4': [['Haute-Vienne', ' 87', ' Limousin', [0], [0], [0]], 
                    ['Var', ' 83', ' Provence-Alpes-Côte d Azur', [0], [0], [0]], 
                    ['Val-d Oise', ' 95', ' Ile-de-France', [0], [0], [0]], 
                    ['Yonne', ' 89', ' Bourgogne', [0], [0], [0]]], 
                    'Stade2': [['Tarn-et-Garonne', ' 82', ' Midi-Pyrénées', [0], [0], [0]],
                     ['Vaucluse', ' 84', ' Provence-Alpes-Côte d Azur', [0], [0], [0]],
                      ['Essonne', ' 91', ' Ile-de-France', [0], [0], [0]], 
                      ['Vosges', ' 88', ' Lorraine', [0], [0], [0]]],
                       'Stade3': [['Hauts-de-Seine', ' 92', ' Ile-de-France', [0], [0], [0]],
                        ['Val-de-Marne', ' 94', ' Ile-de-France', [0], [0], [0]],
                         ['Somme', ' 80', ' Picardie', [0], [0], [0]],
                          ['Tarn', ' 81', ' Midi-Pyrénées', [0], [0], [0]]],
                           'Stade1': [['Territoire-de-Belfort', ' 90', ' Franche-Comté', [0], [0], [0]],
                            ['Vendée', ' 85', ' Pays de la Loire', [0], [0], [0]],
                             ['Vienne', ' 86', ' Poitou-Charentes', [0], [0], [0]], 
                             ['Seine-Saint-Denis', ' 93', ' Ile-de-France', [0], [0], [0]]]}
    ##fin des variables de test
                             
    Label(fenetre, text="Cliquez sur le bouton").pack(pady=20, padx=10) 
    
    ## pour la fonction command du bouton, partial permet d'avoir une variable
    ##il faut penser à faire l'import de functools au debut
     
    Button(fenetre, text=stade, command=partial(nouvelle_fenetre, stade, StadeEquipes)).pack(pady=5, padx=10)  
    Button(fenetre, text="Quitter", command=fenetre.destroy).pack(pady=5) 
      
    # /!\ n'oubliez pas de finir avec la boucle principale /!\ 
      
    fenetre.mainloop()
    
