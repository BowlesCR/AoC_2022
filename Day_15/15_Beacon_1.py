import fileinput
import re


def main():
    re_parse = re.compile(r"=(-?\d+)")

    excl: set[tuple[int, int]] = set()
    sensors: set[tuple[int, int]] = set()
    beacons: set[tuple[int, int]] = set()

    for line in fileinput.input():
        sx, sy, bx, by = (int(i) for i in re_parse.findall(line))

        sensors.add((sx, sy))
        beacons.add((bx, by))

        ROW = 2000000

        md = abs(sx - bx) + abs(sy - by)

        p_md = md - abs(sy - ROW)

        for x in range(sx - p_md, sx + p_md + 1):
            md_test = abs(sx - x) + abs(sy - ROW)
            if md_test == 0 or md_test > md:
                continue

            excl.add((x, ROW))

    print(len(excl.difference(beacons)))


if __name__ == "__main__":
    main()
