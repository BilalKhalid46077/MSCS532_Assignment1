"""
MSCS532 Assignment 1
Bilal Khalid
Implementation of the Insertion Sort Algorithm that sorts numbers in monotonically decreasing order.

"""

def Insertion_Sort(arr):

    # Start from the second element
    for j in range(1, len(arr)):

        key = arr[j]

        i = j - 1

        # Move elements of the array that are greater than key to one position ahead of their current position
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1

        # Insert the key into its correct sorted position
        arr[i + 1] = key

    return arr


def main():

    numbers = [12, 5, 8, 19, 3, 15]

    print("=" * 45)
    print("Insertion Sort: ")
    print("=" * 45)

    print("\nOriginal Array: ", numbers)

    Insertion_Sort(numbers)

    print("\nSorted Array: ", numbers)


if __name__ == "__main__":
    main()
