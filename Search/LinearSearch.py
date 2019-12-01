
def linearSearch(list, key):

    for item in list:
        if (key == item):
            return True

    return False


def Main():

    x = [2, 4, 6, 7, 12, 43, 24, 65]

    res = linearSearch(x, 8)
    print(res)


if __name__ == "__main__":
    Main()
