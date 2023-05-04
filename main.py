import math
with open("poeme.txt","r") as f:
    contenu = f.read()
contenu=contenu.split(" ")
liste=[]
for element in contenu:
    #element.split(""\n"")
    for lettre in element:
        if lettre == " " or lettre == "\n" or lettre == "'" or lettre == "!":
            lettre=""

print(contenu)
py=([len(element) for element in contenu])
print(py)

pi=str(math.pi)
pi=pi.replace(".","")
pi=list(pi)
print(pi)

#Exercice2
import csv

class Etudiant:
    def __init__(self,nom,annee_naissance,gpa,connais_python):
        self.nom=nom
        self.annee_naissance=annee_naissance
        self.gpa=gpa
        self.connais_python=connais_python

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom:str):
        if not isinstance(nom, str):
            raise TypeError("Entrez une chaîne de caractère")
        self.__nom = nom

    @property
    def annee_naissance(self):
        return self.__annee_naissance
    @annee_naissance.setter
    def annee_naissance(self, annee_naissance):
        if not isinstance(annee_naissance, int):
            raise TypeError("Entrez un int")
        self.__annee_naissance=annee_naissance

    @property
    def gpa(self):
        return self.__gpa
    @gpa.setter
    def gpa(self, gpa):
        if not isinstance(gpa, float):
            raise TypeError("Entrez un float")
        self.__gpa=gpa

    @property
    def connais_python(self):
        return self.__connais_python
    @connais_python.setter
    def connais_python(self, connais_python):
        if not isinstance(connais_python, bool):
            raise TypeError("Entrez un booléen")
        self.__connais_python=connais_python

    def to_dict(self):
         print( {"nom": self.nom , "annee_naissance":self.annee_naissance,"gpa":self.gpa,"connais_python":self.connais_python})

    @staticmethod
    def from_dict(d):
        return Etudiant(
            nom=d["nom"],
            annee_naissance=int(d["annee_naissance"]),
            gpa=float(d["gpa"]),
            connais_python=bool(d["connais_python"])
        )



class Groupe:
    def __init__(self,etudiants):
        self.etudiants=etudiants
    def sauvegarder_csv(self,chemin):
        with open('chemin', 'w', newline='') as f:
            fieldnames = ['nom', 'annee_naissance','gpa','connais_python']
            writer = f.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for etudiant in self.etudiants:
                writer.writerow(etudiant.to_dict)

etudiant1=Etudiant("Florian",2002,2.8,False)
etudiant2=Etudiant("Kevin",2004,5.0,True)
etudiant3=Etudiant("Raph",2011,3.2,True)
etudiant4=Etudiant("Julian",2000,1.9,False)

etudiant1.to_dict()
etudiant2.to_dict()
etudiant3.to_dict()
etudiant4.to_dict()

liste=Groupe([etudiant1,etudiant2,etudiant3,etudiant4])


#Exercice 3
import pickle
# Lecture
with open("poeme.txt", "rb") as f:
    contenu = pickle.load(f)
# Écriture
with open("poeme.txt", "wb") as f:
    pickle.dump(contenu, f)

import pickle
with open("poeme.txt","wb") as f:
    pickle.duloload(f)


salut