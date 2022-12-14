import fileinput
import functools
import json
import re


def main():
    lines = list(fileinput.input())

    packets = []
    while lines:
        packets.append(json.loads(lines.pop(0)))
        packets.append(json.loads(lines.pop(0)))
        if lines:
            lines.pop(0)

    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=functools.cmp_to_key(cmp))

    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))


def cmp(left: list, right: list) -> int:
    if left == right:
        return 0
    else:
        return -1 if validate(left, right) else 1


def validate(left: list | int, right: list | int) -> bool | None:
    if isinstance(left, int) and isinstance(right, int):
        left: int
        right: int
        return left < right if left != right else None
    elif isinstance(left, list) and isinstance(right, list):
        left: list
        right: list

        for i in range(min(len(left), len(right))):
            r = validate(left[i], right[i])
            if r is not None:
                return r
        return None if len(left) == len(right) else len(left) < len(right)
    elif isinstance(left, int):
        left: int
        right: list
        return validate([left], right)
    elif isinstance(right, int):
        left: list
        right: int
        return validate(left, [right])


re_striplist = re.compile(r"^\[(.*)]\n?$")
re_split = re.compile(r"(\d+|\[.*])")

if __name__ == "__main__":
    main()
