import fileinput


def score(opp, me) -> int:
    s = ord(me) - ord("A") + 1

    if opp == me:  # Draw
        return s + 3

    if opp == "A" and me == "C":  # Rock, Scissors -- Lose
        return s
    elif opp == "B" and me == "A":  # Paper, Rock -- Lose
        return s
    elif opp == "C" and me == "B":  # Scissors, Paper -- Lose
        return s

    if opp == "C" and me == "A":  # Scissors, Rock -- Win
        return s + 6
    elif opp == "A" and me == "B":  # Rock, Paper -- Win
        return s + 6
    elif opp == "B" and me == "C":  # Paper, Scissors -- Win
        return s + 6

    return 0


def shape(opp, res):
    if res == "Y":
        return opp

    elif res == "X":
        if opp == "A":
            return "C"
        elif opp == "B":
            return "A"
        elif opp == "C":
            return "B"

    elif res == "Z":
        if opp == "A":
            return "B"
        elif opp == "B":
            return "C"
        elif opp == "C":
            return "A"


total = 0
for line in fileinput.input():
    (opp, res) = line.strip().split()
    me = shape(opp, res)
    total += score(opp, me)
print(total)
