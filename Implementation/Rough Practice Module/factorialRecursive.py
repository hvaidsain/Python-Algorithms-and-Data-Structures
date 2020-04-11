
def fact(n):
    if(n == 1 or n == 0):
        return 1

    return n * fact(n-1)


def Main():
    res = fact(10)
    print(res)


if __name__ == "__main__":
    Main()
