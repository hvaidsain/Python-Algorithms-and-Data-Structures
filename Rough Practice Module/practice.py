

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


k = 15

s = set()

flag = False

for i in range(0, len(a)):

    if((k-a[i]) in s):
        print("number exist")
        flag = True
        break
    elif(a[i] not in s):
        s.add(a[i])

if(flag == False):
    print("does not exxist")
