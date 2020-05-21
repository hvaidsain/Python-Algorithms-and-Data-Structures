# nearest gratest element to the right
# given an array find the nearest greater element to the right for each element in
# the array
# print -1 if no nearest element found

# for example: [2,4,3,6,5,7,1,9,8]

# output = [-1,-1,4,-1,6,-1,7,-1,9]

a = [2,4,3,6,5,7,1,9,8]

output = []
output.append(-1)



# brute force solution

# for i in range(1,len(a)):
#     flag = 0
#     for j in range(i-1,-1,-1):
#         if a[j] > a[i]:
#             output.append(a[j])
#             flag=1
#             break
#     if flag == 0:
#         output.append(-1)

# print(output)

# stack solution

stack = []




