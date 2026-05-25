def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
arr = list(map(int, input("Enter the sorted array: ").split()))
target = int(input("Enter the target element: "))
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")




