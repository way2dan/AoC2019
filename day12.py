from itertools import product
from numpy import sign
from math import gcd


def apply_gravity(moons, v):
    for i, j in product(range(4), range(4)):
        for c in range(3):
            v[i][c] += sign(moons[j][c] - moons[i][c])


def apply_velocity(moons, v):
    for i in range(4):
        for c in range(3):
            moons[i][c] += v[i][c]


def compare(m0, m, coordinate):
    f = True
    for i in range(4):
        f = f and (m[i][coordinate] == m0[i][coordinate])
    return f


def calculate_energy(moons, velocities):
    E = 0
    for i in range(4):
        ep = sum([abs(mc) for mc in moons[i]])
        ek = sum([abs(vc) for vc in velocities[i]])
        E += ep*ek
    return E


moons = [[4, 12, 13], [-9, 14, -3], [-7, -1, 2], [-11, 17, -1]]
m0 = [[4, 12, 13], [-9, 14, -3], [-7, -1, 2], [-11, 17, -1]]


v = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
v0 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

Steps = 1000
axis_with_no_period = [0, 1, 2]
periods = []
i = 0
while axis_with_no_period:
    i += 1
    apply_gravity(moons, v)
    apply_velocity(moons, v)
    if i == Steps:
        print(calculate_energy(moons, v))
    for c in axis_with_no_period:
        if compare(m0, moons, coordinate=c) and compare(v0, v, coordinate=c):
            periods.append(i)
            axis_with_no_period.remove(c)

p = periods[0] * periods[1] * periods[2]
d1 = gcd(periods[0], periods[1])
d2 = gcd(periods[1], periods[2])
d3 = gcd(periods[0], periods[2])
d4 = gcd(d1,d2)

print(p/d1/d2/d3*d4)
