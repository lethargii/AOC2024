from InputMat import InputMat

class Vec2Int:
    def __init__(self, x:int = 0, y:int = 0) -> None:
        self.x: int = x
        self.y: int = y
    def __add__(self, vec2):
        return Vec2Int(self.x + vec2.x, self.y + vec2.y)
    def __sub__(self, vec2):
        return Vec2Int(self.x - vec2.x, self.y - vec2.y)
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

class Antennas(InputMat):
    def __init__(self, file_name: str, integer: bool = False, day: int = 1) -> None:
        super().__init__(file_name, integer, day)
        self.antinodes: list[Vec2Int] = []
        self.height: int = len(self.data)
        self.width: int = len(self.data[0])
        self.frequencies: dict[str, list[Vec2Int]] = {}
        self.solution(1)
    
    def get_frequencies(self) -> None:
        for i in range(self.height):
            for j in range(self.width):
                if self.data[i][j] != ".":
                    if self.data[i][j] not in self.frequencies:
                        self.frequencies[self.data[i][j]] = [Vec2Int(i, j)]
                    else:
                        self.frequencies[self.data[i][j]] += [Vec2Int(i, j)]
        print(self.frequencies)

    def get_antinode(self, u: Vec2Int, v: Vec2Int) -> list[Vec2Int]:
        a = v + (v - u)
        b = u + (u - v)
        return [w for w in [a, b] if self.is_valid_antinode(w)]

    def get_antinodes(self) -> None:
        for key in self.frequencies:
            for i in range(len(self.frequencies[key]) - 1):
                for j in range(i + 1, len(self.frequencies[key])):
                    self.antinodes += [antinode for antinode in self.get_antinode(self.frequencies[key][i], self.frequencies[key][j]) if antinode not in self.antinodes]
        self.res = len(self.antinodes)
        print(self.antinodes)

    def is_valid_antinode(self, u: Vec2Int):
        return u.x >= 0 and u.x < self.width and u.y >= 0 and u.y < self.height

    def solve(self, part: int) -> None:
        self.get_frequencies()
        self.get_antinodes()
        super().solve(part)

antennas = Antennas("input8_test", False, 8)
antennas = Antennas("input8", False, 8)
