from intcomp import IntcodeController
from itertools import product
UNKNOWN = -1
WALL = 0
EMPTY = 1
OXYGEN = 2
NOTVISITED = -1
dr = [0, -1, 1, 0, 0]  # 0, North, South, West, East
dc = [0, 0, 0, -1, 1]


def fillroutes(maze, vm: IntcodeController, celltype, r, c, route):
    if (maze[r][c][0] != UNKNOWN) and (maze[r][c][0] != celltype):
        print('Something is wrong')
    maze[r][c][0] = celltype
    if celltype == WALL:
        return False
    try:
        if (len(maze[r][c][2]) > len(route)) or maze[r][c][1] == NOTVISITED:
            maze[r][c][1] = len(route)
            maze[r][c][2] = route
            route = route + [(r, c)]
            for d in range(1, 5):
                dump = vm.dump()
                vm.buffer.append(d)
                vm.run2output()
                celltype = vm.output[-1]
                fillroutes(maze, vm, celltype, r+dr[d], c+dc[d], route)
                vm.restore_from_dump(dump)
    except IndexError:
        print('not enough maze size')
        return
    return


def fillroutes2(maze, r, c, route):
    if maze[r][c][0] != WALL and \
            ((len(maze[r][c][2]) > len(route)) or maze[r][c][1] == NOTVISITED):
        maze[r][c][1] = len(route)
        maze[r][c][2] = route
        route = route + [(r, c)]
        for d in range(1, 5):
            fillroutes2(maze, r+dr[d], c+dc[d], route)


def print_maze(maze, theroute):
    longest_route = 0
    chars = {UNKNOWN: '\u2591', WALL: '\u2588', EMPTY: ' ', OXYGEN: 'O'}
    for r in range(Width):
        s = ''
        for c in range(Width):
            the_char = chars[maze[r][c][0]]
            if (r, c) in theroute:
                the_char = '\u00b7'
            if maze[r][c][0] == EMPTY:
                if maze[r][c][1] > longest_route:
                    longest_route = maze[r][c][1]

            s += the_char

        print(s)
    return longest_route


f = open('input15.txt', 'r')
ls1 = f.read().split(',')
vm = IntcodeController([int(s) for s in ls1])

Width = 50

maze = [[[UNKNOWN, NOTVISITED, []] for _ in range(Width)] for i in range(Width)]
fillroutes(maze, vm, EMPTY, Width // 2, Width // 2, [])
chars = {UNKNOWN: '?', WALL: '\u2588', EMPTY: ' ', OXYGEN: 'O'}
for r,c in product(range(Width), range(Width)):
    if maze[r][c][0] == OXYGEN:
        oxy_r = r
        oxy_c = c
        theroute = maze[r][c][2]


print_maze(maze, theroute)
print(len(theroute))

new_maze = [[[maze[i][j][0], NOTVISITED, []] for j in range(Width)] for i in range(Width)]

fillroutes2(new_maze, oxy_r, oxy_c, [])
print(print_maze(new_maze, []))
