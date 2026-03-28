def merge(left,right,mid,Arr):
    leftRange = mid-left+1
    rightRange = right-mid
    L = [Arr[left+i] for i in range(leftRange)]
    R = [Arr[mid+i+1] for i in range(rightRange)]
    i = j = 0
    k = left
    while i < leftRange and j < rightRange:
        if L[i]<R[j]:
            Arr[k] = L[i]
            i+=1
        else:
            Arr[k] = R[j]
            j+=1
        k+=1
    while i < leftRange:
        Arr[k] = L[i]
        i += 1
        k+=1
    while j < rightRange:
        Arr[k] = R[j]
        j += 1
        k+=1
def MergeSort(L,R,Arr):
    if L < R:
        mid = (L+R)//2
        MergeSort(L,mid,Arr)
        MergeSort(mid+1,R,Arr)
        merge(L,R,mid,Arr)
if __name__ == "__main__":
    Array = [7,5,3,4,6,9,1,2,8,10]
    print(f"Before Sorting: {Array}")
    MergeSort(0,len(Array)-1,Array)
    print(f"After Sorting: {Array}")