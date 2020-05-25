# Given an almost sorted array...find an element x and return
# it index.
# Almost sorted array means that an element element can be in its sorted 
# position i or i+1 or i-1.

# for example a = [1,2,4,3,5,6,8,7] sorted arr = [1,2,3,4,5,6,7,8]

a = [1,2,4,3,5,6,8,7]
k = 7

start =0
end = len(a)-1
res = -1
while start <= end:

    mid = (start + end) // 2

    if a[mid] == k:
        res = mid
        break

    elif mid-1 >= start and a[mid-1] ==k:
        res = mid-1
        break
    elif mid+1 <= end and a[mid+1] ==k:
        res = mid+1
        break
    elif k > a[mid]:
        start = mid+2
    
    elif k < a[mid]:
        end = mid-2

print(res)