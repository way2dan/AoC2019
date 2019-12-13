lens = {1: 4, 2: 4, 3: 2, 4: 2, 99: 1, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2}


class IntcodeController:

    def __init__(self, intcode, buffer=[], pointer=0, extended={}, get_input=None):
        self.intcode = intcode
        self.virgincode = [] + intcode
        self.buffer = buffer
        self.virginbuffer = [] + buffer
        self.ib = 0
        self.pointer = pointer
        self.output = []
        self.alive = True
        self.opcode = []
        self.lastopcode = 0
        self.relbase = 0
        self.extended = extended
        print(self.extended)
        self.tracking = False
        self.get_input = get_input

    def reset(self):
        self.__init__(self.virgincode, self.virginbuffer, pointer=0)

    def print(self):
        print('pointer=', self.pointer, 'opcode=', self.intcode[self.pointer],
              'relbase=', self.relbase, self.extended)

    def parsecurrentopcode(self):
        n = self.intcode[self.pointer]
        self.opcode = [n % 100, (n // 100) % 10, (n // 1000) % 10,
                       (n // 10000) % 10]

    def read(self, n):
        if n < len(self.intcode):
            return self.intcode[n]
        else:
            return self.extended[n] if n in self.extended else 0

    def write(self, v):
        offset = lens[self.opcode[0]] - 1
        n = self.parameter(offset, mode=1) + (self.relbase if self.opcode[offset] == 2 else 0)
        if n < len(self.intcode):
            self.intcode[n] = v
        else:
            self.extended[n] = v

    def parameter(self, offset, mode=-1):
        mode = self.opcode[offset] if mode == -1 else mode
        if mode == 0:
            return self.read(self.intcode[self.pointer+offset])
        if mode == 1:
            return self.intcode[self.pointer+offset]
        if mode == 2:
            return self.read(self.intcode[self.pointer+offset]+self.relbase)

    def read_input(self):
        if not self.get_input:
            self.ib += 1
            return self.buffer[self.ib-1]
        else:
            return self.get_input()

    def onetick(self):
        self.parsecurrentopcode()
        next_pointer = self.pointer + lens[self.opcode[0]]
        self.lastopcode = self.opcode[0]
        if self.tracking:
            self.print()
        if self.opcode[0] == 1:
            self.write(self.parameter(1) + self.parameter(2))
        if self.opcode[0] == 2:
            self.write(self.parameter(1) * self.parameter(2))
        if self.opcode[0] == 3:
            self.write(self.read_input())
        if self.opcode[0] == 4:
            self.output.append(self.parameter(1))
        if self.opcode[0] == 5:
            if self.parameter(1) != 0:
                next_pointer = self.parameter(2)
        if self.opcode[0] == 6:
            if self.parameter(1) == 0:
                next_pointer = self.parameter(2)
        if self.opcode[0] == 7:
            self.write(1 if self.parameter(1) < self.parameter(2) else 0)
        if self.opcode[0] == 8:
            self.write(1 if self.parameter(1) == self.parameter(2) else 0)
        if self.opcode[0] == 9:
            self.relbase += self.parameter(1)
        if self.opcode[0] == 99:
            self.alive = False
        return next_pointer

    def run(self):
        while self.alive:
            self.pointer = self.onetick()

    def run2output(self):
        self.lastopcode = 0
        while (self.lastopcode != 4) and self.alive:
            self.pointer = self.onetick()
        return self.alive

    def next_triple(self):
        self.run2output()
        self.run2output()
        self.run2output()
        if self.alive:
            return self.output[-3:]
        else:
            return None
