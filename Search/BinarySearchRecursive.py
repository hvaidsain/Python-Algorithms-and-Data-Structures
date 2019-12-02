
def binarySearch(list, key, first, last):

    if(first > last):
        return False

    mid = int((first+last)/2)

    if(key == list[mid]):
        return True
    elif(key > list[mid]):
        return binarySearch(list, key, mid+1, last)
    else:
        return binarySearch(list, key, first, mid-1)


def Main():

    list = [1, 2, 3, 4, 5, 6, 7, 8, 12, 23, 34, 45, 56, 67, 78]
    res = binarySearch(list, 90, 0, len(list)-1)
    print(res)


if __name__ == "__main__":
    Main()
