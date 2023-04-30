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
    def nom(self, annee_naissance):
        if not isinstance(annee_naissance, int):
            raise TypeError("Entrez un int")
        self.__annee_naissance=annee_naissance

    @property
    def gpa(self):
        return self.__gpa
    @gpa.setter
    def nom(self, gpa):
        if not isinstance(gpa, float):
            raise TypeError("Entrez un float")
        self.__gpa=gpa

    @property
    def connais_python(self):
        return self.__connais_python
    @connais_python.setter
    def nom(self, connais_python):
        if not isinstance(connais_python, bool):
            raise TypeError("Entrez un booléen")
        self.__connais_python=connais_python

    def to_dict(self):
         return {"nom": self.nom , "annee_naissance":self.annee_naissance,"gpa":self.gpa,"connais_python":self.connais_python}

class Groupe(Etudiant):

    def __init__(self,nom,annee_naissance,gpa,connais_python):
        super.__init__(self,nom,annee_naissance,gpa,connais_python)

    def sauvagrder_csv(self,chemin):





#Exercice 3