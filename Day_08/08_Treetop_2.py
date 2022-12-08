import fileinput


class Grid:
    def __init__(self, trees):
        self.trees = trees

    def height(self) -> int:
        return len(self.trees)

    def width(self) -> int:
        return len(self.trees[0])

    def is_visible(self, r: int, c: int) -> bool:

        # top or left edge
        if r == 0 or c == 0:
            return True

        # right or bottom edge
        if r == self.height() or c == self.width():
            return True

        # left
        if all([tree < self.trees[r][c] for tree in self.trees[r][:c]]):
            return True

        # right
        if all([tree < self.trees[r][c] for tree in self.trees[r][c + 1 :]]):
            return True

        # top
        if all([self.trees[y][c] < self.trees[r][c] for y in range(0, r)]):
            return True

        # bottom
        if all([self.trees[y][c] < self.trees[r][c] for y in range(r + 1, self.height())]):
            return True

        return False

    def count_visible(self) -> int:
        count = 0
        for r in range(self.height()):
            for c in range(self.width()):
                if self.is_visible(r, c):
                    count += 1
        return count

    def score(self, r: int, c: int) -> int:
        # top or left edge
        if r == 0 or c == 0:
            return 0

        # right or bottom edge
        if r == self.height() - 1 or c == self.width() - 1:
            return 0

        prod = 1

        # left
        i = 1
        for i, h in enumerate(self.trees[r][c - 1 :: -1], 1):
            if h >= self.trees[r][c]:
                break
        prod *= i

        # right
        i = 1
        for i, h in enumerate(self.trees[r][c + 1 :], 1):
            if h >= self.trees[r][c]:
                break
        prod *= i

        # up
        i = 1
        for i, h in enumerate([self.trees[y][c] for y in range(r - 1, -1, -1)], 1):
            if h >= self.trees[r][c]:
                break
        prod *= i

        # down
        i = 1
        for i, h in enumerate([self.trees[y][c] for y in range(r + 1, self.height())], 1):
            if h >= self.trees[r][c]:
                break
        prod *= i
        return prod

    def max_score(self) -> int:
        max_score = 0
        for r in range(self.height()):
            for c in range(self.width()):
                score = self.score(r, c)
                max_score = max(max_score, score)
        return max_score


def main():
    grid = Grid([line.strip() for line in fileinput.input()])

    print(grid.max_score())


if __name__ == "__main__":
    main()
