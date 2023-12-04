#!/usr/bin/env python3

import re

global POSSIBLE_RED, POSSIBLE_GREEN, POSSIBLE_BLUE
POSSIBLE_RED = 12
POSSIBLE_GREEN = 13
POSSIBLE_BLUE = 14

def main():
    possibleIDs = []

    with open("dataTwo.txt", "r") as f:

        x = [y.strip() for y in f.readlines()]

        for game in x:
            rounds = game.split(";")

            gameNumber = re.match(r"Game \d+", rounds[0])[0]
            gameNumber = gameNumber.replace("Game ", "").strip()

            RED_SATISFIED = False
            GREEN_SATISFIED = False
            BLUE_SATISFIED = False

            for round in rounds:
                ## Handling Red
                redCount = re.search(r"[0-9]+ red", round)
                if not (redCount is None) and not RED_SATISFIED:
                    redCount = int(redCount[0].replace("red", "").strip())
                    if redCount > POSSIBLE_RED:
                        RED_SATISFIED = True

                ## Handling Greenf
                greenCount = re.search(r"[0-9]+ green", round)
                if not (greenCount is None) and not GREEN_SATISFIED:
                    greenCount = int(greenCount[0].replace("green", "").strip())
                    if greenCount > POSSIBLE_GREEN:
                        GREEN_SATISFIED = True

                ## Handling Blue
                blueCount = re.search(r"[0-9]+ blue", round)
                if not (blueCount is None) and not BLUE_SATISFIED:
                    blueCount = int(blueCount[0].replace("blue", "").strip())
                    if blueCount > POSSIBLE_BLUE:
                        BLUE_SATISFIED = True

            if not (RED_SATISFIED or GREEN_SATISFIED or BLUE_SATISFIED):
                possibleIDs.append(int(gameNumber))

    print(possibleIDs)
    sumVal = sum(possibleIDs)
    print(sumVal)

if __name__ == "__main__":
    main()
