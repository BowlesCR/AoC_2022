import fileinput


def score(opp, me) -> int:
    s = ord(me) - ord("A") + 1

    if opp == me:  # Draw
        return s + 3

    # Lose conditions
    if (opp == "A" and me == "C") or (opp == "B" and me == "A") or (opp == "C" and me == "B"):
        return s

    # Win conditions
    if (opp == "C" and me == "A") or (opp == "A" and me == "B") or (opp == "B" and me == "C"):
        return s + 6

    return 0


def main():
    total = 0
    for line in fileinput.input():
        (opp, me) = line.strip().split()
        total += score(opp, me)
    print(total)


if __name__ == "__main__":
    main()
