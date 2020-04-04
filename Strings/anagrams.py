

s1 = "mary"

s2 = "ramy"

#sorting method

# s1 = "".join(sorted(s1))

# s2 = "".join(sorted(s2))

# print(s1==s2)


#hashing method

d1 = dict()
d2 = dict()

for i in s1:
    if i in d1:
        d1[i] = d1[i]+1
    else:
        d1[i] = 1

for i in s2:
    if i in d2:
        d2[i] = d2[i]+1
    else:
        d2[i] = 1

#if dictionary comparison returns 0 then dict is equal else not

print(cmp(d1,d1))

