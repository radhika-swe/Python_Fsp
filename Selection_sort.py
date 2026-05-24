"""Selection Sort is a simple sorting algorithm that repeatedly finds the smallest element from the unsorted part of the array and places it at the correct position. It divides the array into sorted and unsorted sections. Its time complexity is O(n^2) and it works well for small datasets.
"""


def selection_sort(arr):
  length=len(arr)

  for i in range(0,length-1):
    min_index=1
    for j in range(i+1,length):
      if arr[j]<arr[min_index]:
        min_index=j
      if i!= min_index:
        arr[i],arr[min_index]=arr[min_index],arr[i]
  return arr

n=int(input("Enter the number of books : "))
arr = list(map(int, input("Enter the numbers marked on books").split()))
sorted_arr = selection_sort(arr)
print(sorted_arr)