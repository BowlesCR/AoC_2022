from collections import namedtuple
import fileinput


def dist(head: tuple[int, int], tail: tuple[int, int]) -> int:
    # nonstandard distance formula -- diagonals count as one step.

    if head == tail:
        # no real point in this, but why not
        return 0
    if (head[0] - tail[0]) ** 2 <= 1 and (head[1] - tail[1]) ** 2 <= 1:
        return 1
    else:
        # no point in actually calculating
        return 2


def main():
    Pos = namedtuple("Pos", "r c")
    knots: list[Pos] = [Pos(0, 0) for _ in range(10)]
    tail_positions: set[Pos] = set()
    tail_positions.add(knots[-1])

    line: str
    for line in fileinput.input():
        direction, steps = line.strip().split()
        steps = int(steps)

        sign: int = -1 if direction in ["L", "U"] else 1

        for _ in range(steps):

            if direction in ["U", "D"]:
                knots[0] = knots[0]._replace(r=knots[0].r + sign)
            elif direction in ["L", "R"]:
                knots[0] = knots[0]._replace(c=knots[0].c + sign)
            else:
                assert False

            for i in range(1, len(knots)):
                if dist(knots[i - 1], knots[i]) > 1:
                    dr = knots[i - 1].r - knots[i].r
                    dc = knots[i - 1].c - knots[i].c

                    # either/or, both
                    if dr != 0:
                        knots[i] = knots[i]._replace(r=knots[i].r + dr // abs(dr))  # clamp to 1 unit
                    if dc != 0:
                        knots[i] = knots[i]._replace(c=knots[i].c + dc // abs(dc))  # clamp to 1 unit

                    if i + 1 == len(knots):  # did we just move the tail?
                        tail_positions.add(knots[-1])
                else:
                    break  # if this knot didn't need to move, then the ones behind it don't either.

    print(len(tail_positions))


if __name__ == "__main__":
    main()
