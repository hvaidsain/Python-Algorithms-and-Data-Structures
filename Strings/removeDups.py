#using hash Set method
st = set()
s="javalavacadara"


for char in s:
    st.add(char)

print(st)

def removeDups(s):
    noRep=""
    for x in s:
        if(x in st):
            noRep+=x
            st.remove(x)

    print(noRep)

def main():

    removeDups(s)





if __name__ == "__main__":
    main()



