from itertools import permutations
from intcomp import IntcodeController


f = open('input7.txt', 'r')
ls1 = f.read().split(',')

powers = []
for prm in permutations([0, 1, 2, 3, 4]):
    c = [IntcodeController([int(s) for s in ls1]) for _ in range(5)]
    signal = 0
    for i in range(5):
        c[i].buffer = [prm[i], signal]
        c[i].run()
        signal = c[i].output[-1]
    powers.append(signal)
print('First half answer is ', max(powers))

powers = []
for prm in permutations([5, 6, 7, 8, 9]):
    c = [IntcodeController([int(s) for s in ls1], buffer=[prm[i]]) for i in range(5)]
    signal = 0
    alive = True
    while alive:
        for i in range(5):
            c[i].buffer.append(signal)
            alive = alive and c[i].run2output()
            signal = c[i].output[-1]
    powers.append(signal)

print('Second haf answer is ', max(powers))
