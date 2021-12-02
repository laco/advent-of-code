# DAY 02


def read_input():
    ret = []
    with open("./input.txt", "r", encoding="utf-8") as f:
        content = f.read()
        for line in content.splitlines():
            direction, unit = line.split()
            ret.append((direction, int(unit)))
    return ret

def calculate_horizontal_position_and_depth(moves):
    horizontal_pos, depth = 0, 0
    for direction, unit in moves:
        if direction == "forward":
            horizontal_pos += unit
        elif direction == "up":
            depth -= unit
        elif direction == "down":
            depth += unit
    return horizontal_pos, depth

def calculate_horizontal_position_and_depth_part2(moves):
    horizontal_pos, depth, aim = 0, 0, 0
    for direction, unit in moves:
        if direction == "forward":
            horizontal_pos += unit
            depth += aim * unit
        elif direction == "up":
            # up X decreases your aim by X units.
            aim -= unit
        elif direction == "down":
            # down X increases your aim by X units.
            aim += unit
    return horizontal_pos, depth

horizontal_pos, depth = calculate_horizontal_position_and_depth(read_input())

print(f"Solution part 1: {horizontal_pos} * {depth} = {horizontal_pos * depth}")

horizontal_pos2, depth2 = calculate_horizontal_position_and_depth_part2(read_input())

print(f"Solution part 1: {horizontal_pos2} * {depth2} = {horizontal_pos2 * depth2}")