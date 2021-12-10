# DAY 10
from collections import deque


def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


lines = read_input()

OPEN_CLOSE_PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
OPENING_PARENS = "".join(list(OPEN_CLOSE_PAIRS.keys()))
CLOSING_PARENS = "".join(list(OPEN_CLOSE_PAIRS.values()))


def is_matching_parens(op, cl):
    return op + cl in ["()", "{}", "<>", "[]"]


def syntax_checker(line):
    stack = deque()
    for pos, char in enumerate(line):
        if char in OPENING_PARENS:
            stack.append(char)
        elif char in CLOSING_PARENS:
            previous_open = stack.pop()
            if not is_matching_parens(previous_open, char):
                return False, char, pos, None
    return True, None, None, add_closing_chars(stack)


def add_closing_chars(stack):
    ret = ""
    for char in reversed(stack):
        ret += OPEN_CLOSE_PAIRS[char]
    return ret


def score_for_illegal_character(char):
    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    return scores[char]


def score_closing_chars(closing_chars):
    ret = 0
    values = {
        "]": 2,
        ")": 1,
        "}": 3,
        ">": 4,
    }
    for char in closing_chars:
        ret = ret * 5
        ret = ret + values[char]
    return ret


def collect_bad_lines(lines):
    illegal_characters = []
    for line in lines:
        is_valid, illegal_character, _, _ = syntax_checker(line)
        if not is_valid:
            illegal_characters.append(illegal_character)
    return sum([score_for_illegal_character(ic) for ic in illegal_characters])


def collect_scores_for_good_line_closings(lines):
    scores = []
    for line in lines:
        is_valid, _, _, closing_chars = syntax_checker(line)
        if is_valid:
            score = score_closing_chars(closing_chars)
            scores.append(score)
    return sorted(scores)


print("Part 1")
print(collect_bad_lines(lines))

print("Part 2")
sorted_scores = collect_scores_for_good_line_closings(lines)

print(sorted_scores)
print(sorted_scores[int(len(sorted_scores) / 2)])