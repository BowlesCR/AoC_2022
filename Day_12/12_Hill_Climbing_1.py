import fileinput
from queue import Queue


class Hill:
    def __init__(self, grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
        self.grid = grid
        self.start = start
        self.end = end

    def path(self):
        queue = Queue()
        queue.put(self.start)
        visited = set()
        visited.add(self.start)

        parent = dict()
        parent[self.start] = None

        path_found = False
        while queue:
            pos = queue.get()
            r, c = pos
            if pos == self.end:
                path_found = True
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
                    parent[n] = pos
                    visited.add(n)

        assert path_found
        path = []
        end = self.end
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end])
            end = parent[end]
        path.reverse()
        print(len(path) - 1)


def main():
    grid = [list(line.strip()) for line in fileinput.input()]
    start = None
    end = None
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "S":
                start = (r, c)
                grid[r][c] = 0
            elif grid[r][c] == "E":
                end = (r, c)
                grid[r][c] = 25
            else:
                grid[r][c] = ord(grid[r][c]) - ord("a")
    hill = Hill(grid, start, end)

    hill.path()


if __name__ == "__main__":
    main()
