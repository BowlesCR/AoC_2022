import fileinput
import re

parser = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)\n?$")

count = 0

for line in fileinput.input():
    match = parser.match(line)
    r1 = set(range(int(match.group(1)), int(match.group(2)) + 1))
    r2 = set(range(int(match.group(3)), int(match.group(4)) + 1))

    overlap = r1.intersection(r2)
    if len(overlap) > 0:
        count += 1
print(count)
