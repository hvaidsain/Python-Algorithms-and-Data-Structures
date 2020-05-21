#  given an array find the nearest greater element to the left...if no element
# then print -1

# for ex [2,3,1,4,6,5,8,7]

# ans [3,4,4,6,8,8,-1,-1]

# brute force solution : 
# time complexity O(n^2)

# for n^2 solutions....if in the second loop if j depends on i then problem can be 
# reduced to a stack problem

a = [2,3,1,4,6,5,8,7]

output = []

# for i in range(0,len(a)-1):
#     flag = 0
#     for j in range(i+1,len(a)):
#         if a[j]>a[i]:
#             output.append(a[j])
#             flag = 1
#             break

#     if flag == 0:
#         output.append(-1)

# # output.reverse()

# print(output)

# stack solution

stack = []
for i in range(len(a)-1,-1,-1):

    if(not stack):
        output.append(-1)

    elif(stack and stack[-1]<a[i]):

        while(stack and stack[-1]<a[i]):
            stack.pop()

        if(not stack):
            output.append(-1)
        else:
            output.append(stack[-1])

    elif(stack and stack[-1]>a[i]):
        output.append(stack[-1])

    stack.append(a[i])

output.reverse()

print(output)




