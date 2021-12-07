# DAY-07
from statistics import median


def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        return [int(i) for i in f.read().split(",")]


def distance(positions, target):
    return [abs(p - target) for p in positions]



input_data = read_input()

print("Solution - Part 1")
print(
    sum(distance(input_data, int(median(input_data))))
)

print()
print("-" * 80)
print()

# Part 2

def distance2(positions, target):
    def _sum_of_first_n(n):
        return (n * (n + 1)) / 2
    return [_sum_of_first_n(abs(p - target)) for p in positions]


def find_best_distance(data):
    current_best_distance, current_best_pos = None, None
    for pos in range(min(data), max(data) + 1):
        distances = distance2(data, pos)
        sum_distance = int(sum(distances))
        if not current_best_distance or current_best_distance > sum_distance:
            current_best_distance, current_best_pos = sum_distance, pos
    return current_best_pos, current_best_distance


print("Solution - Part 2")
print(find_best_distance(input_data))