from intcomp import IntcodeController
RC_BLACK = 0
RC_WHITE = 1
TURN_RIGHT = {(0,1): (-1,0), (0,-1): (1,0), (1,0): (0,1), (-1,0): (0,-1)}
TURN_LEFT = {(0,1): (1,0), (0,-1): (-1,0), (1,0): (0,-1), (-1,0): (0,1)}


class Robot:

    def __init__(self, intcode: IntcodeController, panel={}):
        self.panel = panel
        self.pos = (0, 0)
        self.code = intcode
        self.direction = (0, -1)  # dx, dy

    def color(self):
        return self.panel[self.pos] if self.pos in self.panel else RC_BLACK

    def paint(self, c=RC_WHITE):
        self.panel[self.pos] = c

    def do_one_step(self):
        self.pos = (self.pos[0]+self.direction[0], self.pos[1]+self.direction[1])

    def run(self):
        while self.code.alive:
            self.code.buffer.append(self.color())
            self.code.run2output()
            if self.code.run2output():
                self.paint(self.code.output[-2])
            turn = self.code.output[-1]
            if turn == 0:
                self.direction = TURN_LEFT[self.direction]
            else:
                self.direction = TURN_RIGHT[self.direction]
            self.do_one_step()

    def print_as_picture(self):
        X = [c[0] for c in self.panel]
        minX, maxX = min(X), max(X)
        Y = [c[1] for c in self.panel]
        minY, maxY = min(Y), max(Y)
        for y in range(minY, maxY+1):
            s = ''
            for x in range(minX, maxX):
                if (x, y) in self.panel:
                    s += ' ' if self.panel[(x,y)] == RC_BLACK else '\u2588'
                else:
                    s += '#'
            print(s)

