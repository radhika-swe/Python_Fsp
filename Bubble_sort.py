def bubble_sort(arr):
    length = len(arr)

    for i in range(0, length - 1):
        for j in range(0, length - i - 1):

            if arr[j]>arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]

    return arr

n=int(input("Enter the number of students"))
arr = list(map(int, input("Enter the heights of student").split()))
sorted_arr = bubble_sort(arr)
print(sorted_arr)