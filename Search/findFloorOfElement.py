# given a sorted list of number..find the floor of the number

# floor of the number is defined as greatest number less than equal to k

a=[1,2,3,4,6,7,9,10]
k=8

start = 0
end = len(a)-1
res = -1
while start <= end:
    mid = (start+end)//2

    if a[mid] == k:
        res = mid
        break

    elif a[mid] < k:
        res = mid
        start = mid+1

    elif a[mid] > k:
        end = mid-1

print(a[res])


