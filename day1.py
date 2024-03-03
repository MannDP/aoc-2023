from helpers import read_file

if __name__ == "__main__":
    lines = read_file("resources/day1.txt")
    result = 0
    for l in lines:
        digits = []
        for d in l:
            if d.isdigit():
                if len(digits) == 2:
                    digits.pop()
                digits.append(int(d))
        if len(digits) != 2:
            digits.append(digits[0])
        number = digits[0] * 10 + digits[1]
        result += number
    print(result)
