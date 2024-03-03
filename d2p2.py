from collections import defaultdict
from functools import reduce

from helpers import read_file

if __name__ == "__main__":
    input = read_file("resources/day2.txt")

    def get_round_counts(round: str) -> dict[int, int]:
        color_counts = defaultdict(lambda: 0)

        round_color_counts = round.split(",")
        for count_color in round_color_counts:
            count, color = count_color.strip().split(" ")
            color_counts[color] += int(count)
        return color_counts

    result = 0
    for idx, line in enumerate(input):
        game_id = idx + 1
        rounds = line.split(":")[1].strip().split(";")
        required_color_count = {"red": 0, "green": 0, "blue": 0}
        for round in rounds:
            round_counts = get_round_counts(round)
            for color, count in round_counts.items():
                required_color_count[color] = max(count, required_color_count[color])
        game_power = reduce(lambda x, y: x * y, required_color_count.values())
        result += game_power
    print(result)
