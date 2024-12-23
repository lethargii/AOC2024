class InputMat:
    def __init__(self, file_name: str, integer: bool = False, day: int = 1) -> None:
        self.data: list[list[str]] = []
        for line in open(file_name).readlines():
            self.data.append([character for character in line if character != "\n"])
        self.res: int = 0
        self.day: int = day

    def solve(self, part: int) -> None:
        self.res = 0

    def solution(self, part: int) -> None:
        self.solve(part = part)
        parts: list[str] = ["one", "two"]
        print(f"Day {self.day}, Part {parts[part - 1]} : {self.res}")

