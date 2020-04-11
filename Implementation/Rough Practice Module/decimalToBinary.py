


def binaryRepresentation(x):
    
    binary =""

    while(x!=0):
        binary = str(x%2) + binary
        x=x/2

    print(int(binary))

def main():
    x = 10
    binaryRepresentation(x)

if __name__ == "__main__":
    main()