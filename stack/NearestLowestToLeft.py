# Given an array...find the nearest lowest element to the left for 
# all elements of the array..if not found print -1

# for example a = [2,4,1,5,8,6,3,7]

# output = [-1,2,-1,1,5,5,1,3]

# brute force solution

a = [2,4,1,5,8,6,3,7]

output = []
# output.append(-1)
n = len(a)


# for i in range(1,n):
#     flag = 0
#     for j in range(i-1,-1,-1):
#         if a[j]<a[i]:
#             output.append(a[j])
#             flag=1
#             break
#     if flag == 0:
#         output.append(-1)

# print(output)

# stack solution


stack = []

for i in range(0,n):
    if not stack:
        output.append(-1)
    elif stack and stack[-1]<a[i]:
        output.append(stack[-1])
    elif stack and stack[-1]>a[i]:

        while stack and stack[-1]>a[i]:
            stack.pop()

        if not stack:
            output.append(-1)
        else:
            output.append(stack[-1])

    stack.append(a[i])

    
print(output)


