# given a sorted list of number..find the ceil of the number

# ceil of the number is defined as smalles number greater than equal to k


a=[1,2,3,4,6,7,9,10]
k=5

start = 0
end = len(a)-1
res = -1
while start <= end:
    mid = (start+end)//2

    if a[mid] == k:
        res = mid
        break

    elif a[mid] < k:
        start = mid+1

    elif a[mid] > k:
        res = mid
        end = mid-1

print(a[res])