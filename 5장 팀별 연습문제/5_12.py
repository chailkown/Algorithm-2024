def partition(A, left, right):
    mid = (left + right) // 2
    
    if A[left] > A[mid]:
        A[left], A[mid] = A[mid], A[left]
    if A[left] > A[right]:
        A[left], A[right] = A[right], A[left]
    if A[mid] > A[right]:
        A[mid], A[right] = A[right], A[mid]
    
    pivot = A[mid]  
    
    print("피벗으로 선택된 값:", pivot)  
    
    low = left + 1
    high = right
    
    while low <= high:
        while low <= right and A[low] <= pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high

arr = [3, 6, 8, 10, 1, 2, 1]
print("원본 리스트:", arr)
partition_index = partition(arr, 0, len(arr) - 1)
print("파티션 인덱스:", partition_index)
print("파티션 이후 리스트:", arr)
