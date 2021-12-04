# DAY 04
from pprint import pprint
from typing import Tuple

def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        numbers_drawn = [int(i) for i in f.readline().strip().split(",")]
        f.readline()
        bingo_cards = []
        current_card = []
        while True:
            line = f.readline()
            numbers = [int(number_str) for number_str in line.strip().split()]
            if numbers:
                if len(current_card) < 25:
                    current_card += numbers
                else:
                    bingo_cards.append(current_card)
                    current_card = numbers
            if not line:
                break

        return numbers_drawn, bingo_cards

def _row_and_column(index) -> Tuple[int, int]:
    row = index // 5
    column = index % 5
    return row, column


def is_bingo(bingo_card, drawn_numbers):
    row_matches = [0 for _ in range(0, 5)]
    column_matches = [0 for _ in range(0, 5)]
    numbers_circled = []
    for i, number in enumerate(drawn_numbers):
        # print("number", number, bingo_card)
        try:
            index = bingo_card.index(number)
        except ValueError:
            continue
        row, column = _row_and_column(index)
        row_matches[row] += 1
        column_matches[column] += 1
        numbers_circled.append(number)

        if 5 in row_matches or 5 in column_matches:
            # BINGO!!!!
            return i, [n for n in bingo_card if n not in numbers_circled]
        # pprint((bingo_card, index, number))


def find_first_winning_card(bingo_cards, drawn_numbers):
    win_card = None
    win_numbers_left = None
    win_on_number = None

    for bingo_card in bingo_cards:
        on_number, numbers_left = is_bingo(bingo_card, drawn_numbers)
        if win_on_number is None or win_on_number > on_number:
            win_card = bingo_card
            win_numbers_left = numbers_left
            win_on_number = on_number
    return win_card, win_numbers_left, win_on_number

def find_last_winning_card(bingo_cards, drawn_numbers):
    win_card = None
    win_numbers_left = None
    win_on_number = None

    for bingo_card in bingo_cards:
        on_number, numbers_left = is_bingo(bingo_card, drawn_numbers)
        if win_on_number is None or win_on_number < on_number:
            win_card = bingo_card
            win_numbers_left = numbers_left
            win_on_number = on_number
    return win_card, win_numbers_left, win_on_number

numbers_drawn, bingo_cards = read_input()

win_card, win_numbers_left, win_on_number = find_first_winning_card(bingo_cards, numbers_drawn)

print("PART 1")
print(sum(win_numbers_left) * numbers_drawn[win_on_number])
print()

print("PART 2")

loose_card, loose_numbers_left, loose_on_number = find_last_winning_card(bingo_cards, numbers_drawn)
print(sum(loose_numbers_left) * numbers_drawn[loose_on_number])
print()