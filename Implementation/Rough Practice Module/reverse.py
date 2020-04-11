

reversing a string
s = "abcd"
rev = ""
for i in range(len(s)-1,-1,-1):
    rev = rev + s[i]

print(rev)

sorting a string

s = '4343434'



res = ''.join(sorted(s))

print(res)