# Give an array for a price of stock for different days...find the number of
# consecutive days the stock price is less than or equal to the price on the given 
# day including the given day

# example = [100, 80, 60, 70, 60, 75, 85]

# output = [1, 1, 1, 2, 1, 4, 6]


a = [100, 80, 60, 70, 60, 75, 85]

output = []

stack = []

for i in range(0,len(a)):
    if not stack:
        output.append(-1)

    elif stack and stack[-1][0]>a[i]:
        output.append(stack[-1][1])

    elif stack and stack[-1][0]<a[i]:
        while stack and stack[-1][0]<a[i]:
            stack.pop()

        if not stack:
            output.append(-1)
        else:
            output.append(stack[-1][1])

    stack.append([a[i],i])


for i in range(0,len(a)):
    output[i] = i - output[i]

print(output)

    

