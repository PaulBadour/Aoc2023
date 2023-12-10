'''
1464/1655
Part one went down relatively smoothly, happy to not have any pathfinding
Part two took a long time of bouncing ideas back and forth the figure out a solution
'''

from aoclib import *
DAY = 10
PART = 2

pInp = get_input(DAY)
ans = 0

grid = [list(i) for i in pInp]
print(grid, len(grid),len(grid[0]))
class Node:
    def __init__(self, sym,x,y):
        self.sym = sym
        self.nextTo = []
        self.x,self.y = x,y
        self.t = False
    def add(self, dirs):
        global grid
        if dirs[0] == 1:
            if self.x > 0:
                self.nextTo.append(grid[self.x-1][self.y])

        if dirs[1] == 1:
            if self.y < len(grid[0]) - 1:
                self.nextTo.append(grid[self.x][self.y+1])

        if dirs[2] == 1:
            if self.x < len(grid) - 1:
                self.nextTo.append(grid[self.x+1][self.y])

        if dirs[3] == 1:
            if self.y > 0:
                self.nextTo.append(grid[self.x][self.y-1])

    def print(self):
        print(f"{self}({self.x},{self.y}) symbol {self.sym} neighbor {self.nextTo}")
            

first = None
for i in range(len(grid)):
    for j in range(len(grid[i])):
        t = False
        if grid[i][j] == 'S':
            t = True
        grid[i][j] = Node(grid[i][j],i,j)
        if t:
            first = grid[i][j]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        match grid[i][j].sym:
            case "S":
                grid[i][j].add([1,0,1,0])
            case "|":
                grid[i][j].add([1,0,1,0])
            case "-":
                grid[i][j].add([0,1,0,1])
            case "L":
                grid[i][j].add([1,1,0,0])
            case "J":
                grid[i][j].add([1,0,0,1])
            case "7":
                grid[i][j].add([0,0,1,1])
            case "F":
                grid[i][j].add([0,1,1,0])
            case ".":
                pass


first.t = True
n1,n2 = first.nextTo[0],first.nextTo[1]
l1,l2 = first,first
t1,t2 = 0,0
ans = 0
#first.print()

while n1 != n2 and not n1.t:
    #n1.print()
    #n2.print()
    #input()
    #ans += 1
    t1 = n1
    n1 = n1.nextTo[0] if n1.nextTo[0] != l1 else n1.nextTo[1]
    l1 = t1
    l1.t = True

    t2 = n2
    n2 = n2.nextTo[0] if n2.nextTo[0] != l2 else n2.nextTo[1]
    l2 = t2
    l2.t = True
n1.t = True
n2.t = True

for i in range(len(grid)):
    last = None
    inside = False
    for j in range(len(grid[i])):
        if inside and not grid[i][j].t:
            #grid[i][j].print()
            ans += 1
        elif grid[i][j].t:
            if grid[i][j].sym in ('|','S'):
                inside = False if inside else True
            elif last == None and grid[i][j].sym in ('7','F','J','L'):
                last = grid[i][j].sym

            elif grid[i][j].sym in ('7','F','J','L'):
                if set([last,grid[i][j].sym]) in [set(['7','L']), set(['F','J'])]:
                    inside = False if inside else True
                last = None




submit(DAY, PART, ans)