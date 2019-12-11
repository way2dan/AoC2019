from robots import Robot, RC_BLACK, RC_WHITE
from intcomp import IntcodeController


f = open('input11.txt', 'r')
ls1 = f.read().split(',')
vm = IntcodeController([int(s) for s in ls1], buffer=[])
r = Robot(vm)
r.run()
print(len(r.panel))
vm.reset()
r = Robot(vm, panel={(0,0): RC_WHITE})
r.run()
r.print_as_picture()