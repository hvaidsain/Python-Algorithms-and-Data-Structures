

count = 0
page = 0
    
for i in range(0,n):

    
    for j in range(1,arr[i]+1):

        if(j==1):
            page = page+1
            print(page)
        if(j>k):
            page = page+1
            print(page)
        if(page == j):

            count = count+1
                