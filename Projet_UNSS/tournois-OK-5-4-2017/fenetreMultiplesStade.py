#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

##affichage d'une fenetre fille en cliquant sur un bouton

from functools import partial ## permet dans un bouton d'avoir une commande avec des variable
from tkinter import * 
from choixResultatMatch import *


def poule (nbEquipeParPoule):
    ## determine les rencontre des équipes dans les poules
    ## création d'un dictionnaire avec  poule de 4 équipes (clée : premier) ou de 5 équipe (clée: second)
    ## on peut definie au départ les equipes qui se rencontre en modifiant le dico
    cas={'4equipes':[1,4,2,3,1,3,2,4,1,2,3,4],'5equipes':[2,5,3,4,1,5,2,3,1,4,3,5,1,3,2,4,1,2,4,5]}
    
    
    if nbEquipeParPoule == 4:
        match = cas['4equipes']          ## si 4 equipes dans la poule alors cette conbimnaison est choisie
        
    else:
        match = cas['5equipes']           ## si 5 equipes dans la poule alors cette conbimnaison est choisie
        
    ##print(match)    
    return(match)                       ## retourne la liste comme valeur
    
def fenetreRencontreMatch(equipe1,equipe2):
    
    #fenetre qui s'ouvre quant on clique sur le match correspondant
    
    #global fenetre_fille1 
  
    # ceci est une fenêtre fille1 (Toplevel) 
    # elle sera automatiquement détruite lorsque vous quitterez le 
    # programme en fermant la fenêtre principale 
  
    fenetre_fille1 = Toplevel() 
    fenetre_fille1.title("resultats du match")     ## titre de la fenetre avec le nombre de stade
    
    
   
    
    fenetre_fille1.geometry("600x150") ##Premier chiffre pour horizontale
    fenetre_fille1.resizable(width=True, height=True)
    ##fenetre_fille1.minsize("400x100")
    ##fenetre_fille1.maxsize("600x200")
    fenetre_fille1.config(bg="white")
    tailleCaracT = "courier 12"
    #var = IntVar()
    
    ## affichage titre
    txt = Label(fenetre_fille1,text = "résultats de la rencontre")
    txt.config(bd=2,fg="black",bg="white",font=tailleCaracT)
    txt.grid(row = 0,column = 0,sticky=NSEW, columnspan=4)
    
    
    
    ##affichage équipe 
    ligneEquipe1 = 2  ##utilisé pour positionner dans la fenetre
    
    fenetreAffichage = fenetre_fille1
    
    Frame5 = Frame(fenetre_fille1, bg="blue",borderwidth=1)
    Frame5.grid(row=0,column = 0)
    Frame5.rowconfigure(0, weight=100)
    Frame5.columnconfigure(0, weight=100)
    
    affichage(Frame5,equipe1, equipe2, ligneEquipe1)
    
    Button(fenetre_fille1, text="Quitter", command=fenetre_fille1.destroy).grid(row=10) ##bouton de sortie de la fenetre 
   
      
 
def matchsDifferents( NumEquipe,listeEquipe):
    
    ## affiche les differents match en fonction du nombre d équipes dans chaque poule (variable)
    NbMatch= (len(NumEquipe))
    i=0
    print(NumEquipe)
    print("\n")
    print(listeEquipe)
    while i< NbMatch:
        j=(NumEquipe[i])     ## -1 car debut à indice 0
        k=NumEquipe[i+1]
        
        print(str(j)+" contre "+str(k))
        print((listeEquipe[j-1][0])+" contre "+(listeEquipe[k-1][0]))
        
        equipe1 = (listeEquipe[j-1][0])
        equipe2 = (listeEquipe[(k-1)][0])
        Button(fenetre_fille, text="resultat du match", command=partial(fenetreRencontreMatch, equipe1, equipe2)).grid(row=1+2*i, column=2) 
        ##Label(fenetre_fille, text="").pack(pady=0)
        
        ##textAffichage = (str(listeEquipe[j-1][0])+" "+str(listeEquipe[j-1][3]))
        textAffichage = str(equipe1)
        Label(fenetre_fille, text= textAffichage).grid(row=2+2*i, column=2) 
        
        ##textAffichage = (str(listeEquipe[(k-1)][0])+" "+str(listeEquipe[(k-1)][3]))
        textAffichage = str(equipe2)
        Label(fenetre_fille, text= textAffichage).grid(row=3+2*i, column=2) 
        Label(fenetre_fille, text= " ").grid(row=4+2*i, column=2) 
        
        i+=2
        
        

    
def nouvelle_fenetre (variable, StadeEquipes): 
    """ 
        cette fonction crée une nouvelle fenêtre fille à chaque fois 
        qu'on clique sur le bouton correspondant 
    """ 
    ## variable est le nom du stade 
    ## StadeEquipes est le dico avec l'ensemble des stades et des equipes de chaque stade
    
    global fenetre_fille 
  
    # ceci est une fenêtre fille (Toplevel) 
    # elle sera automatiquement détruite lorsque vous quitterez le 
    # programme en fermant la fenêtre principale 
    nomStade = ("Stade "+str(variable))
    fenetre_fille = Toplevel() 
    fenetre_fille.title(nomStade)     ## titre de la fenetre avec le nombre de stade
    fenetre_fille.geometry("300x700")
    #fenetre_fille.config(bg="white")
    
    equipes=StadeEquipes[variable]   ## mettre dans une liste 'equipes'' la liste du dico 'StadeEquipe' qui a la clée 'variable'    
    nb=len(equipes)   ##compter le nombre d'équipe
        
    
    ## affiche les équipes  et leur resultats les une sous les autres
    
    
    ## créer l'ensemble des matchs en fonction du nombre d'équipe
    
    poule(nb)   ## utilise la def poule de rencontre.py pour definir l'ordre des matchs
    
    matchsDifferents(poule(nb),equipes)
    
    
    Button(fenetre_fille, text="Quitter", command=fenetre_fille.destroy).grid(row=1, column=10)  ##bouton de sortie de la fenetre

    
    
    
    
    
    
if __name__ == '__main__':
    # ceci est la fenêtre principale du programme (Tk) 
      
    fenetre = Tk() 
      
    fenetre.title("Fenêtre principale") 
      
    ## StadeEquipes est un dico pour tester ce programme
    ## Stade1 permet de choisir le dico avec Stade1  on peut tester avec Stade2 et autre
    stade="Stade4" 
    StadeEquipes= {'Stade4': [['moi', ' 100', ' ici', [0], [0], [0]],['Haute-Vienne', ' 87', ' Limousin', [0], [0], [0]], 
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
                             
    Label(fenetre, text="Cliquez sur le bouton").grid(row=1, column=2) 
    
    ## pour la fonction command du bouton, partial permet d'avoir une variable
    ##il faut penser à faire l'import de functools au debut
     
    Button(fenetre, text=stade, command=partial(nouvelle_fenetre, stade, StadeEquipes)).grid(row=2, column=2)  
    Button(fenetre, text="Quitter", command=fenetre.destroy).grid(row=4, column=2)  
      
    # /!\ n'oubliez pas de finir avec la boucle principale /!\ 
      
    fenetre.mainloop()
    
