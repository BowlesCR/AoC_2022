import fileinput


def main():
    for line in fileinput.input():
        packets = [set(line[i - 3 : i + 1]) for i in range(3, len(line))]

        for i, packet in enumerate(packets, 4):
            if len(packet) == 4:
                print(i)
                break


if __name__ == "__main__":
    main()
