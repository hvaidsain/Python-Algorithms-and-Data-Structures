# Check if the given string is pallindrome
# if pallindrome then return "YES" else return "NO"

def isPallindrome(str):
    rev = ''
    for i in range(len(str)-1,-1,-1):
        rev = rev+str[i]

    print("rev:"+rev+" str:"+str)
    if(rev==str):
        return "YES"

    return "NO"


def Main():
    str = "arora"
    result = isPallindrome(str)
    print(result)

if __name__ == "__main__":
    Main()