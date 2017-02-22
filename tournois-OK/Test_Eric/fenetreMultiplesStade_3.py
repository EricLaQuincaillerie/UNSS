#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

#affichage d'une fenetre fille en cliquant sur un bouton

from functools import partial # permet dans un bouton d'avoir une commande avec des variable
from tkinter import * 

test = StringVar
Result = []

def Enr_Resultat():
    ###print (Resultat.get())
    mem_result=Resultat.get()
    print(mem_result)
    Result.append(mem_result)
    
def ff(bt):
    num=bt.cget("text")
    print(num)
    test = str(num)
    print(test)
    Result.append(num)
    fenetre_resultat = Toplevel() 
    fenetre_resultat.title("résultat pour "+ "test")     ### titre de la fenetre avec le nombre de stade
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
    print(Result)    
    Button(fenetre_resultat, text="Valider", command=fenetre_resultat.destroy).pack(pady=10) ##bouton de sortie de la fenetre
    
    
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

    i=0
    j=1
    
    print(equipes)
    
    while j< nb:
        while i+j < nb:
            i+=1
            w=j+i
            #print ("equipe "+str(j)+"\n"+"equipe "+str(w)+"\n")
            textAffichage = str(equipes[j-1][0])
            b=Button(fenetre_fille, text = textAffichage, bg = "light green", relief = RAISED, activebackground = "white", bd = 2)
            b.config(command=lambda bt=b: ff(bt))
            b.pack(pady=2)
            #b.grid(row = b, column = 1, padx = 5, pady = 5)
            textAffichage = str(equipes[(w-1)][0])
            b=Button(fenetre_fille, text = textAffichage, bg = "light green", relief = RAISED, activebackground = "white", bd = 2)
            b.config(command=lambda bt=b: ff(bt))
            b.pack(pady=3)
            
        j+=1
        i=0    
    
    
    Button(fenetre_fille, text="Quitter", command=fenetre_fille.destroy).pack(pady=10) ##bouton de sortie de la fenetre

