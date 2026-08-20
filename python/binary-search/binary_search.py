"""Functions to implement binary search"""

def find(search_list, value):
    return do_find(sorted(search_list), value, 0, len(search_list) -1)


def do_find(arr, target, left, right):
    if left > right:
        raise ValueError('value not in array')
    
    mid = (left + right) // 2
    
    if arr[mid] > target:
        return do_find(arr, target, left, mid - 1)
    if arr[mid] < target:
        return do_find(arr, target, mid + 1, right)
    return mid
