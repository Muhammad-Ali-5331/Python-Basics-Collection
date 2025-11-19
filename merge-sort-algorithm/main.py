def MergeSort(arr: list[int]):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_array = arr[:mid]
        right_array = arr[mid:]
        MergeSort(left_array)
        MergeSort(right_array)
        merge(arr, left_array, right_array)


def merge(ARRAY: list[int], left: list[int], right: list[int]):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ARRAY[k] = left[i]
            i += 1
        else:
            ARRAY[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        ARRAY[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        ARRAY[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    MergeSort(array)
    print(*array)