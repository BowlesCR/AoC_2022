import fileinput

elves = []

acc = 0
for i in fileinput.input():
    if i.strip().isnumeric():
        acc += int(i)
    else:
        elves.append(acc)
        acc = 0

print(max(elves))
