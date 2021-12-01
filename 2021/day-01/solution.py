# DAY 01


def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        content = f.read()
        return [int(line) for line in content.splitlines()]


def count_measurements_increase_pairs(measurements):
    increase_count = 0
    for i, j in zip(measurements[0:-1], measurements[1:]):
        if i < j:
            increase_count += 1
    return increase_count


def count_measurements_increase_trio(measurements):
    trio_sums = [i + j + k for i, j, k in zip(measurements[0:-2], measurements[1:-1], measurements[2:])]
    return count_measurements_increase_pairs(trio_sums)


measurements = read_input()

# Part 1
print(count_measurements_increase_pairs(measurements))

# Part 2
print(count_measurements_increase_trio(measurements))