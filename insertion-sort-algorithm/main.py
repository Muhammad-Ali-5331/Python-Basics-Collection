# ------------------------------- Insertion Sort Implementation ------------------------------- #

def insertionSort(arr: list[int]) -> list[int]:
    """ Sorts a list of integers using the insertion sort algorithm. """

    # Start from the second element (index 1) cosidering the first element is already "sorted"
    for i in range(1, len(arr)):

        # Store the current element to be compared and inserted
        current_value = arr[i]

        # Initialize j to the index before i to compare backwards
        j = i - 1

        # Shift elements in the sorted portion (left side) that are greater than current_value
        while j >= 0 and current_value < arr[j]:
            arr[j + 1] = arr[j]  # Move the larger element one step to the right
            j -= 1  # Move left in the array

        # Insert current_value into its correct sorted position
        arr[j + 1] = current_value

    # Return the sorted list
    return arr


# ------------------------------- Example Usage ------------------------------- #
if __name__ == "__main__":
    print(insertionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))