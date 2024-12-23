data_input = []
data = open("input2")
for line in data.readlines():
    data_input.append([int(valeur) for valeur in line.split(sep = " ")])
res = [True for i in range(len(data_input))]

def increases(liste: list[int]) -> bool:
    return not (liste != sorted(liste) and liste != sorted(liste, reverse = True))

def is_safe(liste: list[int]) -> bool:
    if not increases(liste):
        return False
    else:
        for i in range(len(liste)-1):
            if not (1 <= abs(liste[i] - liste[i+1]) <= 3):
                return False
    return True

for i in range(len(res)):
    res[i] = is_safe(data_input[i])

print(f"Day1, Part one : {sum(res)}")

def almost_safe(liste):
    if is_safe(liste):
        return True
    for i in range(len(liste)):
        if is_safe(liste[:i]+liste[i+1:]):
            return True
    return False

for i in range(len(res)):
    res[i] = almost_safe(data_input[i])
print(f"Day1, Part two : {sum(res)}")
