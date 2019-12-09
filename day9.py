from intcomp import IntcodeController

f = open('input9.txt', 'r')
ls1 = f.read().split(',')
vm = IntcodeController([int(s) for s in ls1], buffer=[1])
vm.run()
print(vm.output)
vm.reset()
vm.buffer = [2]
vm.run()
print(vm.output)
