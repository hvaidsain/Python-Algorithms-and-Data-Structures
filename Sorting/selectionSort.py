

def Main():
    a = [21,1,43,25,45,32,6,4,87,25,67,65,9]

    print("before sorting",a)

    selectionSort(a)

    print("after sorting",a)
    


def selectionSort(a):

    for i in range(0,len(a)-1):
        min = i
        for j in range (i+1,len(a)):
            if(a[j]<a[min]):
                min = j
        
        temp = a[i]
        a[i] = a[min]
        a[min] = temp





    
if __name__ == "__main__":
    Main()


