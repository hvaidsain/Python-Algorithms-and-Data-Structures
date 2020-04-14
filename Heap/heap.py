import sys
# takes an array and index q of the element that we need to heapify
# time complexity : O(logn)
def heapify(a,i):
    n = len(a)
    left = 2*i +1
    right = 2*i +2

    largest = i

    if(left<n and a[left]>a[largest]):
        largest = left

    if(right<n and a[right]>a[largest]):
        largest = right

    if(largest!=i):
        temp = a[i]
        a[i] = a[largest]
        a[largest] = temp
        heapify(a,largest)

# time complexity : O(n)
def buildHeap(a):

    n = len(a)

    l = n//2 - 1

    for i in range(l,-1,-1):
        heapify(a,i)

# time complexity : O(logn)
def getMax(a):

    if len(a)==0:
        return "Heap is empty"
    maxi = a[0]
    last = len(a)-1
    a[0] = a[last]
    a.pop()
    heapify(a,0)

    return maxi



# time complexity : O(logn)
def increaseKey(a,i,key):
    if(i>=len(a)):
        return "key index to large"
    if(len(a)==0):
        return "Heap is empty"

    a[i] = key
    while(i>0 and a[i//2] < a[i]):
        temp = a[i//2]
        a[i//2] = a[i]
        a[i] = temp
        
        i = i//2

def insert(a,key):

    a.append(-9)

    i = len(a) - 1

    increaseKey(a,i,key)




        


