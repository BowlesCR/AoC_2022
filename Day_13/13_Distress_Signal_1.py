import fileinput
import json
import re


def main():

    acc = 0

    lines = list(fileinput.input())
    i = 1
    while lines:
        left = json.loads(lines.pop(0))
        right = json.loads(lines.pop(0))
        if validate(left, right):
            acc += i
        if lines:
            lines.pop(0)
        i += 1
    print(acc)


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
