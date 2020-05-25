# Given an array find the maximum size subarray with sum less than equal to k

# for ex : [2,4,5,1,0,0,0,0,3,-1,9,7]  K = 12

# return the maximum subarray length

# brute force solution....find all possible subarrays

# sliding window technique
import sys

a=[2,4,5,1,0,0,0,0,3,-1,9,7] 
k = 12

left = 0
maxi = -1*(sys.maxsize)
sum = 0

for i in range(0,len(a)):
    sum = sum + a[i]

    while sum>k and left<=i:
        sum = sum - a[left]
        left = left + 1

    maxi = max(maxi,i-left+1)

print(maxi)


