def bubbleSort(arr:list[int]) -> list[int]:
    for i in range(len(arr)):
        swappingOuccurred = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swappingOuccurred = True
        if not swappingOuccurred:
            break
    return arr

if __name__ == "__main__":
    print(bubbleSort([9,8,7,6,5,4,3,2,1]))