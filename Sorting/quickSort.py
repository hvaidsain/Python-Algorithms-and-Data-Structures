


def pivot(a,first,last):

    x = a[last]

    i = first-1

    for j in range (first,last):

        if(a[j]<=x):
            i = i+1
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
        
    temp = a[i+1]
    a[i+1] = a[last]
    a[last] = temp

    return i+1



def quick(arr,first,last):

    if(first<last):
         piv = pivot(arr,first,last)
         quick(arr,first,piv-1)
         quick(arr,piv+1,last)

    



arr = [23,43,54,2,4,1,57,26,36,87,6,11]

quick(arr,0,len(arr)-1)

print(arr)

