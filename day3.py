data = open("input3")
data_input = data.read()
res = 0
for mul in data_input.split(sep = "mul("):
    parenthese = mul.split(sep = ")")[0]
    comma = parenthese.split(sep = ",")
    if len(comma) == 2 and comma[0].isnumeric() and comma[1].isnumeric():
        res += int(comma[0])*int(comma[1])
print(f"Day1, Part one : {res}")

res = 0
do = True
instructions = data_input.split(sep = "(")
for i in range(1, len(instructions)):
    if do and instructions[i-1][-3:] == "mul":
        parenthese = instructions[i].split(")")[0]
        comma = parenthese.split(sep = ",")
        if len(comma) == 2 and comma[0].isnumeric() and comma[1].isnumeric():
            res += int(comma[0])*int(comma[1])
    elif instructions[i-1][-2:] == "do" and instructions[i][0] == ")":
        do = True
    elif instructions[i-1][-5:] == "don't" and instructions[i][0] == ")":
        do = False
print(f"Day1, Part two : {res}")
