from helpers import read_file

if __name__ == "__main__":
    lines = read_file("resources/day1.txt")
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    result = 0
    for line in lines:
        digits = []
        i = 0
        while i < len(line):
            # the char is a digit
            if line[i].isdigit():
                digits.append(int(line[i]))
                i += 1
                continue
            # the char may be start of a word
            for idx, word in enumerate(words):
                if line[i : i + len(word)] == word:
                    digits.append(idx + 1)
                    # overlap of the last character of the previous word, and the start of the next
                    # eg. oneight
                    # for general correctness, this should be i += 1, but this is an optimization possible given the correct set of words
                    i += len(word) - 2
            i += 1
        first, last = digits[0], digits[-1]
        result += first * 10 + last
    print(result)
