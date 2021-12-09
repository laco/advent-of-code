# DAY 08

def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        ret = []
        for line in f.readlines():
            patterns, output = [parts.split() for parts in line.split("|")]
            ret.append((patterns, output))
    return ret


patterns_and_outputs = read_input()
outputs = [o for _, o in patterns_and_outputs]


def is_1478(pattern):
    return len(pattern) in [2, 4, 3, 7]


def count_1478(outputs):
    return len([p for o in outputs for p in o if is_1478(p)])


print("Part 1")
print(count_1478(outputs))

# --------------------------------------------------------------------------------


def find_first(iterable, condition):
    return next((i for i in iterable if condition(i)), None)

def sort_letters(s):
    return "".join(sorted(s))

def decode_numbers(patterns):
    # seven segments used in 8
    # six segments used in 0, 6, 9
    # five segments used in 2, 3, 5
    # four segments used in 4
    # three segments used in 7
    # two segments used in 1

    numbers = {
        1: find_first(patterns, lambda p: len(p) == 2),
        4: find_first(patterns, lambda p: len(p) == 4),
        7: find_first(patterns, lambda p: len(p) == 3),
        8: find_first(patterns, lambda p: len(p) == 7),
    }

    segment_a = [l for l in numbers[7] if l not in numbers[1]][0]

    # IDEA1: C appears in only 8 cases, F is in 9 of 10
    for l in numbers[1]:
        oc = len([p for p in patterns if l in p])
        if oc == 8:
            segment_c = l
        elif oc == 9:
            segment_f = l

    # print(f"a -> {segment_a}, c -> {segment_c}, f -> {segment_f}")
    numbers[6] = find_first(patterns, lambda p: len(p) == 6 and (segment_c not in p))


    # IDEA2: four is always a part of 9
    possible_nines = [p for p in patterns if len(p) == 6 and all(l in p for l in numbers[4])]
    assert len(possible_nines) == 1
    numbers[9] = possible_nines[0]

    # Zero is the only with 6 segments left
    numbers[0] = find_first(patterns, lambda p: len(p) == 6 and p not in [numbers[9], numbers[6]])

    # FIVE is part of six
    numbers[5] = find_first(patterns, lambda p: len(p) == 5 and all(l in numbers[6] for l in p ))

    # TWO don't have F
    numbers[2] = find_first(patterns, lambda p: len(p) == 5 and p != numbers[5] and segment_f not in p)
    numbers[3] = find_first(patterns, lambda p: len(p) == 5 and p != numbers[5] and segment_f in p)

    assert(len(set(numbers.values())) == 10)
    assert(set(numbers.values()) == set(patterns))
    return numbers, {sort_letters(v): k for k, v in numbers.items()}

total = 0
for p, o in patterns_and_outputs:
    _, numbers_lookup = decode_numbers(p)
    total = total + int("".join(str(numbers_lookup[sort_letters(n)]) for n in o))

print("Part 2")
print(total)
