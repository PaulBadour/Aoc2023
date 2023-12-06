'''
1428/1040

I am cursed by simple logic errors when writing code fast that hold me back
Part 2 scared me into thinking I would need to optimize my code but it worked fine

'''
from aoclib import *
import re
DAY = 6
PART = 2

pInp = get_input(DAY)
ans = 0

amts = []

times = int(''.join(re.findall(r'\d+',pInp[0])))
dists = int(''.join(re.findall(r'\d+',pInp[1])))


amt = 0
for j in range(times):
    if (times - j) * j > dists:
        amt += 1

ans = amt

submit(DAY, PART, ans)