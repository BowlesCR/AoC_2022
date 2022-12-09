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
    head: Pos = Pos(0, 0)
    tail: Pos = Pos(0, 0)
    tail_positions: set[Pos] = set()
    tail_positions.add(tail)

    line: str
    for line in fileinput.input():
        direction, steps = line.strip().split()
        steps = int(steps)

        sign: int = -1 if direction in ["L", "U"] else 1

        for _ in range(steps):

            if direction in ["U", "D"]:
                head = head._replace(r=head.r + sign)
            elif direction in ["L", "R"]:
                head = head._replace(c=head.c + sign)
            else:
                assert False

            if dist(head, tail) > 1:
                dr = head.r - tail.r
                dc = head.c - tail.c

                # either/or, both
                if dr != 0:
                    tail = tail._replace(r=tail.r + dr // abs(dr))  # clamp to 1 unit
                if dc != 0:
                    tail = tail._replace(c=tail.c + dc // abs(dc))  # clamp to 1 unit

                tail_positions.add(tail)

    print(len(tail_positions))


if __name__ == "__main__":
    main()
