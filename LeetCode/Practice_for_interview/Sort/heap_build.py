def build_heap(arr):
    n = len(arr)
    for i in reversed(range(n//2)):
        adjust(arr, i, n-1)

def adjust(arr, root, high):
    if root > high:
        return
    child = 2 * root + 1
    tmp = arr[root]
    while child < high:
        if child + 1 <= high and arr[child] < arr[child+1]:
            child += 1
        if tmp > arr[child]:
            break
        arr[root] = arr[child]
        root = child
        child = child * 2 + 1
    arr[root] = tmp

arr = [5, 3, 2, 7, 1]
build_heap(arr)
print(arr)
