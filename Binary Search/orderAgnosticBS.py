def orderAgnosticBS(arr, target):
    start = 0
    end = len(arr) - 1 

    isAsc = arr[start] < arr[end]


    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        
        elif isAsc:
            if arr[mid] < target:
                start = mid + 1 
            
            else:
                end = mid - 1 
        else:
            if arr[mid] > target:
                start = mid + 1 
            
            else:
                end = mid - 1 


    return -1 


arr = [15, 10, 5, 3, 1, 0,-8]
result = orderAgnosticBS(arr, 15)
print(result)