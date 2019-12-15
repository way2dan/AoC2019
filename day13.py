from intcomp import IntcodeController
from numpy import sign

f = open('input13.txt', 'r')
ls1 = f.read().split(',')
code = [int(s) for s in ls1]
code[0] = 2
foo = lambda: sign(ball_x-paddle_x)
vm = IntcodeController(code, get_input=foo)

ball_x = 0
paddle_x = 0
score = 0
while vm.alive:
    a = vm.next_triple()
    if a:
        if a[:2] == [-1, 0]:
            print('score is ', a[2])
        if a[2] == 3:
            paddle_x = a[0]
        if a[2] == 4:
            ball_x = a[0]
