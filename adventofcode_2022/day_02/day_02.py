game_wins = 0
part_2_wins = 0


def part_1_game_score(them, me):

    if them == me:
        # Draw = 3
        return me + 3

    elif (them == 1 and me == 2) or (them == 2 and me == 3) or (them == 3 and me == 1):
        # 6 if I won
        return me + 6

    else:
        # 0 if I lost
        return me + 0


def part_2_game_score(them, how):
    if how == "Win":
        if them == 1:
            return them, 2
        if them == 2:
            return them, 3
        if them == 3:
            return them, 1

    if how == "Lose":
        if them == 1:
            return them, 3
        if them == 2:
            return them, 1
        if them == 3:
            return them, 2

    if how == "Draw":
        return them, them


for game in list(open("input.txt", "r").readlines()):
    if "X" in game:
        part_2_result = "Lose"
    if "Y" in game:
        part_2_result = "Draw"
    if "Z" in game:
        part_2_result = "Win"

    game = game.replace("A", "1")
    game = game.replace("X", "1")
    game = game.replace("B", "2")
    game = game.replace("Y", "2")
    game = game.replace("Z", "3")
    game = game.replace("C", "3")

    them, me = game.split(" ")

    game_wins += part_1_game_score(int(them), int(me))
    part_2_wins += part_1_game_score(*part_2_game_score(int(them), part_2_result))


print(f"total: {game_wins}")
print(f"Part 2 Method: {part_2_wins}")
