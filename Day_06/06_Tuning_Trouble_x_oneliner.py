import fileinput

LEN = 14


def main():
    for line in fileinput.input():
        print([i + 1 for i in range(LEN - 1, len(line)) if len(set(line[i - LEN + 1 : i + 1])) == LEN][0])


if __name__ == "__main__":
    main()
