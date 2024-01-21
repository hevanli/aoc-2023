lines = []
with (open("input3.txt")) as file:
    lines = [line.strip() for line in file.readlines()]

print(len(lines[23]))
print(lines[23][130])
