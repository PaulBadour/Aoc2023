'''
360/2567

Part 1 went smoothly with recursion
Part 2 taught me to always think about dynamic programing if your first thought is recursion
'''
from copy import copy
from aoclib import *
import functools
import re
DAY = 12
PART = 2


# patterns = {}
cache = {}
# pInp = get_example(DAY,offset=1)
pInp = get_input(DAY)
ans = 0

# def genPatt(p):
#     pattern = ''
#     for i in p:
#         pattern += '#{' + str(i) + '}\.*'
#     return pattern


def halfCheck(s):
    nums = []
    inside = False
    c = 0
    lastQ = False
    for i in s[0]:
        if i == '?':
            lastQ = True
            break
        if inside:
            if i == '#':
                c += 1
            else:
                inside = False
                nums.append(c)
        elif i == '#':
            inside = True
            c = 1

    if inside and not lastQ:
        nums.append(c)
    if inside and lastQ and len(nums) < len(s[1]) and c > s[1][len(nums)]:
        return False
    # if not lastQ and nums == s[1][:-1]:
    #     return 

    if nums == s[1] and not lastQ:
        return 1
    return nums == s[1][:len(nums)]


def check(s):
    # global patterns
    nums = []
    inside = False
    c = 0
    for i in s[0]:
        if inside:
            if i == '#':
                c += 1
            else:
                inside = False
                nums.append(c)
        elif i == '#':
            inside = True
            c = 1

    if inside:
        nums.append(c)
    #print(s, nums)
    #input()
    return nums == s[1]
    # p = None
    # if ','.join([str(i) for i in s[1]]) in patterns.keys():
    #     p = patterns[','.join([str(i) for i in s[1]])]
    # else:
    #     p = genPatt(s[1])
    #     patterns[','.join([str(i) for i in s[1]])] = p

    # return True if re.fullmatch(p, s[0]) != None else False

def poss(s):
    #print(s)
    if s[0].count('?') > 0:
        r  = halfCheck(s)
        if type(r) is int:
            return r
        if not r:
            return 0
        p1,p2 = copy(s),copy(s)
        p1[0]=p1[0].replace('?','.',1)
        p2[0]=p2[0].replace('?','#',1)
        #print('recurse', p1,p2)
        return poss(p1) + poss(p2)
    else:
        #print('returning')
        return 1 if check(s) else 0
    

def takeTwo(x):
    global cache
    name = '{};{}'.format(x[0],x[1])
    if name in cache:
        return cache[name]
    s = copy(x)

    if len(s[1]) == 0:
        return 1 if '#' not in s[0] else 0
    
    t = 0
    num = s[1][0]
    for j in range(len(s[0])):
        if j+num <= len(s[0]) and s[0][j:j+num].count('.') == 0 and (j == 0 or s[0][j-1] != '#') and (j + num == len(s[0]) or s[0][j+num] != '#'):
            t += takeTwo((s[0][j + num + 1:], s[1][1:]))
        if s[0][j] == '#':
            break
    cache[name] = t
    return t

for num, i in enumerate(pInp):
    #print(num)
    i = i.split(' ')
    i[0] = '?'.join([i[0] for j in range(5)])
    i[1] = ','.join([i[1] for j in range(5)])
    i[1] = list(map(int, i[1].split(',')))
    # if num < 9:
    # ans += poss(i)
    ans += takeTwo(i)
    #input(ans)
submit(DAY, PART, ans)