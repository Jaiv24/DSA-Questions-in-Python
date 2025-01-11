def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1 

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] < target:
            start = mid + 1 
            
        elif arr[mid] > target:
            end = mid - 1 

        else:
            return mid 

    return -1 


arr = [4,5,6,8,13,15]
result = binarySearch(arr, 15)
print(result)