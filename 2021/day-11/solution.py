# DAY 11
from typing import Dict, Tuple


def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        return parse_input(f.read())


def parse_input(input_str: str):
    ret = {}
    for i, line in enumerate(input_str.splitlines(keepends=False)):
        for j, char in enumerate(line):
            ret[(i,j)] = int(char)
    return ret


starting_energy_levels = read_input()


def get_adjacent(c : Tuple[int, int]):
    ret = []
    for i in [-1, 0, +1]:
        for j in [-1, 0, +1]:
            ret.append((c[0] + i, c[1] + j))
    return [(i, j) for i, j in ret if i >=0 and i <= 9 and j >= 0 and j <= 9 ]


def simulate_step(starting_levels: Dict[Tuple[int, int], int]):
    # Increase levels with 1
    levels = {k: v + 1 for k, v in starting_levels.items()}
    flashes_we_already_had = set()

    # do flashes
    while True:
        flashes = {k for k, v in levels.items() if v > 9}
        if flashes == flashes_we_already_had:
            break
        for f in flashes:
            if f not in flashes_we_already_had:
                flashes_we_already_had.add(f)
                for a in get_adjacent(f):
                    levels[a] += 1

    # print(flashes_we_already_had)

    levels = {k: v if v <=9 else 0 for k, v in levels.items()}
    return levels, flashes_we_already_had


# print(starting_energy_levels)
def simulate_steps(starting_levels: Dict[Tuple[int, int], int], steps=100):
    num_flashes = 0
    levels = starting_levels
    for step in range(steps):
        levels, flashes = simulate_step(levels)
        num_flashes += len(flashes)
        # print(step, num_flashes)
    return levels, num_flashes


def find_first_step_with_100_flashes(levels: Dict[Tuple[int, int], int]):
    step = 0
    while True:
        levels, flashes = simulate_step(levels)
        num_flashes = len(flashes)
        step += 1
        # print(step, num_flashes)
        if num_flashes == 100:
            break
    return step


print("Part 1")
print(simulate_steps(starting_energy_levels))

print()
print("Part 2")
print(find_first_step_with_100_flashes(starting_energy_levels))