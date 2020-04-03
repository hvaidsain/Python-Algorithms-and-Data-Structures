#Find number occuring max no. of times



def Main():
    a = [1,2,3,4,5,6,3,2,4,5,6,4,3,3,4,4,4,5,5,6,7,8,9,8,7,6,5,5,5]
    #brute force technique

    highestFreq = findFreqBruteForce(a)
    print(highestFreq)
    
    #hashtable technique

    highestFreq = findFreqHashTech(a)
    print(highestFreq)

def findFreqHashTech(a):
    max = 0
    counter = 0
    x = dict()

    for i in range(0,len(a)):
        if a[i] in x:
            x[a[i]] = x[a[i]] + 1
        else:
            x[a[i]] = 1
    
    for key,value in x.items():
        if(value>counter):
            counter = value
            max = key

    return max

def findFreqBruteForce(a):
    max = 0
    counter = 0
    for i in range(0,len(a)):
        counter = 0
        for j in range(0,len(a)):
            if(a[i]==a[j]):
                counter+=1
        if(counter>max):
            max = a[i]

    return max

if __name__ == "__main__":
    Main()