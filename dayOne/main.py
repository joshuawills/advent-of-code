#!/usr/bin/env python3

import re

REGEX=r"one|two|three|four|five|six|seven|eight|nine"

def replace(x):

    for n, char in enumerate(x):
        if char == "nine":
            x[n] = "9"
        if char == "eight":
            x[n] = "8"
        if char == "seven":
            x[n] = "7"
        if char == "six":
            x[n] = "6"
        if char == "five":
            x[n] = "5"
        if char == "four":
            x[n] = "4"
        if char == "three":
            x[n] = "3"
        if char == "two":
            x[n] = "2"
        if char == "one":
            x[n] = "1"
    
    return x

def main():
    
    sum = 0
    with open("fileTwo.txt", "r") as f:
        for x in f.readlines():
            x = x.strip()
            numbers = re.findall(f"[0-9]+|{REGEX}", x)
            numbers = [x.strip() for x in numbers]
            numbers = replace(numbers)
            numbers = "".join(numbers)
            firstNum = numbers[0]
            # lastNum = numbersBackwards[0]
            val = int(firstNum) * 10 + int(lastNum)
            sum += val
            print(f"{x}: {numbers}: {val}")


        print(sum)

if __name__ == "__main__":
    main()
