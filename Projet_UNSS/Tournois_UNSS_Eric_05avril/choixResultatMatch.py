
# -*- coding: utf-8 -*-
#!/usr/bin/python3

from tkinter import *
from functools import partial ## permet dans un bouton d'avoir une commande avec des variable

matchPremierTour={}

def updateAttendance():
	# ENREGISTREMENT DES RÉSULTATS DU PREMIER TOUR
	
	###lbDept.delete(0, END)  ##permet d'éffacer l'affichage de la liste et de metre la nouvelle liste à la place
	
	cr = csv.reader(open(Resultat1erTour.encode('utf-8'),"rt")) #on récupére le fichier
	datalist = list(cr) #on le met sous forme de liste
	c = csv.writer(open(Resultat1erTour.encode('utf-8'), "wt")) #on écrit dans le fichier
	
	for x in range(0, len(listeDept)):
		
		if listeDept[x][3].get() == 1:
			lbDept.insert(END, listeDept[x][1]+"-"+listeDept[x][0])
			c.writerows([[listeDept[x][0],listeDept[x][1],listeDept[x][2]]])

		#On met writerows (au pluriel) pour pouvoir écrire plusieurs
		#ligne, on concatène la liste "datalist" avec la
		#ligne à ajouter (il faut la mettre sous forme d'une liste de liste)

