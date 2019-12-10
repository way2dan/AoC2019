from math import gcd, atan2
from itertools import product


def get_directions(S):
    a = []
    for x, y in product(range(-S, S), range(-S, S)):
        if gcd(x, y) == 1:
            a.append((x, y))
    a.sort(key=lambda t: atan2(-t[1], t[0]))
    a.insert(0, a.pop(-1))
    return a


def lookup(belt, x, y, dx, dy):
    i = 0
    found = False
    while not found:
        i += 1
        if (0 <= x + i*dx < len(belt)) and (0 <= y + i*dy < len(belt[0])):
            found = belt[x + i*dx][y + i*dy] == '#'
        else:
            break
    return found


def shoot_lazer(belt, x, y, dx, dy):
    i = 0
    found = False
    while not found:
        i += 1
        if (0 <= x + i*dx < len(belt)) and (0 <= y + i*dy < len(belt[0])):
            found = belt[x + i*dx][y + i*dy] == '#'
        else:
            break
    if found:
        belt[x + i * dx][y + i * dy] = '*'
    return (x + i*dx, y + i*dy) if found else None


f = open('input10.txt', 'r')
belt = [list(s.strip('\n')) for s in f.readlines()]
Width, Height = len(belt[0]), len(belt)
visible = [[0 for i in range(Width)] for _ in range(Height)]
best_asteroid = [0, 0, 0]
directions = get_directions(max(Height, Width))

for x, y in product(range(Height), range(Width)):
    if belt[x][y] != '#':
        continue
    for dx, dy in directions:
        visible[x][y] += lookup(belt, x, y, dx, dy)
    if visible[x][y] > best_asteroid[2]:
        best_asteroid = [x, y, visible[x][y]]
print(best_asteroid)

i = 0
while i < 200:
    for dx, dy in directions:
        vaporized = shoot_lazer(belt, best_asteroid[0], best_asteroid[1], dx, dy)
        i += 1 if vaporized else 0
        if i == 200:
            break
print(vaporized)
