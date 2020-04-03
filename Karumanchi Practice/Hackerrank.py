
arr = [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]

n= sum(arr)

print(n)

n = len(arr)

count = 0
d = 3

for i in range(0,n-2):

        for j in range(i+1,n-1):

            for k in range(j+1,n):

                # print(arr[i],arr[j],arr[k])
                if((arr[j]-arr[i]) == (arr[k]-arr[j])):
                    if(d == (arr[j]-arr[i])):
                        print(arr[i],arr[j],arr[k])

                        count = count + 1

# for i in range(0,n-2):
#         for j in range(i+1,n-1):
#             for k in range(j+1,n):

                
#                 if((arr[j]-arr[i]) == (arr[k]-arr[j])):
#                     if(d == (arr[j]-arr[i])):
#                         print(arr[i],arr[j],arr[k])
#                         count = count + 1


print(count)