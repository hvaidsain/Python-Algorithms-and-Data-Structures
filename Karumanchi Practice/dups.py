#Find if array has duplicates

#hashtable method



def Main():

    a = [1,2,3,1,4,5,6,7]
    print(findDuplicate(a))
    
def findDuplicate(a):
    x = dict()
    for i in range(0,len(a)):
        if a[i] in x:
            return a[i]
        else:
            x[a[i]] = 1
    
    return "No Duplicates"







if __name__ == "__main__":
    Main()