from collections import defaultdict

from helpers import read_file

if __name__ == "__main__":
    input = read_file("resources/day2.txt")

    red_total, green_total, blue_total = 12, 13, 14

    def is_possible(r: int, g: int, b: int) -> bool:
        return r <= red_total and g <= green_total and b <= blue_total

    result = 0
    for idx, line in enumerate(input):
        game_id = idx + 1
        rounds = line.split(":")[1].strip().split(";")
        possible = True
        for round in rounds:
            color_counts = defaultdict(lambda: 0)

            round_color_counts = round.split(",")
            for color_count in round_color_counts:
                value, color = color_count.strip().split(" ")
                color_counts[color] += int(value)

            if not is_possible(
                color_counts["red"], color_counts["green"], color_counts["blue"]
            ):
                possible = False
                break
        if possible:
            result += game_id
    print(result)
