# DAY 05
from collections import Counter

def read_input():
    ret = []
    with open("./input.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line:
                print("* ", line)
                ret.append(parse_input_line(line))
    return ret

def parse_input_line(line_str):
    def _to_coords(s):
        x, y = [int(n) for n in s.split(",")]
        return x, y
    # print("*", line_str.split(" -> "))
    start, end = [_to_coords(l.strip()) for l in line_str.split(" -> ")]

    return start, end

def is_horizontal_or_vertical(line):
    start, end = line
    return start[0] == end[0] or start[1] == end[1]


def line_points(line):
    def _get_direction(start_c, end_c):
        if start_c == end_c:
            return 0
        elif start_c < end_c:
            return 1
        elif start_c > end_c:
            return -1

    (start_x, start_y), (end_x, end_y) = line
    direction_x, direction_y = _get_direction(start_x, end_x), _get_direction(start_y, end_y)
    ret = [(start_x, start_y)]
    while (start_x, start_y) != (end_x, end_y):
        start_x, start_y = start_x + direction_x, start_y + direction_y
        ret.append((start_x, start_y))
    return ret


hydrothermal_vent_lines = read_input()


def get_overlap_points(line_points):
    counter = Counter(p for lp in line_points for p in lp)
    return [coord for coord, occ in counter.items() if occ > 1]


horizontal_or_vertical_line_points = [line_points(line) for line in hydrothermal_vent_lines if is_horizontal_or_vertical(line)]
overlap_points = get_overlap_points(horizontal_or_vertical_line_points)

print("Solution - Part 1")
print(len(overlap_points))
print()

all_line_points = [line_points(line) for line in hydrothermal_vent_lines ]
all_overlap_points = get_overlap_points(all_line_points)


print("Solution - Part 2")
print(len(all_overlap_points))
print()
