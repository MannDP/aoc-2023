from helpers import read_file

if __name__ == "__main__":
    lines = read_file("resources/day1.txt")
    result = 0
    for line in lines:
        digits = []
        for d in line:
            if d.isdigit():
                if len(digits) == 2:
                    digits.pop()
                digits.append(int(d))
        number = digits[0] * 10 + digits[-1]
        result += number
    print(result)
