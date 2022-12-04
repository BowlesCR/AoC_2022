import fileinput

total = 0

lines: list[str] = list(fileinput.input())
assert len(lines) % 3 == 0
for i in range(0, len(lines), 3):
    overlap = set(lines[i].strip()).intersection(lines[i + 1].strip()).intersection(lines[i + 2].strip())
    assert len(overlap) == 1
    print(overlap)
    item: str = overlap.pop()
    if item.islower():
        total += ord(item) - ord("a") + 1
    else:
        total += ord(item) - ord("A") + 27
print(total)
