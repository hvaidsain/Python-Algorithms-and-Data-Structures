
def factorial(n):
    fact = 1

    for i in range(1, n+1):
        fact = fact*i

    return fact


def Main():

    res = factorial(40)
    print(res)


if __name__ == "__main__":
    Main()
