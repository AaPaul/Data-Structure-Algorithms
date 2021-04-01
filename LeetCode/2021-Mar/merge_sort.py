def merge_sort_recursive(arr: list):
    if len(arr)<=1:
        return arr
    mid = len(arr)/2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i<len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

new_list = merge_sort_recursive([14, 12, 15, 13, 16])
print(new_list)





arr = [14, 12, 15, 13, 11, 16]
merge_sort_recursive(arr)