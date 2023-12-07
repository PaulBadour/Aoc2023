'''
1230/5358

Part one turned out fine, im happy with the rank hand function
Part two had many many frustrating bugs along with a few minsunderstandings

'''

from aoclib import *
from collections import Counter
DAY = 7
PART = 2

pInp = get_input(DAY)
ans = 0

def sort(c):
    ranks = ('A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J')[::-1]
    ans = c[1]*100
    ans += ranks.index(c[0])
    return ans

def jRank(x):
    t = dict(Counter(x))
    del t['J']
    counts = sorted([(i, j) for i,j in t.items()], key=sort, reverse=True)
    #print(counts, x)

    if len(counts) != 0:
        
        repLet = counts[0][0]
        x=x.replace('J',repLet)
    else:
        x = "AAAAA"

    #print(x)
    #input()
    return rankHand(x)

def rankHand(x):

    if x.count(x[0]) == 5:
        # print(x, ' is 7')
        return 7
    elif x.count(x[0]) == 4 or x.count(x[1]) == 4:
        # print(x, ' is 6')
        return 6
    elif len(set(list(x))) == 2:
        # print(x, ' is 5')
        return 5
    elif x.count(x[0]) == 3 or x.count(x[1]) == 3 or x.count(x[2]) == 3:
        # print(x, ' is 4')
        return 4
    elif len(set(list(x))) == 3:
        # print(x, ' is 3')
        return 3
    elif len(set(list(x))) == 4:
        # print(x, ' is 2')
        return 2
    else:
        # print(x, ' is 1')
        return 1


def switch(x,y):
    ranks = ('A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J')
    if 'J' in x:
        xr = jRank(x.split(' ')[0])
    else:
        xr = rankHand(x.split(' ')[0])

    if 'J' in y:
        yr = jRank(y.split(' ')[0])

    else:
        yr = rankHand(y.split(' ')[0])


    if xr == yr:
        for i in range(5):
            if ranks.index(x[i]) < ranks.index(y[i]):
                #print('x')
                xr+= 1
                break
            elif ranks.index(x[i]) > ranks.index(y[i]):
                #print('y')
                yr+= 1
                break

    if xr > yr:
        #print('switching ', x, y)
        return True
    
    return False

sorting = True
while sorting:
    #input(pInp)
    sorting = False
    for i in range(len(pInp) - 1):
        if switch(pInp[i], pInp[i+1]):
            temp = pInp[i]
            pInp[i] = pInp[i+1]
            pInp[i+1] = temp
            sorting = True

#print(pInp)
for num,i in enumerate(pInp):
    bid = int(i.split(' ')[1])
    ans += bid * (num+1)

submit(DAY, PART, ans)