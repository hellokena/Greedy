import sys

tc = 1
while True:
    l,p,v = list(map(int, sys.stdin.readline().rstrip().split()))
    if l==0 and p==0 and v==0: break
    else:
        day = 0
        while v>0:
            if v<=l:
                day+=v
                brea
            day += l
            v -= p
        print('Case '+str(tc)+': '+str(day))
        tc += 1
