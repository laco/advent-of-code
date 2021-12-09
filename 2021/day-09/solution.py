# DAY 08
import math


sample_data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        return parse_input(f.read())


def parse_input(s: str):
    rows = []
    for line in s.splitlines():
        columns = []
        for num in line.strip():
            columns.append(int(num))
        rows.append(columns)
    return rows


def is_low_point(i, j, heightmap):
    height = heightmap[i][j]
    neighbours = get_neighbours(i, j, heightmap)
    return all(height < n[2] for n in neighbours)


def get_neighbours(i, j, heightmap):
    max_i = len(heightmap) - 1
    max_j = len(heightmap[0]) -1

    ret = []
    neighbours = [(i -1, j), (i + 1, j), (i, j -1), (i, j + 1)]

    for ni, nj in neighbours:
        if ni < 0 or ni > max_i or nj < 0 or nj > max_j:
            continue
        ret.append((ni, nj, heightmap[ni][nj]))

    return ret



def find_all_low_points(heightmap):
    low_points = []
    for i, row in enumerate(heightmap):
        for j, height in enumerate(row):
            if is_low_point(i, j, heightmap):
                low_points.append((i, j, height))
    return low_points


def print_map(heightmap):
    for i, line in enumerate(heightmap):
        for j, n in enumerate(line):
            if is_low_point(i, j, heightmap):
                print(f'\N{ESC}[31m{n}\u001b[0m', end="")
                # print("*", end="")
            else:
                print(n, end="")
        print()


def sum_of_risk(low_points):
    return sum(p[2] for p in low_points) + len(low_points)


print("Part 1")
sample_heightmap = parse_input(sample_data)
# print_map(sample_heightmap)
sample_low_points = find_all_low_points(sample_heightmap)

print(f"Sum of risk (sample): {sum_of_risk(sample_low_points)}")

print()

heightmap = read_input()
# print_map(heightmap)
low_points = find_all_low_points(heightmap)
print(f"Sum of risk: {sum_of_risk(low_points)}")
print()

# ------------------------------------------------------------------------------------
print("*" * 100)
print("Part 2 ")

def calc_basin(i, j, heightmap, acc = None):
    if not acc:
        acc = []
    acc.append((i, j))

    for ni, nj, nh in get_neighbours(i, j, heightmap):
        if (ni, nj) not in acc and nh < 9:
            acc = calc_basin(ni, nj, heightmap, acc)

    return acc

def calc_all_basin(low_points, heightmap):
    ret = {}
    for i, j, _ in low_points:
        ret[(i, j)] = calc_basin(i, j, heightmap)
    return ret

def calc_basing_sizes(basins):
    return sorted([len(points) for center, points in basins.items()], reverse=True)

basins = calc_all_basin(low_points, heightmap)
basin_sizes = calc_basing_sizes(basins)
print("Top 3 basins", basin_sizes[:3], math.prod(basin_sizes[:3]))