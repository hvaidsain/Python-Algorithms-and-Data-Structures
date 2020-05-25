# given a sorted array which is rotated . 
# Find and the return element k in the array

# for example a = [12,14,16,18,2,3,5,6,7,8,9]

# return index of k = 8 output = 9



a = [12,14,16,18,2,3,5,6,7,8,9]
k = 9

res = -1


start = 0
end = len(a)-1

while(start<=end):
    mid = (start+end)//2
    
    if a[mid]==k:
        res = mid
        break
    else:
        if a[mid]>a[start]:

            if k<a[mid] and k >=a[start]:
                end = mid-1
            elif k<a[start]:
                start = mid+1

        if a[mid]<a[end]:

            if  k>a[mid] and k <= a[end]:
                start = mid+1
            elif k>a[end]:
                end = mid-1

    

print(res)

