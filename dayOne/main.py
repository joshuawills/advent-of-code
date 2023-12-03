#!/usr/bin/env python3

import re

REGEX=r"one|two|three|four|five|six|seven|eight|nine"

# def replace(x: str):
#     x = x.replace("nine", "9")
#     x = x.replace("eight", "8")
#     x = x.replace("seven", "7")
#     x = x.replace("six", "6")
#     x = x.replace("five", "5")
#     x = x.replace("four", "4")
#     x = x.replace("three", "3")
#     x = x.replace("two", "2")
#     x = x.replace("one", "1")
#     return x

def main():
    
    sum = 0
    with open("fileTwo.txt", "r") as f:
        for x in f.readlines():
            x = x.strip()
            numbers = re.findall(f"[0-9]+|{REGEX}", x)
            numbers = "".join(numbers)
            # numbers = replace(numbers)
            # val = int(numbers[0]) * 10 + int(numbers[-1])
            # sum += val
            print(f"{x}: {numbers}")


        print(sum)

if __name__ == "__main__":
    main()
