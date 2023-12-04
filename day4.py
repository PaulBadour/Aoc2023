'''
757/670

VERY nearly had a great part one time but a parsing logic error held me back multiple minutes
Part 2 was pretty solid minus a slight misunderstanding of the rules on my part

'''

from aoclib import *
DAY = 4
PART = 2

pInp = get_input(DAY)
ans = 0

inst = [1 for i in range(len(pInp))]

for it, i in enumerate(pInp):
    wNums = i[i.index('|') + 2:].split(' ')
    hNums = i[i.index(':') + 2:i.index('|')-1].split(' ')

    score = 0

    for j in hNums:
        if j in wNums and j != '':
            #score = score * 2 if score != 0 else 1 PART ONE
            score += 1

    for j in range(score):
        if it + 1 + j < len(pInp):
            inst[it + 1 + j] += inst[it]

ans = sum(inst)
submit(DAY, PART, ans)