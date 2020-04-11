#binary search

#a = [1,2,3,4,5,6,7,6,5,4,3,2,1]

# a = [1,2,3,4,5,6,7]


# first = 0
# last = len(a) - 1

# res = -1

# while(first <= last):

#     mid = int((first + last)/2)

#     if(a[mid]>a[mid+1] and a[mid]>a[mid-1]):
#         res = a[mid]
#         break

#     elif(a[mid] > a[mid-1] and a[mid] < a[mid+1]):
#         first = mid+1

#     else:
#         last = mid - 1


# if(res == -1):
#     print("no such number")
# else:
#     print("number is:",res)

def swap(i,mid):
    temp = a[i]
    a[i] = a[mid]
    a[mid]= temp



a = [2,2,1,2,1,2,1,0,1,0,2,1,0,2,1,2,0,1,2,1,2]


f = 0
mid = 0
l= len(a)-1

while(mid<l):
    if(a[mid]==0):
        swap(f,mid)
        f = f+1
        mid = mid+1
        
    elif(a[mid]==1):
        mid = mid +1
    elif(a[mid]==2):
        swap(l,mid)
        l = l-1
        


print(a)













# i = -1

# for k in range(0,len(a)):
#     if(a[k]==0):
#         i = i+1
#         temp = a[k]
#         a[k] = a[i]
#         a[i] = temp
    
# for j in range(i+1,len(a)):
#     if(a[j]==1):
#         i = i+1
#         temp = a[j]
#         a[j] = a[i]
#         a[i] = temp


# print(a)

