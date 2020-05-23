# Given an array...find the nearest lowest element to the right for 
# all elements of the array..if not found print -1

# for example a = [2,4,1,5,8,6,3,7]

# output = [1,1,-1,3,6,3,-1,-1]

# brute force solution

a = [2,4,1,5,8,6,3,7]

output = []

# for i in range(0,len(a)-1):
#     flag = 0
#     for j in range(i+1,len(a)):
#         if a[j]<a[i]:
#             flag = 1
#             output.append(a[j])
#             break
#     if flag == 0:
#         output.append(-1)

# output.append(-1)

# print(output)

# stack solution

stack = []

for i in range(len(a)-1,-1,-1):
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


output.reverse()
print(output)
