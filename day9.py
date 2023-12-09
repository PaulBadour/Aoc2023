'''
2182/2826

For being such an easy day, im upset i did not perform well, wasnt really feeling great though

'''

from aoclib import *
import re
DAY = 9
PART = 2

pInp = get_input(DAY)
ans = 0

for i in pInp:
    nums = []
    row = list(map(int, re.findall(r'-?\d+',i)))
    l = row[-1]
    f = row[0]
    while len(nums) == 0 or nums[-1].count(0) != len(nums[-1]):
        row = [row[j+1] - row[j] for j in range(len(row) - 1)]
        nums.append(row)

    t = 0
    for i in range(len(nums)):
        t = nums[len(nums) - i - 1][0] - t
    ans += f - t
submit(DAY, PART, ans)