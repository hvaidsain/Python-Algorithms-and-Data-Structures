
def fibo(n):
    first = 1
    second = 1
    if(n == 1 or n == 2):
        return 1
    res = 0
    for i in range(0, n-2):
        res = first + second

        first = second
        second = res

    return res


def Main():

    res = fibo(7)
    print(res)


if __name__ == "__main__":
    Main()
