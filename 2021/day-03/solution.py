# DAY 03

def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        content = f.read()
        return [str(line) for line in content.splitlines()]

def calculate_gamma_and_epsilon_rate(binaries):
    gamma = ""
    epsilon = ""

    for i in range(12):
        count_one = 0
        count_zero = 0

        for b in binaries:
            if b[i] == "1":
                count_one += 1
            elif b[i] == "0":
                count_zero += 1

        if count_one > count_zero:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return gamma, epsilon


def _count(position, binaries):
        zero = 0
        one = 0
        for b in binaries:
            if b[position] == "0":
                zero += 1
            else:
                one += 1
        return zero, one


def _most_common(position, binaries):
    zero, one = _count(position, binaries)
    if zero > one:
        return "0"
    elif zero <= one:
        return "1"


def _least_common(position, binaries):
    zero, one = _count(position, binaries)
    if zero > one:
        return "1"
    elif zero <= one:
        return "0"

def _calculate_rating(binaries, filter):
    kept = binaries
    for i in range(12):
        keep_value = filter(i, kept)
        # print(f"We need to keep numbers where {i} is {keep_value}.")
        # print(f"Before: {len(kept)}")

        kept = [ b for b in kept if b[i] == keep_value]

        # print(f"After: {len(kept)}")
        # if len(kept) < 10:
        #     print("kept", kept)
        # print("-------")

        if len(kept) == 1:
            return kept[0]


def calculate_oxygen_generator_rating(binaries):
    return _calculate_rating(binaries, filter=_most_common)


def calculate_co2_scrubber_rating(binaries):
    return _calculate_rating(binaries, filter=_least_common)


gamma_str, epsilon_str = calculate_gamma_and_epsilon_rate(read_input())

print("--- Solution - Part 1 ---")
print(f"Gamma rate is {gamma_str} = {int(gamma_str, 2)}")
print(f"Epsilon rate is {epsilon_str} = {int(epsilon_str, 2)}")

power_consumption = int(gamma_str, 2) * int(epsilon_str, 2)
print()
print(f"The power consumption of the submarine is {power_consumption}")


print("--- Solution - Part 2 ---")
oxigen_generator_rating = calculate_oxygen_generator_rating(read_input())
co2_scrubber_rating = calculate_co2_scrubber_rating(read_input())
life_support_rating = int(oxigen_generator_rating, 2) * int(co2_scrubber_rating, 2)

print()
print(f"The life support rating is {oxigen_generator_rating} ({int(oxigen_generator_rating, 2)}) x {co2_scrubber_rating} ({int(co2_scrubber_rating, 2)})= {life_support_rating} ")