import fileinput

total = 0

line: str
for line in fileinput.input():
    line = line.strip()
    comp1 = set(line[: len(line) // 2])
    comp2 = set(line[len(line) // 2 :])

    overlap = comp1.intersection(comp2)
    assert len(overlap) == 1

    item: str = overlap.pop()
    if item.islower():
        total += ord(item) - ord("a") + 1
    else:
        total += ord(item) - ord("A") + 27
print(total)
