'''
217/315

Very happy with first part time despite not leaderboarding
Second part was pretty solid I just had a logic error that held me back a few places
'''

from aoclib import *
DAY = 2
PART = 2

pInp = get_input(DAY)
ans = 0



for i in pInp:
    cInd = i.index(':')
    gameId = int(i[5:cInd])

    nums = i[cInd+2:].split(';')
    minNums = {'red':0, 'blue':0, 'green':0}
    for j in nums:
        newNums = j.split(',')
        for k in newNums:
            if k[0] == ' ':
                k = k[1:]

            kNum = int(k[:k.index(' ')])
            kColor = k[k.index(' ') + 1:]

            if kNum > minNums[kColor]:
                minNums[kColor] = kNum

    ans += minNums['red'] *  minNums['green'] *  minNums['blue']
submit(DAY, PART, ans)