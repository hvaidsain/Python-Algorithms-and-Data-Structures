
# find maximum number of continuos 1's is a binary array

import sys

a = [0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0]

cnt = 0
maxi = -1*(sys.maxsize)

for i in range(0,len(a)):
    if a[i] == 0:
        cnt = 0

    else:
        cnt+=1
        maxi = max(maxi,cnt)

print(maxi)