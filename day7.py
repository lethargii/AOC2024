# Classe Operator
class Operator:
    def __init__(self, file_name: str) -> None:
        self.data_input: dict[int, list[int]] = {}
        for line in open(file_name).readlines():
            line_split = line.split()
            self.data_input[int(line_split[0][:-1])] = [int(k) for k in line_split[1:]]
        self.possibilities: dict[int, list[int]] = {}
        self.possible: int = 0

    def concatenate(self, a: int, b: int) -> int:
        return int(str(a) + str(b))

    def find_possibilitie(self, tab: list[int], cat: bool = False) -> list[int]:
        if len(tab) == 1:
            return tab
        possibilitie:list[int] = self.find_possibilitie(tab[:-1], cat = cat)
        res_tab: list[int] = []
        for val in possibilitie:
            res_tab += [tab[-1] * val]
            res_tab += [tab[-1] + val]
            if(cat):
                res_tab += [self.concatenate(val, tab[-1])]
        return res_tab

    def find_possibilities(self, cat: bool = False) -> None:
        for key in self.data_input:
            self.possibilities[key] = self.find_possibilitie(self.data_input[key], cat = cat)

    def nb_possible(self) -> None:
        for key in self.possibilities:
            if key in self.possibilities[key]:
                self.possible += key

    def solve_part_one(self) -> None:
        self.possible = 0
        self.find_possibilities()
        self.nb_possible()

    def solve_part_two(self) -> None:
        self.possible = 0
        self.find_possibilities(cat = True)
        self.nb_possible()

operator = Operator("input7")
operator.solve_part_one()

print(f"Day7, Part one : {operator.possible}")

operator.solve_part_two()

print(f"Day7, Part two : {operator.possible}")
