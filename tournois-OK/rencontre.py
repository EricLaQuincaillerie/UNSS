#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 


def rencontre (nombreEquipe):
    ## créer l'ensemble des matchs en fonction du nombre d'équipe
    
    nbEquipe = nombreEquipe
    
    i=0
    j=1
    
    
    while j< nbEquipe:
        while i+j < nbEquipe:
            i+=1
            print ("equipe "+str(j)+"\n"+"equipe"+str(j+i)+"\n")
        
        j+=1
        i=0
    
if __name__ == "__main__":
    rencontre(6)
