# DAY 12
from collections import Counter


def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        return parse_input(f.read())


def parse_input(input_str: str):
    ret = []
    for line in input_str.splitlines(keepends=False):
        c1, c2 = line.split("-")
        ret.append((c1, c2))
    return ret


def get_connections_for(cave_name, all_connections):
    cons = []
    for c1, c2 in all_connections:
        if c1 == cave_name:
            cons.append(c2)
        elif c2 == cave_name:
            cons.append(c1)
    return cons


def generate_paths(cave_connections: list, start="start", end="end", caves_we_already_visited=[]):
    if start == end:
        yield caves_we_already_visited + [end]

    for c in get_connections_for(start, cave_connections):
        if c == c.lower() and c in caves_we_already_visited:
            continue
        yield from generate_paths(cave_connections, start=c, end=end, caves_we_already_visited=caves_we_already_visited + [start])



# --- Testing with the examples ---

SAMPLE1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""
sample1_connections = parse_input(SAMPLE1)
sample1_paths = [path for path in generate_paths(sample1_connections)]
assert len(sample1_paths) == 10

SAMPLE2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""
sample2_connections = parse_input(SAMPLE2)
sample2_paths = [path for path in generate_paths(sample2_connections)]
assert len(sample2_paths) == 19

SAMPLE3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""
sample3_connections = parse_input(SAMPLE3)
sample3_paths = [path for path in generate_paths(sample3_connections)]
assert len(sample3_paths) == 226

# --- Part 1 Solution ---

cave_connections = read_input()
cave_paths = [path for path in generate_paths(cave_connections)]
print("Part 1")
print(len(cave_paths))



# --- Part 2 ---

def _can_we_go(cave, caves_we_already_visited):
    if cave == "start":
        return False
    elif "end" == caves_we_already_visited[-1]:
        return False
    elif (cave not in caves_we_already_visited) or (cave != cave.lower()):
        return True
    else: # lower chars
        _, most_common_count = Counter([c for c in caves_we_already_visited if c == c.lower()]).most_common()[0]
        if most_common_count <= 1:
            return True
        else:
            return False


def generate_paths2(cave_connections: list, caves_we_already_visited = None):
    caves_we_already_visited = caves_we_already_visited or ["start"]
    current_cave = caves_we_already_visited[-1]

    if current_cave == "end":
        yield caves_we_already_visited

    for c in get_connections_for(current_cave, cave_connections):
        if not _can_we_go(c, caves_we_already_visited):
            continue
        yield from generate_paths2(cave_connections, caves_we_already_visited=caves_we_already_visited + [c])

print("Part 2")

cave_paths2 = [path for path in generate_paths2(cave_connections)]
print(len(cave_paths2))

