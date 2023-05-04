import math
with open("poeme.txt","r",encoding="utf-8") as f:
    poeme = f.read()
    poeme=poeme.replace("!","")
    poeme = poeme.replace("'", " ")
    poeme = poeme.replace("?", "")
    poeme = poeme.replace(",", "")
    poeme = poeme.replace(".", "")
    poeme=poeme.split()

pi_chara=([str(len(mot)%10) for mot in poeme])
pi_chiffre_str=str()
for chiffre in pi_chara:
    pi_chiffre_str+=chiffre
pi_chiffre_str=pi_chiffre_str[0]+"."+pi_chiffre_str[1:]

pi=str(math.pi) #pi convertit en caractere

print(f"Voici le pi obtenu grâce au poème : {pi_chiffre_str}")
print(f"Voici le pi du module math : {pi}")
print(f"Est ce que le pi obtenu grâce au poème est similaire au pi du module math ? {float(pi_chiffre_str) ==float(pi)}")


#Creation d'un fichier avec pi calcule grace au poeme
with open("pi_en_fichier.txt","w",encoding="utf-8") as f:
    f.write(pi_chiffre_str)


#Exercice2
import csv

class Etudiant:
    def __init__(self, nom:str, annee_naissance:int, gpa:float, connais_python:bool):
        self.nom = nom
        self.annee_naissance = annee_naissance
        self.gpa = gpa
        self.connais_python = connais_python

    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, nom):
        if not isinstance(nom, str):
            raise TypeError("Entrer un str")
        self._nom = nom
    @property
    def annee_naissance(self):
        return self._annee_naissance
    @annee_naissance.setter
    def annee_naissance(self, annee_naissance):
        if not isinstance(annee_naissance, int):
            raise TypeError("Entrer un int")
        self._annee_naissance = annee_naissance
    @property
    def gpa(self):
        return self._gpa
    @gpa.setter
    def gpa(self, gpa):
        if not isinstance(gpa, float):
            raise TypeError("Entrer un float")
        if gpa < 0:
            raise ValueError("Entrer une valeur positive")
        self._gpa = gpa
    @property
    def connais_python(self):
        return self._connais_python
    @connais_python.setter
    def connais_python(self, connais_python):
        if not isinstance(connais_python, bool):
            raise TypeError("Entrer un bolléen")
        self._connais_python = connais_python

    def to_dict(self):
        return {"Nom" : self.nom, "Annee de naissance" : self.annee_naissance, "GPA" : self.gpa, "Connais PYTHON" : self.connais_python}

    def from_dict(d):
        return Etudiant(nom=d.get("Nom"), annee_naissance=d.get("Annee de naissance"), gpa=d.get("GPA"), connais_python=d.get("Connais PYTHON"))

class Groupe(Etudiant):
    def __init__(self):
        self.liste_etudiants = list()

    def ajouter_etudiant(self, object):
        self.liste_etudiants.append(object)

    def sauvegarder_csv(self, chemin):
        with open(chemin, "w", newline="") as file:
            writer = csv.DictWriter(file, ["Nom", "Annee de naissance", "GPA", "Connais PYTHON"])
            writer.writeheader()
            for etudiant in self.liste_etudiants:
                writer.writerow(etudiant.to_dict())

    def charger_csv(chemin):
        with open(chemin, "r") as file:
            content = file.read().split("\n")
            content = content[1:-1]
            obj_temporaire = Groupe()
            for etudiants in content:
                infos = etudiants.split(",")
                obj_temporaire.ajouter_etudiant(Etudiant(nom=infos[0], annee_naissance=int(infos[1]), gpa=float(infos[2]), connais_python=bool(infos[3])))
        return obj_temporaire


def Ex2():
    E1 = Etudiant(nom="Pestrimaux", annee_naissance=2002, gpa=1.0, connais_python=True)
    E2 = Etudiant(nom="Barrios", annee_naissance=2001, gpa=1.1, connais_python=False)
    groupe = Groupe()
    groupe.ajouter_etudiant(E1)
    groupe.ajouter_etudiant(E2)
    groupe.sauvegarder_csv("Groupe.csv")

    groupe2 = Groupe.charger_csv("Groupe.csv")
    return groupe

etudiant1=Etudiant("Florian",2002,2.8,False)
etudiant2=Etudiant("Kevin",2004,5.0,True)
etudiant3=Etudiant("Raph",2011,3.2,True)
etudiant4=Etudiant("Julian",2000,1.9,False)

etudiant1.to_dict()
etudiant2.to_dict()
etudiant3.to_dict()
etudiant4.to_dict()




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