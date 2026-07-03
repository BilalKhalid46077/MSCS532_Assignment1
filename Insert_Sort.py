"""
MSCS532 Assignment 1
Bilal Khalid
Insertion Sort - Sorting Array In Descending Order

"""

def Insert_Sort(arr):

    for j in range(1, len(arr)):

        key = arr[j]

        i = j - 1

        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1

        arr[i + 1] = key

    return arr


numbers = [12, 5, 8, 19, 3, 15]

print("Original Array: ", numbers)

sorted_numbers = Insert_Sort(numbers)

print("Sorted Array in Descending Order: ", sorted_numbers)
