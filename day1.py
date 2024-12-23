liste1 = []
liste2 = []
data = open("input1")
for line in data.readlines():
    valeurs = line.split(sep="   ")
    liste1.append(int(valeurs[0]))
    liste2.append(int(valeurs[1]))
res = 0
for i in range(len(liste1)):
    val1 = max(liste1)
    liste1.remove(val1)
    val2 = max(liste2)
    liste2.remove(val2)
    res += abs(val1-val2)
print(f"Day1, Part one : {res}")

liste1 = []
liste2 = []
res = 0
data = open("input1")
for line in data.readlines():
    valeurs = line.split(sep="   ")
    liste1.append(int(valeurs[0]))
    liste2.append(int(valeurs[1]))
for val in liste1:
    res += liste2.count(val)*val
print(f"Day1, Part two : {res}")
