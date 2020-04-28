import heapq as heap

l1 = [23,12,43,2,54,36,1,22,9]

heap.heapify(l1)
print(l1)

print(heap.heappop(l1))
print(l1)


heap.heappush(l1,-10)
print(l1)
print(heap.heappop(l1))

