'''
5034/3561

Part one was definitely rough, lots of stupid bugs that costed me time along with me not finding a wonderful solution quickly
Part two was pretty good for me, quick turnaround
'''


from aoclib import *
DAY = 3
PART = 2





pInp = get_input(DAY)
cNums = []
foundCoords = set()
ans = 0

grid = [[None for j in range(len(pInp[0]))] for i in range(len(pInp))]
lastNum = None

def findNum(x,y,check=True):
    global grid,foundCoords,lastNum
    num = None

    if grid[x][y].isdigit():
        num = grid[x][y]
        #print('foudnNumne ', x, y)
        for i in range(1,4):
            if y+i < len(pInp[0]) and grid[x][y+i].isdigit():
                num = num + grid[x][y+i]
            else:
                break

        tempi = 0
        for i in range(1,4):
            tempi=i
            if y-i >= 0 and grid[x][y-i].isdigit():
                num = grid[x][y-i] + num
            else:
                break
        coord = (x, y-tempi+1)
        if coord not in foundCoords or not check:
            foundCoords.add(coord)
            lastNum = int(num)
            return int(num)
        else:
            return None
    
    return None


symbols = set(list('!#$%&-/?@=+*'))
symCoords = []
for x, i in enumerate(pInp):
    for y, j in enumerate(i):
        grid[x][y] = j
        if j in symbols:
            symCoords.append((x,y))



for i in symCoords:
    numList = []
    

    if i[1] > 0:
        if findNum(i[0],i[1]-1) != None:
            cNums.append(findNum(i[0],i[1]-1,False))
            numList.append(lastNum)

    if i[1] < len(pInp[0]) - 1:
        if findNum(i[0],i[1]+1) != None:
            cNums.append(findNum(i[0],i[1]+1,False))
            numList.append(lastNum)

    if i[0] > 0:
        if findNum(i[0]-1,i[1]) != None:
            cNums.append(findNum(i[0]-1,i[1],False))
            numList.append(lastNum)
        
        if i[1] > 0:
            if findNum(i[0]-1,i[1]-1) != None:
                cNums.append(findNum(i[0]-1,i[1]-1,False))
                numList.append(lastNum)

        if i[1] < len(pInp) - 1:
            if findNum(i[0]-1,i[1]+1) != None:
                cNums.append(findNum(i[0]-1,i[1]+1,False))
                numList.append(lastNum)

    if i[0] < len(pInp[0]) - 1:
        if findNum(i[0]+1,i[1]) != None:
            cNums.append(findNum(i[0]+1,i[1],False))
            numList.append(lastNum)
        
        if i[1] > 0:
            if findNum(i[0]+1,i[1]-1) != None:
                cNums.append(findNum(i[0]+1,i[1]-1,False))
                numList.append(lastNum)

        if i[1] < len(pInp) - 1:
            if findNum(i[0]+1,i[1]+1) != None:
                cNums.append(findNum(i[0]+1,i[1]+1,False))
                numList.append(lastNum)
    
    numList = list(set(numList))
    if len(numList) == 2 and grid[i[0]][i[1]] == "*":
        ans += numList[0] * numList[1]



submit(DAY, PART, ans)