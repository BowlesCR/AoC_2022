import fileinput
import re
from functools import lru_cache


class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


class Scan:
    def __init__(self):
        self.lines: list[tuple[range, range]] = []
        self.max_y = 0
        self.sand: set[tuple[int, int]] = set()

    def add_line(self, p1: Point, p2: Point) -> None:
        x = range(min(p1.x, p2.x), max(p1.x, p2.x) + 1)
        y = range(min(p1.y, p2.y), max(p1.y, p2.y) + 1)

        self.lines.append((x, y))

        self.max_y = max(self.max_y, max(y))

    @lru_cache
    def point_on_line(self, x: int, y: int) -> bool:
        for line in self.lines:
            if x in line[0] and y in line[1]:
                return True
        return False

    def add_sand(self) -> bool:
        x, y = (500, 0)

        while True:
            if y < self.max_y + 1 and (x, y + 1) not in self.sand and not self.point_on_line(x, y + 1):
                # Straight down
                y += 1
            elif y < self.max_y + 1 and (x - 1, y + 1) not in self.sand and not self.point_on_line(x - 1, y + 1):
                # Down-left
                x -= 1
                y += 1
            elif y < self.max_y + 1 and (x + 1, y + 1) not in self.sand and not self.point_on_line(x + 1, y + 1):
                # Down-right
                x += 1
                y += 1
            else:
                # Settled
                if x == 500 and y == 0:
                    return False

                self.sand.add((x, y))
                return True


def main():
    re_points = re.compile(r"(\d+),(\d+)")
    scan = Scan()

    for line in fileinput.input():
        points = re_points.findall(line)
        for i in range(1, len(points)):
            p1 = Point(int(points[i - 1][0]), int(points[i - 1][1]))
            p2 = Point(int(points[i][0]), int(points[i][1]))
            scan.add_line(p1, p2)

    while scan.add_sand():
        pass

    print(len(scan.sand) + 1)


if __name__ == "__main__":
    main()
