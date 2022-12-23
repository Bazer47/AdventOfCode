import re

winning_combs = [[1, 2], [2, 3], [3, 1]]
loosing_combs = [comb[::-1] for comb in winning_combs]

map_rock_paper_scissors = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 0,
    "Y": 3,
    "Z": 6
}

INPUT_FILE = "input.txt"


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    games = []
    for line in lines:
        game_score = 0
        game = re.search(r"([A-Z]) ([A-Z])", line)
        mapped_game = [*map(map_rock_paper_scissors.get, game.groups())]

        if mapped_game[1] == 0:
            comb = [c for c in loosing_combs if mapped_game[0] == c[0]][0]    
        elif mapped_game[1] == 3:
            game_score += 3
            comb = [mapped_game[0], mapped_game[0]]
        elif mapped_game[1] == 6:
            game_score += 6
            comb = [c for c in winning_combs if mapped_game[0] == c[0]][0]
        else:
            raise ValueError(f"Uknown value: {mapped_game[1]}")

        game_score += comb[1]

        mapped_game.extend((comb[1], game_score))
        games.append(mapped_game)

    # print(games)
    games_score_sum = sum([game[3] for game in games])
    print(games_score_sum)


if __name__ == "__main__":
    main()
