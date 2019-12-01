import math
# First of All Binary Search works on sorted list
# Algo - We first check whether the midlle item matches the search key if yes then return middle
# or else if the key is less then we search in the first half of the list or else in 2nd half
# Hence this way we reject the half of the list in each iteration

# Time complexity O(logn)
# Space Complexity O(1)


def binarySearch(list, key):  # list is sorted

    first = 0
    last = len(list)-1

    while (first <= last):
        mid = int((first+last)/2)

        if(key == list[mid]):
            return True

        elif(key < list[mid]):
            last = mid-1

        else:
            first = mid+1
    return False


def Main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 12, 23, 24, 45, 56, 67]
    res = binarySearch(list, 47)
    print(res)


if __name__ == "__main__":
    Main()
