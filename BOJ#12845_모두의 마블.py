import sys
n = int(sys.stdin.readline().rstrip())
gold = 0
cardlevel = list(map(int, sys.stdin.readline().rstrip().split()))
cardlevel.sort()
while len(cardlevel) > 1:
    newcardlevel = max(cardlevel[-1], cardlevel[-2])
    gold += cardlevel[-1] + cardlevel[-2]
    cardlevel.remove(cardlevel[-1])
    cardlevel.remove(cardlevel[-1])
    cardlevel.append(newcardlevel)
print(gold)
