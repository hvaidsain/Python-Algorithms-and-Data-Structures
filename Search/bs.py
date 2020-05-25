def binarySearch(a, first, end, k):
    
    while first <= end:
        mid = (first + end) // 2
        
        if a[mid] == k:
            return mid

        elif a[mid] < k:
            first = mid + 1
            
        elif a[mid] > k:
            end = mid - 1
            

    return - 1