import heap

a = [1,2,3,4,5,6,7,8,9,10]

print(f"before building heap {a}")

heap.buildHeap(a)

print(f"after building heap {a}")

print(f"max : {heap.getMax(a)}")

print(f"latest array status {a}")

heap.increaseKey(a,3,400)

print(f"latest array status {a}")

heap.increaseKey(a,8,30)

print(f"latest array status {a}")

heap.insert(a,15)
print(f"latest array status {a}")

heap.insert(a,12)
print(f"latest array status {a}")

heap.insert(a,500)
print(f"latest array status {a}")

heap.insert(a,50)
print(f"latest array status {a}")

