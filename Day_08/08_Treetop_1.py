import fileinput


class Grid:
    def __init__(self, trees):
        self.trees = trees

    def height(self) -> int:
        return len(self.trees)

    def width(self) -> int:
        return len(self.trees[0])

    def is_visible(self, r, c) -> bool:

        # top or left edge
        if r == 0 or c == 0:
            return True

        # right or bottom edge
        if r == self.height() - 1 or c == self.width() - 1:
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


def main():
    grid = Grid([line.strip() for line in fileinput.input()])
    print(grid.count_visible())


if __name__ == "__main__":
    main()
