# s =[0]*10

# print(s)

a = [2,1,1,1]

maxi = a[0]
second = a[len(a)-1]

for i in range(len(a)):

    if(a[i]>maxi):
        maxi = a[i]
    elif(a[i]>second and a[i]<maxi ):
        second = a[i]

print("second:{}".format(second))
print("max:{}".format(maxi))

# a = [2,7,4,1,8,1]

# while(len(a)>1):
#     max1 = 0
#     max2 = 0
#     for i in range(len(a)):
#         if(a[i]>a[max1]):
#             max2 = max1
#             max1 = i
#         elif(a[i]>a[max2]):
#             max2 = i
                    
#     if(a[max1] == a[max2]):
#             a.remove(a[max1])
#             a.remove(a[max2])
                
#     elif(a[max1] != a[max2]):
#         a[max1] = a[max1] - a[max2]
#         a.remove(a[max2])

#     print(a)
                

# print(a)

