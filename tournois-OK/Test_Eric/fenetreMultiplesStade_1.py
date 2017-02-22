#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

#affichage d'une fenetre fille en cliquant sur un bouton

from functools import partial # permet dans un bouton d'avoir une commande avec des variable
from tkinter import * 

def resultat(): ### pour afficher l'enregistrement des résultat
    fenetre_resultat = Toplevel() 
    fenetre_resultat.title("résultat pour "+bt1.get("text"))     ### titre de la fenetre avec le nombre de stade
    fenetre_resultat.geometry("300x200")
    fenetre_resultat.config(bg="red")
    
    global Resultat
    Resultat = StringVar()
    
    forfait = Radiobutton(fenetre_resultat, text="forfait", variable=Resultat, value=0, command=Enr_Resultat)
    defaite = Radiobutton(fenetre_resultat, text="defaite", variable=Resultat, value=1, command=Enr_Resultat)
    nul = Radiobutton(fenetre_resultat, text="nul", variable=Resultat, value=2, command=Enr_Resultat)
    victoire = Radiobutton(fenetre_resultat, text="victoire", variable=Resultat, value=3, command=Enr_Resultat)
    
    forfait.pack()
    defaite.pack()
    nul.pack()
    victoire.pack()
    
    Button(fenetre_resultat, text="Valider", command=fenetre_resultat.destroy).pack(pady=10) ##bouton de sortie de la fenetre

tour=[]

def Enr_Resultat():
    ###print (Resultat.get())
    mem_result=Resultat.get()
    tour.append(mem_result)
    
#def ff(bt):
    #num=bt.cget("text")
    #print(num)

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
    
    ## créer l'ensemble des matchs en fonction du nombre d'équipe
    
    ### supprimé en double? nbEquipe = nb
    
    i=0
    j=1
    
    
    while j< nb:
        while i+j < nb:
            i+=1
            w=j+i
            print ("equipe "+str(j)+"\n"+"equipe "+str(w)+"\n")
            textAffichage = (str(equipes[j-1][0]))+" "+str(equipes[j-1][3]) 
            bt1=Button(fenetre_fille, text=textAffichage, command=resultat).pack(pady=1, padx=0)  ### test bouton
            ###Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
            textAffichage = (str(equipes[w-1][0])+" "+str(equipes[w-1][3])) 
            bt1=Button(fenetre_fille, text=textAffichage, command=resultat).pack(pady=1, padx=0)  ### test bouton
            ###Label(fenetre_fille, text= textAffichage).pack(pady=1, padx=0)
            Label(fenetre_fille, text= " ").pack(pady=1, padx=0)
            ### test bouton
            tour.append(equipes[j-1][0])
            tour.append(equipes[w-1][0])
           
        j+=1
        i=0
    
    Button(fenetre_fille, text="Quitter", command=fenetre_fille.destroy).pack(pady=10) ##bouton de sortie de la fenetre
    print (tour)
    
#print (mem_result)
    

    
    
#if __name__ == '__main__':
    ## ceci est la fenêtre principale du programme (Tk) 
      
    #fenetre = Tk() 
      
    ####fenetre.title("Fenêtre principale") 
      
    ### StadeEquipes est un dico pour tester ce programme
    ### Stade1 permet de choisir le dico avec Stade1  on peut tester avec Stade2 et autre
    #stade="Stade1" 
    #StadeEquipes= {'Stade4': [['Haute-Vienne', ' 87', ' Limousin', [0], [0], [0]], 
                    #['Var', ' 83', ' Provence-Alpes-Côte d Azur', [0], [0], [0]], 
                    #['Val-d Oise', ' 95', ' Ile-de-France', [0], [0], [0]], 
                    #['Yonne', ' 89', ' Bourgogne', [0], [0], [0]]], 
                    #'Stade2': [['Tarn-et-Garonne', ' 82', ' Midi-Pyrénées', [0], [0], [0]],
                     #['Vaucluse', ' 84', ' Provence-Alpes-Côte d Azur', [0], [0], [0]],
                      #['Essonne', ' 91', ' Ile-de-France', [0], [0], [0]], 
                      #['Vosges', ' 88', ' Lorraine', [0], [0], [0]]],
                       #'Stade3': [['Hauts-de-Seine', ' 92', ' Ile-de-France', [0], [0], [0]],
                        #['Val-de-Marne', ' 94', ' Ile-de-France', [0], [0], [0]],
                         #['Somme', ' 80', ' Picardie', [0], [0], [0]],
                          #['Tarn', ' 81', ' Midi-Pyrénées', [0], [0], [0]]],
                           #'Stade1': [['Territoire-de-Belfort', ' 90', ' Franche-Comté', [0], [0], [0]],
                            #['Vendée', ' 85', ' Pays de la Loire', [0], [0], [0]],
                             #['Vienne', ' 86', ' Poitou-Charentes', [0], [0], [0]], 
                             #['Seine-Saint-Denis', ' 93', ' Ile-de-France', [0], [0], [0]]]}
    ###fin des variables de test
                             
    #Label(fenetre, text="Cliquez sur le bouton").pack(pady=20, padx=10) 
    
    ### pour la fonction command du bouton, partial permet d'avoir une variable
    ###il faut penser à faire l'import de functools au debut
     
    #Button(fenetre, text=stade, command=partial(nouvelle_fenetre, stade, StadeEquipes)).pack(pady=5, padx=10)  
    #Button(fenetre, text="Quitter", command=fenetre.destroy).pack(pady=5) 
      
    ## /!\ n'oubliez pas de finir avec la boucle principale /!\ 
      
    #fenetre.mainloop()
    
