# DAY 14
from collections import Counter


def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        return parse_input(f.read())


def parse_input(input_str: str):
    polymer_template = ""
    rules = {}
    for lno, line in enumerate(input_str.splitlines(keepends=False)):
        if not line:
            continue
        elif lno == 0:
            polymer_template = line
        else:
            pair, to_insert = line.split(" -> ")
            rules[pair] = to_insert
    return polymer_template, rules


SAMPLE = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

def do_step(template, rules):
    ret = template[0]
    for i in range(1, len(template)):
        p_prev, p = template[i-1], template[i]
        ret += rules.get(f"{p_prev}{p}", "") + p
    return ret

def do_n_steps(template, rules, steps):
    ret = template
    for _ in range(steps):
        ret = do_step(ret, rules)
    return ret

def get_most_and_least_common(polymer):
    p_counts = sorted(Counter(polymer).items(), key=lambda pair: pair[1], reverse=True)
    return p_counts[0][1], p_counts[-1][1]

sample_template, sample_rules = parse_input(SAMPLE)
assert do_step(sample_template, sample_rules) == "NCNBCHB"
assert do_n_steps(sample_template, sample_rules, 4) == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"

sample_after_10 = do_n_steps(sample_template, sample_rules, 10)
assert get_most_and_least_common(sample_after_10) == (1749, 161)

print("Part 1")
template, rules = read_input()
after_10_steps = do_n_steps(template, rules, 10)
mc, lc = get_most_and_least_common(after_10_steps)
print(f"{mc} - {lc} = {mc-lc}")
print()


print("Part 2")

def do_n_steps2(template, rules, steps):
    polymer_counter = Counter(template)
    t_rules = {(k[0], k[1]): v for k, v in rules.items()}
    rule_counter = Counter([(template[i], template[i+1]) for i in range(0, len(template) -1 ) if (template[i], template[i+1]) in t_rules])

    # print(0, polymer_counter, rule_counter)
    for s in range(1, steps + 1):
        next_rule_counter = rule_counter.copy()
        for pair, pn in t_rules.items():
            p1, p2 = pair
            occurences = rule_counter[(p1, p2)]
            next_rule_counter[(p1, p2)] -= occurences
            if (p1, pn) in t_rules:
                next_rule_counter[(p1, pn)] += occurences
            if (pn, p2) in t_rules:
                next_rule_counter[(pn, p2)] += occurences
            polymer_counter[pn] += occurences
        # print(s, polymer_counter, rule_counter, next_rule_counter)
        rule_counter = next_rule_counter

    p_counts = sorted(polymer_counter.items(), key=lambda pair: pair[1], reverse=True)
    return p_counts[0][1], p_counts[-1][1]


assert do_n_steps2(sample_template, sample_rules, 10) == (1749, 161)


mc40, lc40 = do_n_steps2(template, rules, 40)
print(f"{mc40} - {lc40} = {mc40-lc40}")