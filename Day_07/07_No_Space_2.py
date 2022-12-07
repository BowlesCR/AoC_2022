import fileinput


class FS:
    def __init__(self):
        self.tree: dict[str, list[str | int]] = {"/": []}
        self.sizes: dict[str, int] = {}

    def size(self, path: str):
        total = 0
        for item in self.tree[path]:
            if isinstance(item, int):
                total += item
            else:
                total += self.size(f"{path if path != '/' else ''}/{item}")
        self.sizes[path] = total
        return total


def main():

    pwd: list[str] = []
    fs = FS()

    for line in fileinput.input():
        tokens = line.split()
        if tokens[0] == "$":  # command mode
            if tokens[1] == "cd":
                if tokens[2] == "/":
                    pwd = [""]
                elif tokens[2] == "..":
                    pwd.pop()
                else:
                    pwd.append(tokens[2])
            elif tokens[1] == "ls":
                continue
        else:  # output mode
            path = "/".join(pwd)
            if tokens[0] == "dir":
                fs.tree[path if path else "/"].append(tokens[1])
                fs.tree[f"{path}/{tokens[1]}"] = []
            else:
                fs.tree[path if path else "/"].append(int(tokens[0]))

    target = 30000000 - (70000000 - fs.size("/"))
    print(sorted([fs.sizes[dir] for dir in fs.sizes if dir != "/" and fs.sizes[dir] >= target])[0])


if __name__ == "__main__":
    main()
