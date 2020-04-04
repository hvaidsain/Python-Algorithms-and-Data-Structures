# max occurring character in a given string

# solving using hashtable (dictionary)

str = "asbakahajanabaiauayagavafarat"

count = dict()
maxCount = -1
maxChar=""

for char in str:
    if(char in count):
        count[char] = count[char] + 1
    else:
        count[char] = 1

for k,v in count.items():
    if(v>maxCount):
        maxCount = v
        maxChar=k

print("Frequecy of all charaters:")
print(count)

print("Max Occuring charater is "+maxChar)