class affichage(Frame):

	def __init__(self,parent, nomEquipe1, nomEquipe2, ligneEquipe1):
		Frame.__init__(self,parent)
		self.parent = parent
		#self.parent.title("Résultats ")
		self.parent.columnconfigure(0, weight=1)
		self.parent.rowconfigure(0, weight=20)
		## self.master.geometry("600x150") #Premier chiffre pour horizontale
		## self.master.config(bg="white")
		
		self.columnconfigure(0, weight=10)
		self.rowconfigure(0, weight=10)
		self.grid(sticky="NSEW")
		self.config(bg="white")
		
		self.choixResultat1(nomEquipe1,nomEquipe2,ligneEquipe1)	#lance la procédure qui créer les widgets
		
	def caseForfait1(self):
		resultat = self.var1.get()
	
	def caseForfait2(self):
		resultat = self.var2.get()
		
	def testResultatsEquipe(self, nomEquipe1, nomEquipe2, ligneAffichage, col):
		
		##result1= int(self.varResultatEquipe1.get())
		##result2= int(self.varResultatEquipe2.get())
		
		result1= self.varResultatEquipe1.get()   ### result1 et result2 sont au format str
		result2= self.varResultatEquipe2.get()
		
		
					 
		##self.affichePoint1.grid(row=ligneAffichage,column=col+6)
					  
		
		
		print ("résultats: ",nomEquipe1,result1, nomEquipe2, result2)
		
		
		if result1 == "f":
			point1=0
			point2=3
			
		if result2 == "f":
			point1=3
			point2=0
			
			
		if int(result1) == int(result2):
			point1=2
			point2=2
			
		if int(result1) > int(result2):
			point1=4
			point2=1
			
		if int(result1) < int(result2):
			point1=1
			point2=4
	
		self.affichePoint1 = Label(self, text=point1, width=10)
		self.affichePoint1.grid(row=ligneAffichage,column=col+6)
		self.affichePoint2 = Label(self, text=point2, width=10)
		self.affichePoint2.grid(row=ligneAffichage+1,column=col+6)
		
		## inscription dans le dico du premier tour
		matchPremierTour[nomEquipe1+"///"+nomEquipe2]=(nomEquipe1, int(result1), point1, nomEquipe2, int(result2), point2)
		print(matchPremierTour)
		return   matchPremierTour    
	
	def ecrireResultat1(self):
		#global resultatE1
		print("resultat de l'équipe ",(self.varResultatEquipe1.get()))
		resultatE1=int(self.varResultatEquipe1.get())
		print("Résultat de l'équipe1: ",resultatE1)
		return resultatE1
	
	def ecrireResultat2(self):
		#global resultatE2
		print("resultat de l'équipe ",(self.varResultatEquipe2.get()))
		resultatE2= int(self.varResultatEquipe2.get())
		print("Résultat de l'équipe2: ",resultatE2)
		return resultatE2
	
		   
	def choixResultat1(self,nomEquipe1,nomEquipe2,ligneEquipe1):
		
		tailleCaracT = "courier 12"
		ligneEquipe = ligneEquipe1 ##position de la ligne de la premiere equipe
		col=1
		self.var1 = IntVar()
		self.var2 = IntVar()
		
		## affichage titre
		self.txt = Label(self,text = "résultats de la rencontre")
		self.txt.config(bd=2,fg="black",bg="white",font=tailleCaracT)
		self.txt.grid(row = 0,column = col,sticky=W)
		
		self.txt1 = Label(self,text = "Nb de buts")
		self.txt1.config(bd=2,fg="black",bg="white",font=tailleCaracT)
		self.txt1.grid(row = 0,column = col+5,sticky=W)
	   
		self.txt2 = Label(self,text = "Nb de points")
		self.txt2.config(bd=2,fg="black",bg="white",font=tailleCaracT)
		self.txt2.grid(row = 0,column = col+6,sticky=W)
		
		#creation des variables equipe1
	   
	   
		self.varResultatEquipe1 = StringVar()
		self.varResultatEquipe1.set("0")
		
		## position ecriture du nom de l'équipe
		self.txtResultat1 = Label(self, text=("resultat de l'"+ nomEquipe1))
		self.txtResultat1.config(bd=2,fg="black",bg="white",font=tailleCaracT)
		self.txtResultat1.grid(row = ligneEquipe,column = col)
		
		
		##affichage resultat equipe 1
		self.resultatEquipe1 = Entry(self,width=5, textvariable=self.varResultatEquipe1)
		self.resultatEquipe1.config(bd=2,fg="black",bg="white",font=tailleCaracT)    
		self.resultatEquipe1.grid(row= ligneEquipe, column = col+1)
		
		self.afficheResultat1 = Label(self, text="", textvariable=self.varResultatEquipe1, width=10)
		self.afficheResultat1.grid(row=ligneEquipe,column=col+5)
			
		
		resultatE1 = int(self.varResultatEquipe1.get())
		
		
		##affichage bouton radio forfait equipe1
		
		###self.boutonForfait1 = Checkbutton(self, text="forfait", variable=self.var1, command = self.caseForfait1)
		###self.boutonForfait1.grid(row=ligneEquipe,column=col+7)
		
		###self.boutonForfait1.config(bd=2,fg="black",bg="white") 
		
		
		print ("resultat de l'Équipe ",nomEquipe1," : ",resultatE1)        ## pour info
		
		
		#creation des variables equipe2
	   
	   
		self.varResultatEquipe2 = StringVar()
		self.varResultatEquipe2.set("0")
		
		## position ecriture du nom de l'équipe
		self.txtResultat2 = Label(self, text=("resultat de l'"+ nomEquipe2))
		self.txtResultat2.config(bd=2,fg="black",bg="white",font=tailleCaracT)
		self.txtResultat2.grid(row = ligneEquipe+1,column = col)
		
		
		##affichage resultat equipe 2
		self.resultatEquipe2 = Entry(self,width=5, textvariable=self.varResultatEquipe2)
		self.resultatEquipe2.config(bd=2,fg="black",bg="white",font=tailleCaracT)    
		self.resultatEquipe2.grid(row= ligneEquipe+1, column = col+1)
		
		self.afficheResultat2 = Label(self, text="", textvariable=self.varResultatEquipe2, width=10)
		self.afficheResultat2.grid(row=ligneEquipe+1,column=col+5)
			
		
		resultatE2 = int(self.varResultatEquipe2.get())
		
		##affichage bouton Checkbutton forfait equipe2
		
		###self.boutonForfait2 = Checkbutton(self, text="forfait", variable=self.var2,  command = self.caseForfait2)
		###self.boutonForfait2.grid(row=ligneEquipe+1,column=col+7)
		
		###self.boutonForfait2.config(bd=2,fg="black",bg="white") 
		
		
		print ("resultat de l'Équipe ",nomEquipe2," : ",resultatE2)        ## pour info
	   
		print ("RÉSULTATS:",nomEquipe1, resultatE1, nomEquipe2, resultatE2)

		self.btn3=Button(self, text="validation des resultats", command = partial(self.testResultatsEquipe, nomEquipe1, nomEquipe2, ligneEquipe, col))
		
		self.btn3.grid(row=ligneEquipe+6, column=col)
	
		
		##testResultatsEquipe(nomEquipe1,result1, nomEquipe2, result2)
		print("RÉsultat de la rencontre", matchPremierTour)
	updateAttendance()
	

if __name__ =='__main__':
	
	fenetre = Tk() 
	matchPremierTour={}
	nomEquipe1 = "equipe1"
	nomEquipe2 = "equipe2"
	ligneEquipe1 = 2
	#col=1
	#ligneAffichage = ligneEquipe1
	appli=affichage(fenetre, nomEquipe1, nomEquipe2,ligneEquipe1)
	appli.mainloop()
