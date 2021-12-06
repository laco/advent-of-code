# DAY 06
from collections import Counter

def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        return [int(i) for i in f.read().split(",")]

def simulate_lanternfish_reproduction_single_day(starting):
    ret = []
    new_fishes = []
    for fish in starting:
        if fish == 0:
            ret.append(6)
            new_fishes.append(8)
        else:
            ret.append(fish - 1)
    return ret + new_fishes


def simulate_lanterfish_reproduction(starting, days):
    ret = starting
    for _ in range(days):
        ret = simulate_lanternfish_reproduction_single_day(ret)
    return ret


print("Solution - Part 1 ")
print(len(simulate_lanterfish_reproduction(read_input(), 80)))

# ---------------------------------------------------------------------------------------------------------


print("Solution - Part 2 ")


def better_simulate_lanternfish_repr_one_day(fish_counter):
    new_counter_dict = {
        8: fish_counter[0]
    }
    for timer, count in fish_counter.items():
        if timer == 0:
            new_counter_dict[6] = new_counter_dict.get(6, 0) + count
        else:
            new_counter_dict[timer-1] = new_counter_dict.get(timer-1, 0) + count
    return Counter(new_counter_dict)


def better_simulate_lantern_repr(fish_counter, days):
    ret = fish_counter
    for _ in range(days):
        ret = better_simulate_lanternfish_repr_one_day(ret)
    return ret


counted_repr = Counter(read_input())
print(better_simulate_lantern_repr(counted_repr, 256).total())
