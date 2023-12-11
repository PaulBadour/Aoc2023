'''
896/1656

Im amazed i got top 1k on part one, I completely read over the expanding universe part
Part two went pretty smoothly minus my inability to type under pressure
'''

from aoclib import *
DAY = 11
PART = 2

pInp = get_input(DAY)
ans = 0
grid = [list(i) for i in pInp]
c = []

infRows = []
infCols = []

i = 0
while i < len(grid[0]):
    if [j[i] for j in grid].count('#') == 0:
        infCols.append(i)
    i += 1

i = 0
while i < len(grid):
    if grid[i].count('#') == 0:
        infRows.append(i)
    i += 1


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            c.append((i,j))

for i in range(len(c)):
    for j in range(i + 1, len(c)):

        xr = sorted((c[i][0], c[j][0]))
        yr = sorted((c[i][1], c[j][1]))

        for k in range(xr[0], xr[1]):
            if k in infRows:

                ans += (1000000 - 1)

        for k in range(yr[0], yr[1]):
            if k in infCols:

                ans += (1000000 - 1)

        ans += abs(xr[0] - xr[1]) + abs(yr[0] - yr[1])

submit(DAY, PART, ans)
