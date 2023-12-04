#!/usr/bin/env python3

import re

global POSSIBLE_RED, POSSIBLE_GREEN, POSSIBLE_BLUE

def main():
    possibleIDs = []
    sum = 0

    with open("dataTwo.txt", "r") as f:

        x = [y.strip() for y in f.readlines()]

        for game in x:
            rounds = game.split(";")

            gameNumber = re.match(r"Game \d+", rounds[0])[0]
            gameNumber = gameNumber.replace("Game ", "").strip()
            print(f"GameNumber is {gameNumber}")
            RED_SATISFIED = 0
            GREEN_SATISFIED = 0
            BLUE_SATISFIED = 0

            for round in rounds:
                ## Handling Red
                redCount = re.search(r"[0-9]+ red", round)
                if not (redCount is None):
                    redCount = int(redCount[0].replace("red", "").strip())
                    print(f"redCount is {redCount}")
                    if redCount > RED_SATISFIED:
                        print("IN RED")
                        RED_SATISFIED = redCount

                ## Handling Green
                greenCount = re.search(r"[0-9]+ green", round)
                if not (greenCount is None):
                    greenCount = int(greenCount[0].replace("green", "").strip())
                    print(f"greenCount is {greenCount}")
                    if greenCount > GREEN_SATISFIED:
                        print("IN GREEN")
                        GREEN_SATISFIED = greenCount

                ## Handling Blue
                blueCount = re.search(r"[0-9]+ blue", round)
                if not (blueCount is None):
                    blueCount = int(blueCount[0].replace("blue", "").strip())
                    print(f"blueCount is {blueCount}")
                    if blueCount > BLUE_SATISFIED:
                        print("IN BLUE")
                        BLUE_SATISFIED = blueCount

            print(RED_SATISFIED)
            print(GREEN_SATISFIED)
            print(BLUE_SATISFIED)
            sum += RED_SATISFIED * GREEN_SATISFIED * BLUE_SATISFIED


    print(sum)

if __name__ == "__main__":
    main()
