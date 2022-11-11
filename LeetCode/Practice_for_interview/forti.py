from collections import Counter, defaultdict

def func(arr, k):

    l, r = 0, len(arr)
    while l < r:

        mid = l + (r - l) // 2

        if arr[mid] < k:
            l = mid + 1
        else:
            r = mid
        
    if arr[l] == k:
        return l
    else:
        return -1

# arr = [1, 6, 10, 16, 21,......]
arr = [1, 3, 4, 3, 2]

print(func(arr, 2))