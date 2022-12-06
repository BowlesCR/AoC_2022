import fileinput


def main():
    for line in fileinput.input():
        packets = [set(line[i - 13 : i + 1]) for i in range(13, len(line))]

        for i, packet in enumerate(packets, 14):
            if len(packet) == 14:
                print(i)
                break


if __name__ == "__main__":
    main()
