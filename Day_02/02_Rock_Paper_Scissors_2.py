import fileinput


def score(opp, me) -> int:

    me = chr(ord(me) - ord("X") + ord("A"))
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


total = 0
for line in fileinput.input():
    (opp, me) = line.strip().split()
    total += score(opp, me)
print(total)
