# Exercice 1 
semaine = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","samedi","Dimache"]
print ("",semaine[0:5]) 
print("",semaine[5:])
print("Dernier jour de la semaine : ",semaine[6:])
print("Dernier jour de la semaine : ",semaine[-1:])
print("Inverser : ",semaine[ ::-1 ] )
# Exercice 2 
Hiver=["decembre","janvier","fevrier"]
Printemps = ["Mars","April ", "May"]
ete = ["juin","juillet","Aout"]
Automne = ["septembre" , "octobre ", "novembre"]
saisons  = [Automne , Hiver , Printemps , ete ]
print("Saisons : ", saisons[:][1])
# Exercice 3
x = range(11)
for n in x:
  print(n * 9)
# list = list(range(0,91,9))
# Exercice 4
ex = len(range(2,10001,2))
print(ex)

# Partie 3 exercice1
Animal = ["Vache ","Souris","Levure","Bacterie"]
for n in Animal:
    print(n)
# methode2
print("\n".join(Animal))

