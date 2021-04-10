n = input().split('-')

k = list(map(int, n[0].split('+')))
result = sum(k)

#for i in n[0].split('+'):
#    result = int(i)

for i in n[1:]:
    s = list(map(int, i.split('+')))
    result -= sum(s)
print(result)
