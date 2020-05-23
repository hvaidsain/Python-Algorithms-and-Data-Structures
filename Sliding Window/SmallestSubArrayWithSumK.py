# Given an array find the smallest subarray with sum greater than equal to k

# for ex : [2,4,5,8,3,1,9,7] K = 12

# return the smallest subarray length

# brute force solution....find all possible subarrays

import sys
a=[2,4,5,8,3,1,9,7] 
k = 12
mini = sys.maxsize

# for i in range(0,len(a)):
#     sum = 0
#     for j in range(i,len(a)):
#         sum = sum + a[j]

#         if sum >= k:
#             mini = min(mini,j-i+1)

# print(mini)

left = 0
sum = 0
for i in range(0,len(a)):
    sum = sum + a[i]

    while sum>=k and left<=i:
        mini = min(mini,i-left+1)
        sum = sum - a[left]
        left+=1
        
print(mini)

        
