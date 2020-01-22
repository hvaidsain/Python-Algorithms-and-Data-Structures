def Main():
    arr = [23,43,54,2,4,1,57,26,36,87,6,11]

    insertionSort(arr)

    print(arr)



def insertionSort(a):

    for i in range(1,len(a)):
        num = a[i]

        k=i-1

        while(k>=0 and num < a[k]):
            a[k+1] = a[k]
            k = k-1
        
        a[k+1] = num



if __name__ == "__main__":
    Main()


