import fileinput
import sys
from queue import Queue


class Hill:
    def __init__(self, grid: list[list[int]], end: tuple[int, int]):
        self.grid = grid
        self.end = end

        self.starts: list[tuple[int, int]] = []
        for r in range(len(self.grid)):
            for c, h in enumerate(self.grid[r]):
                if h == 0:
                    self.starts.append((r, c))

        self.bestpath: int = sys.maxsize

    def path(self, start) -> int:
        queue = Queue()
        queue.put(start)
        visited = set()
        visited.add(start)

        parent = dict()
        parent[start] = (None, 0)

        path_found = False
        while queue.qsize() > 0:
            pos = queue.get()
            r, c = pos
            if pos == self.end:
                path_found = True
                break

            steps = parent[pos][1]
            if steps >= self.bestpath:
                break

            for nr in range(max(0, r - 1), min(r + 2, len(self.grid))):
                for nc in range(max(0, c - 1), min(c + 2, len(self.grid[0]))):
                    if nr != r and nc != c:  # can't move diagonally
                        continue
                    n = (nr, nc)
                    if n in visited:
                        continue
                    if self.grid[nr][nc] > self.grid[r][c] + 1:
                        continue

                    queue.put(n)
                    parent[n] = (pos, parent[pos][1] + 1)
                    visited.add(n)

        if path_found:
            return parent[self.end][1]
        else:
            return sys.maxsize

    def any_path(self):
        for start in self.starts:
            self.bestpath = min(self.bestpath, self.path(start))
        return self.bestpath


def main():
    grid = [list(line.strip()) for line in fileinput.input()]
    end = None
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "S":
                grid[r][c] = 0
            elif grid[r][c] == "E":
                end = (r, c)
                grid[r][c] = 25
            else:
                grid[r][c] = ord(grid[r][c]) - ord("a")
    hill = Hill(grid, end)

    print(hill.any_path())


if __name__ == "__main__":
    main()
