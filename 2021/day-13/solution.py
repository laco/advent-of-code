# DAY 13

from typing import Tuple, List

SAMPLE="""
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        return parse_input(f.read())


def parse_input(input_str: str):
    dots = []
    folds = []
    for line in input_str.splitlines(keepends=False):
        if line and line.startswith("fold along"):
            orientation, line_num = line.split(" ")[-1].split("=")
            folds.append((orientation, int(line_num)))
        elif line:
            x, y = line.split(",")
            dots.append((int(x), int(y)))
    return dots, folds


def do_fold(dots: List[Tuple[int, int]], fold: Tuple[str, int]) -> List[Tuple[int, int]]:
    def _fold_dot(x, y, orientation, l):
        if orientation == "x" and x < l:
            return (x, y)
        elif orientation == "x" and x > l:
            return (l - (x - l), y)
        elif orientation == "y" and y < l:
            return (x, y)
        elif orientation == "y" and y > l:
            return (x, l - (y - l) )
    orientation, l = fold
    return sorted(list(set([_fold_dot(x, y, orientation, l) for x, y in dots])))

# sample_dots, sample_folds = parse_input(SAMPLE)
# print(do_fold(sample_dots, sample_folds[0]))

dots, folds = read_input()


print("Part 1")
print(len(do_fold(dots, folds[0])))


print("Part 2")


def do_multiple_folds(dots: List[Tuple[int, int]], folds: List[Tuple[str, int]]) -> List[Tuple[int, int]]:
    for fold in folds:
        dots = do_fold(dots, fold)
    return dots

dots_after_all_folds = do_multiple_folds(dots, folds)

def draw(dots: List[Tuple[int, int]]):
    max_x = max(x for x, _ in dots)
    max_y = max(y for _, y in dots)

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x, y) in dots:
                print("*", end="")
            else:
                print(" ", end="")
        print()

draw(dots_after_all_folds)
