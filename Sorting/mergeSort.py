
def Main():
    a = [21,1,43,25,45,32,6,4,87,25,67,65,9]
    print(a)
    mergeSort(a,0,len(a)-1)

    print(a)




def merge(a,first,mid,last):
    x = [None] * (last-first + 1)

    p = first
    q = mid+1

    r = 0

    while(p<=mid and q<=last):
        if(a[p]<= a[q]):
            x[r] = a[p]
            p = p+1
            r = r + 1
        
        elif(a[q]<a[p]):
            x[r] = a[q]
            q = q+1
            r = r + 1
    
    if(p<= mid or q<=last):

        while(p<=mid):
            x[r] = a[p]
            p=p+1
            r=r+1
        while(q<=last):
            x[r] = a[q]
            q=q+1
            r=r+1
    print(x)

    for i in range(0,len(x)):
        a[first] = x[i]
        first = first+1
    


        

def mergeSort(a,first,last):

    if(first<last):

        mid = (first+last)/2 
        mergeSort(a,first,mid)
        mergeSort(a,mid+1,last)
        merge(a,first,mid,last)
    

if __name__ == "__main__":
    Main()