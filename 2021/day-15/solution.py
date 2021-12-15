# DAY 15
from typing import Dict, List, Tuple
from heapq import heappop, heappush
from itertools import product


Pair = Tuple[int, int]
RiskMap = Dict[Pair, int]


def read_input() -> RiskMap:
    with open("./input.txt", "r", encoding="utf-8") as f:
        return parse_input(f.read())


def parse_input(input_str: str) -> RiskMap:
    ret = {}
    for i, line in enumerate(input_str.splitlines(keepends=False)):
        for j, c in enumerate(line):
            ret[(i, j)] = int(c)
    return ret

SAMPLE = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

sample_risk_map = parse_input(SAMPLE)



def get_neighbours(v: Pair) -> List[Pair]:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return [(v[0] + dy, v[1] + dx) for dx, dy in directions]


def dijkstra(risk_map: RiskMap, start: Pair, end: Pair) -> Dict[Pair, int]:
    dist: Dict[Pair, int] = {start: 0}
    q: List[Tuple[int, Pair]] = []

    for v in risk_map.keys():
        if v != start:
            dist[v] = int(1e9)
        heappush(q, (dist[v], v))

    while q:
        _, u = heappop(q)
        if u == end:
            return dist
        for v in get_neighbours(u):
            if v not in risk_map:
                continue
            a = dist[u] + risk_map[v]
            if a < dist[v]:
                dist[v] = a
                heappush(q, (a, v))
    return dist


def get_max(risk_map: RiskMap) -> Pair:
    dest_i = max(i for i, _ in risk_map.keys())
    dest_j = max(j for _, j in risk_map.keys())
    return dest_i, dest_j


def find_shortest_path(risk_map: RiskMap) -> int:
    start, end = (0, 0), get_max(risk_map)
    dist = dijkstra(risk_map, start, end)
    return dist[end]

assert find_shortest_path(sample_risk_map) == 40


risk_map = read_input()
print("Part 1")
print(find_shortest_path(risk_map))


def enlarge_map(risk_map: RiskMap) -> RiskMap:
    risk_map = risk_map.copy()
    mi, mj = get_max(risk_map)
    mi, mj = mi + 1, mj+ 1
    for ix, jx, i, j in product(range(5), range(5), range(mi), range(mj)):
        risk_map[ix * mi + i, jx * mj + j] = (ix + jx + risk_map[i, j] - 1) % 9 + 1

    return risk_map

assert find_shortest_path(enlarge_map(sample_risk_map)) == 315

print("Part2")
print(find_shortest_path(enlarge_map(risk_map)))