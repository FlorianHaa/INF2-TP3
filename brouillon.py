import math
with open("poeme.txt","r") as f:
    contenu = f.read()
contenu=contenu.split(" ")
liste=[]
for element in contenu:
    for lettre in element:
        if lettre == " " or lettre == "\n" or lettre == "'" or lettre == "!":
            lettre=""

print(contenu)






#     for element in contenu:
#         for lettre in element:
#             if lettre == " " or lettre == "\n" or lettre == "'" or lettre == "!":
#                 liste_des_mots+=[mots]
#                 mots=" "
#             else :
#                 mots +=lettre
# print(liste_des_mots)
# py=([len(element) for element in liste_des_mots])
# print(py)
# pi=str(math.pi)
# print(pi)
# pi=pi.replace(".","")
# pi=pi.split("2")
#
# pi=list(pi)
# print(pi)
#
#
