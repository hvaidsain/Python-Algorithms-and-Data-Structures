# Given and infinite array...find the the index of the given number

# for example a = [1,2,3,4,5,12,23,34,45,46,47,56,57,67,68,78,79,......]

# k = 12
# output =4
import bs

a = [1, 2, 3, 4, 5, 12, 23, 34, 45, 46, 47, 56, 57, 67, 68, 78, 79]

k = 1

start = 0
end = 1

while a[end] < k:
    start = end
    end = end * 2

print(bs.binarySearch(a, start, end, k))




    



