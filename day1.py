'''
604/1103

first solution was fine, could have been improved if I knew about str.isdigit
Second part was rough, I am sure there are better ways of doing it but I had some brain farts

'''

from aoclib import *
DAY = 1
PART = 2
pInp = get_input(DAY)
ans=0
nums = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
revNums = tuple(map(lambda x: x[::-1], nums))
for i in pInp:
    f = 0
    c=0
    while f == 0:
        try:
            f=int(i[c])

        except:
            
            for j in nums:
                if i[c:c+len(j)] == j:
                    f = nums.index(j)
                    break
        c+= 1
    l=0
    c=0
    while l == 0:
        try:
            l=int(i[-1 - c])

        except:

            
            for j in revNums:
                if i[::-1][c:c+len(j)] == j:
                    l = revNums.index(j)
                    break

        c+= 1

    ans += int(f'{str(f)}{str(l)}')


submit(DAY, PART, ans)