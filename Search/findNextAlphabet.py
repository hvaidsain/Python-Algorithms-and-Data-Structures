# given an array of sorted alphabet characters...find the next alphabet character
# in the array for a given chanracter k

# for example a = [a,b,c,f,h,j,m,n]
# k = g

# output = "h"


a = ["a","b","c","f","h","j","m","n"]

k = "d"
start = 0
end = len(a)-1

while start <= end:

    mid = start + (end - start)//2

    if ord(a[mid])==ord(k):
        start = mid+1

    elif ord(a[mid]) < ord(k):
        start = mid + 1
        

    elif ord(a[mid])> ord(k):
        res = mid
        end = mid - 1
        
        
    

print(a[res])

