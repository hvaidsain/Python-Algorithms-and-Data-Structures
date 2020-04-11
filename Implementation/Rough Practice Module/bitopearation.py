

a=[1,2,3,4,5,6,7,7,8]

res1 = 0



res2 = 0

for i in range(0,len(a)):
    res1 = res1 ^ a[i]

for x in range(1,9):
    res2 = res2 ^ x


print(res1^res2)
