data = open("input4")
data_input: list[list[str]] = []
for line in data.readlines():
    data_input.append([character for character in line if character != "\n"])

class Cross:
    def __init__(self, mot: list[str], data_input: list[list[str]]) -> None:
        self.res: int = 0
        self.compteur: list[int] = [0, 0, 0, 0]
        self.mot: list[str] = mot
        self.data_input: list[list[str]] = data_input
        self.nlig: int = len(data_input)
        self.ncol: int = len(data_input[0])
    def update_res(self) -> None:
        for i in range(len(self.compteur)):
            if self.compteur[i] == len(self.mot):
                self.res += 1
                self.compteur[i] = 0
    def update_compteur(self, i: int, caractere: str, reverse: bool = False) -> None:
        if self.mot[reverse*(len(self.mot)-1) + (1-reverse*2)*self.compteur[i]] == caractere:
            self.compteur[i] += 1
        else:
            self.compteur[i] = 0
    def reset_compteur(self):
        for i in range(len(self.compteur)):
            self.compteur[i] = 0
    def crosswords(self) -> None:
        for i in range(self.nlig):
            for j in range(self.ncol):
                self.update_compteur(0, self.data_input[i][j])
                self.update_compteur(1, self.data_input[i][j], reverse = True)
                self.update_res()
            self.reset_compteur()
        for j in range(self.ncol):
            for i in range(self.nlig):
                self.update_compteur(0, self.data_input[i][j])
                self.update_compteur(1, self.data_input[i][j], reverse = True)
                self.update_res()
            self.reset_compteur()
        for i in range(self.nlig-len(self.mot)+4):
            for k in range(min(self.nlig - i, self.ncol)):
                self.update_compteur(0, self.data_input[i+k][k])
                self.update_compteur(1, self.data_input[i+k][k], reverse = True)
                self.update_compteur(2, self.data_input[self.nlig - 1 - i - k][k])
                self.update_compteur(3, self.data_input[self.nlig - 1 - i - k][k], reverse = True)
                self.update_res()
            self.reset_compteur()
        for j in range(1, self.ncol-len(self.mot)+4):
            for k in range(min(self.nlig, self.ncol-j)):
                self.update_compteur(0, self.data_input[k][j+k])
                self.update_compteur(1, self.data_input[k][j+k], reverse = True)
                self.update_compteur(2, self.data_input[self.nlig - 1 - k][j + k])
                self.update_compteur(3, self.data_input[self.nlig - 1 - k][j + k], reverse = True)
                self.update_res()
            self.reset_compteur()



cross: Cross = Cross(['X', 'M', 'A', 'S'], data_input)
cross.crosswords()
print(f"Day1, Part one : {cross.res}")

print(f"Day1, Part two : {cross.res}")
