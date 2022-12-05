import fileinput
import re

r_crates = re.compile(r"(\[[A-Z] ?]| {3,4})")
r_numbers = re.compile(r"^(?: \d {0,2}){1,9}\n$")
r_instruction = re.compile(r"^move (\d+) from (\d) to (\d)\n?$")

stacks: list[list[str]] = [[] for i in range(9)]

state = "crates"
for line in fileinput.input():
    if state == "crates":
        if r_numbers.match(line):
            state = "blank"
            continue

        match = r_crates.findall(line)
        if match:
            m: str
            for i, m in enumerate(match):
                m = m.strip(" []")
                if m:
                    stacks[i].append(m)
        else:
            assert False, "Parser failure reading crates"
        continue
    elif state == "blank":
        assert line == "\n", "Parser failure expecting blank line"
        for stack in stacks:
            stack.reverse()
        state = "instructions"
        continue
    elif state == "instructions":
        match = r_instruction.match(line)
        assert match, "Parser failure reading instructions"
        for i in range(int(match.group(1))):
            crate: str = stacks[int(match.group(2)) - 1].pop()
            stacks[int(match.group(3)) - 1].append(crate)

        continue

    assert False, "Parser fallthrough"


print("".join([stack.pop() for stack in stacks if stack]))
