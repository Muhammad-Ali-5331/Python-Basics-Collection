def SelectionSort(arr: list[int]) -> list[int]:
    """
    Implements the Selection Sort algorithm to sort a list of integers
    in ascending order.

    The algorithm finds the minimum element in the unsorted portion and
    swaps it with the element at the current position 'i'.

    Time Complexity: O(n^2)
    """
    n = len(arr)
    # Outer loop iterates through all elements of the array
    for i in range(n):
        # Assume the current element is the minimum of the unsorted section
        min_index = i

        # Inner loop searches for the actual minimum element in the remaining unsorted array (from i+1 to the end)
        for j in range(i + 1, n):
            # CRITICAL FIX: Compare arr[j] against the current minimum (arr[min_index]),
            # NOT the starting element (arr[i])
            if arr[j] < arr[min_index]:
                min_index = j

        # If the minimum element found is not the current element, swap them
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == "__main__":
    # Sample input array
    data = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(f"Original Array: {data}")
    # Execute the sort and print the result
    sorted_data = SelectionSort(data)
    print(f"Sorted Array: {sorted_data}")