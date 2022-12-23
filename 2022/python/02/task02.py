import re

map_rock_paper_scissors = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
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
        mapped_game.append(mapped_game[0]-mapped_game[1])

        game_score += mapped_game[1]
        if mapped_game[2] == 0:
            game_score += 3
        elif (mapped_game[2] == -1) or (mapped_game[2] == 2):
            game_score += 6

        mapped_game.append(game_score)
        games.append(mapped_game)

    print(games)
    games_score_sum = sum([game[3] for game in games])
    print(games_score_sum)


if __name__ == "__main__":
    main()
